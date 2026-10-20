# Care-to-cash flow

Sanitized lifecycle from referral intake to a paid or rejected claim, including the branch when an authorization is expiring.

```mermaid
flowchart TD
    intake["Referral intake"] --> auth["Authorization & voucher setup"]
    auth --> topup["Voucher top-off & rebalancing<br/>hourly / daily / weekly"]
    topup --> shifts["Shift scheduling controls<br/>current workweek, not past expiry"]
    shifts --> timecards["Timecards & autopay"]
    timecards --> claim["Claim generation"]
    claim --> clearinghouse["Clearinghouse"]
    clearinghouse --> payer["Payer"]
    payer --> outcome{"Paid / Rejected"}
    outcome -->|Paid| paid["Paid"]
    outcome -->|Rejected| fix["Correct & resubmit or Appeal"]

    auth --> expiring["Authorization expiring"]
    expiring --> received{"New referral received?"}
    received -->|Yes| add["Add new authorization"]
    received -->|No| extension["90-day extension"]
    extension --> wait["Wait for new authorization"]
```

The lifecycle runs from referral intake into authorization and voucher setup, then voucher top-off and rebalancing on hourly, daily, and weekly schedules. Shift scheduling is limited to the current workweek and cannot pass authorization expiry; timecards and autopay follow, and claim generation sends the claim through the clearinghouse to the payer, where it is paid or rejected and then corrected and resubmitted or appealed. When an authorization is expiring, a new referral adds a new authorization; if none has arrived, a 90-day extension is used while waiting for a new authorization.
