# Referral validation rules

Sanitized product-requirements excerpt, in plain product language.

## One active referral

A member has one active referral per program. Active means the effective date is on or before today and the expiry date is after today.

## No overlapping periods

Effective periods do not overlap, unless the new referral fully replaces the current one.

## Dates

The expiry date must be after the effective date. The effective date may be backdated up to 6 months.

## Intake

At intake, at least one program group must be complete. The groups are Respite and Home Health Aide (HHA).

Each group requires:

- Referral number
- Approved weekly hours
- Effective date
- Expiry date

A partial group is rejected with a clear error.

## Shifts

A shift can be created only within the current Sunday–Saturday week, and not after authorization expiry. Same-day shifts are allowed.

## Edge cases we resolved with operations

**Can hours change after the referral is set?**  
Yes. Hours can change at any time. Renewals are set about 180 days out.

**Can hours go up as well as down?**  
Yes. Hours can increase or decrease.

**Can the effective date be in the past?**  
Yes. The effective date can be in the past, up to 6 months.

**Is the intake form still required?**  
No. The intake form is no longer required.
