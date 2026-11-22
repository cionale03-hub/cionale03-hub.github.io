# Rebuilding CareLinx's VA Care-to-Cash Lifecycle

From referral intake to paid claim, across two VA payers.

**Role:** Product Manager, CareLinx

## Problem

VA home care runs on referrals authorizing fixed weekly hours for Respite and Home Health Aide care. Hours change mid-period, expire after 180 days, and often need extensions while a new authorization is pending. Intake, voucher balances, shift booking, and claims ran separately, so authorized hours, delivered care, and billed claims drifted apart, causing denials and revenue at risk.

## What I did

Mapped the full flow from referral to paid claim with operations, payments, and engineering: intake, voucher top-offs, timecards, autopay, claim submission, rejections, and appeals.

Designed a referral history model with one active authorization per member per program, with validation blocking overlapping, expired, or incomplete referrals. The rules are written up in [Referral validation rules](../artifacts/referral-validation-rules.md).

Specified automated voucher logic on hourly, daily, and weekly schedules that attaches vouchers for new members, rebalances when referrals change, and zeroes expired balances.

Added shift controls blocking care outside the current workweek or past expiry.

Designed a 90-day extension path so care continued and billing didn't stall while new authorizations were pending.

Planned migration of ~584 existing VA families and scoped a second payer launch.

Ran monthly governance reviews of denials, resubmissions, and pending authorizations with ops and leadership.

The sanitized lifecycle is in [Care-to-cash flow](../artifacts/care-to-cash-flow.md).

## Results

- Monthly finalized VA payments grew 64% over seven months ($2.7M to $4.4M).
- Denial rate held at 2–3% from March through August, down from 5.5% in February.
- ~$26M finalized claims, February–August.
- Revenue exposure after resubmissions: ~$790K.
- ~$621K pending-authorization revenue. Of that, only $26.5K (715 hours, March–July) is older backlog past the 90-day window. $594.9K (August–October) is still within the window.
- 5,461 extension service hours (~$202K), March–October, not covered by new authorizations.

### Denial rate by month

Percent of total claims denied. September is a partial month. July is annotated for regional authorization delays.

![VA claim denial rate by month](../artifacts/denial-rate-chart.png)

## Insight

July denials spiked to ~5%, traced to authorization delays in one regional VA network. The rate was back to 2.5% the next month as the VA cleared them.

In August, ~70% of referrals had new authorizations effective only in September or October, leaving August services uncovered: 2,213 hours, ~$82K, ~40.5% of total uncovered extension cost. Recommended pursuing retroactive authorization with the VA or a dedicated recovery process.

## Skills

- Payer authorization
- Claims and revenue cycle
- Systems design
- Requirements
- Root-cause analysis
- Cross-functional leadership
