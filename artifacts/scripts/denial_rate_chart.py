#!/usr/bin/env python3
"""Generate artifacts/denial-rate-chart.png.

VA claim denial rate by month, as a percent of total claims.
September is marked as a partial month. July is annotated
"Regional authorization delays". Percentages only.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager

TEAL = "#0f5e63"
INK = "#14212b"
MUTED = "#5b6670"
GRID = "#e3e6e8"
CALLOUT_BG = "#e6f0f0"

MONTHS = ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
RATES = [5.5, 2.5, 2.4, 2.9, 3.4, 5.1, 2.5, 1.0]
JULY_INDEX = 5
SEPTEMBER_INDEX = 7

OUTPUT = Path(__file__).resolve().parents[1] / "denial-rate-chart.png"


def register_fonts() -> str:
    """Prefer Inter when it is installed. Fall back to DejaVu Sans."""
    registered = False
    for font_path in font_manager.findSystemFonts():
        name = Path(font_path).name.lower()
        if name.startswith("inter") and name.endswith((".ttf", ".otf")):
            font_manager.fontManager.addfont(font_path)
            registered = True
    return "Inter" if registered else "DejaVu Sans"


def build_chart(font_family: str) -> plt.Figure:
    plt.rcParams.update(
        {
            "font.family": font_family,
            "axes.unicode_minus": False,
            "figure.facecolor": "white",
            "savefig.facecolor": "white",
            "axes.facecolor": "white",
        }
    )

    fig, ax = plt.subplots(figsize=(11.2, 6.3), dpi=180)
    positions = list(range(len(MONTHS)))
    bars = ax.bar(
        positions,
        RATES,
        width=0.64,
        color=TEAL,
        zorder=3,
        linewidth=0,
    )

    for index, (bar, rate) in enumerate(zip(bars, RATES)):
        label = f"{rate:.1f}%"
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            rate + 0.16,
            label,
            ha="center",
            va="bottom",
            fontsize=12,
            color=INK,
            fontweight="medium",
            zorder=4,
        )
        if index == SEPTEMBER_INDEX:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                rate + 0.62,
                "partial month",
                ha="center",
                va="bottom",
                fontsize=10,
                color=MUTED,
                fontstyle="italic",
                zorder=4,
            )

    ax.annotate(
        "Regional authorization delays",
        xy=(JULY_INDEX, RATES[JULY_INDEX] + 0.08),
        xytext=(2.15, 7.15),
        ha="center",
        va="center",
        fontsize=11.5,
        color=TEAL,
        fontweight="medium",
        zorder=5,
        arrowprops={
            "arrowstyle": "-|>",
            "color": TEAL,
            "lw": 1.15,
            "shrinkA": 2,
            "shrinkB": 2,
            "mutation_scale": 12,
        },
        bbox={
            "boxstyle": "round,pad=0.45",
            "facecolor": CALLOUT_BG,
            "edgecolor": TEAL,
            "linewidth": 0.9,
        },
    )

    ax.set_title(
        "VA claim denial rate by month",
        loc="left",
        fontsize=18,
        color=INK,
        fontweight="semibold",
        pad=16,
    )
    ax.set_ylabel("Denial rate (% of total)", fontsize=12, color=INK, labelpad=10)
    ax.set_xticks(positions)
    ax.set_xticklabels(MONTHS, fontsize=12, color=INK)
    ax.set_ylim(0, 8.2)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.set_yticklabels(["0%", "2%", "4%", "6%", "8%"], fontsize=11, color=MUTED)
    ax.yaxis.grid(True, linestyle="-", linewidth=0.7, color=GRID, zorder=0)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", length=0, pad=8)
    ax.tick_params(axis="y", length=0, pad=6)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#d5dbde")
    ax.spines["bottom"].set_linewidth(0.8)
    ax.margins(x=0.04)

    fig.tight_layout()
    return fig


def main() -> None:
    font_family = register_fonts()
    figure = build_chart(font_family)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT, bbox_inches="tight", pad_inches=0.35)
    plt.close(figure)


if __name__ == "__main__":
    main()
