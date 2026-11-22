# Period-based benefit ledger for payer-funded home care

**Role:** Product Owner, CareLinx. Wrote the PRD, business rules, and UX requirements across the internal ops dashboard, shift scheduling, invoice payment, caregiver app, and member app.

**Payers:** VA and commercial health-plan partners.

## Problem

Voucher balances — the care hours a payer authorizes for a member — were tracked as one cumulative total. The system could not tell whether hours were used inside the right week, month, or year, so it could schedule or pay out more care than a program authorized in a period. Eligibility changes, authorization renewals, and reduced hours were not reflected cleanly in balances, and ops had no reliable data for utilization reporting.

## Goal

Tie every balance check and deduction to a time-bound budget envelope that matches each program's frequency, so the system cannot reserve or pay more than is authorized in a period, and balances stay in sync across scheduling and payment.

## What I defined

- **Ledger model.** Each program gets period records (weekly Sun–Sat, monthly, annual split at year-end, or one-time), each starting at the program's authorized hours. Records are created when a member's first job completes, when a new authorization from a VA or commercial health-plan partner starts, and when eligibility is reinstated.
- **Journal of every change.** Every credit or debit is a categorized transaction: coverage increase, manual credit, shift paid, coverage loss, or manual debit. Balances are always the sum of the journal, so they stay auditable. Manual debits can never push a balance negative.
- **Guardrails at scheduling.** Shifts can be created only inside an active ledger period with enough remaining hours (remaining minus hours already reserved), in both the internal scheduling tool and the caregiver app, with a clear error when they cannot.
- **Guardrails at payment.** Invoices pay only when the correct period has enough hours. Otherwise an automatic insufficient-hours validation blocks payment.
- **Eligibility lifecycle.** For health-plan members, extensions add periods. Terminations shorten the current period, zero out future balances, auto-cancel future confirmed shifts with notifications, and generate a high-priority follow-up task for the care team. Reactivations restore coverage and block shifts during the gap.
- **Ops visibility.** A Vouchers view in the internal ops dashboard shows each member's vouchers, period ledgers (starting, used, credits, remaining), and a searchable transaction history, plus an Adjust Ledger Balance flow with required notes, limits, and validation.
- **Migration and backfill.** Balances are rebuilt from paid shift history for each program and period, with a defined cut-off date.

## Success measures

- 100% of programs migrated to the ledger
- Overutilization baseline established

Outcome metrics to be added.

## What it shows

I can translate payer authorization rules into a financial-grade data model, design guardrails that prevent revenue leakage before it happens, and coordinate one change across scheduling, payment, mobile, and ops tools.

## Skills

Benefits & authorization modeling · Revenue integrity · Eligibility workflows · Internal tooling · PRD & business rules · Cross-platform delivery
