import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://cloud.nzrtnetwork.com/nextcloud"
AUTH = HTTPBasicAuth("xc", "fgqWc-bsYFS-FWfk4-zPrbc-arY5Q")
NC_BASE = "/remote.php/dav/files/xc/Shared/Templates"

TEMPLATES = {}

# ─── FINANCE ────────────────────────────────────────────────────────────────

TEMPLATES["Finance/Annual Budget Template.md"] = """\
# NZRT Network — Annual Budget Template

**Period:** FY [YEAR] (1 April – 31 March)
**Prepared by:** fin
**Approved by:** xc
**Last updated:** [DATE]

---

## Revenue Forecast

| Stream | Q1 | Q2 | Q3 | Q4 | FY Total |
|--------|----|----|----|----|---------|
| ICS Consulting Retainers | | | | | |
| ICS Project Fees | | | | | |
| ITE Product Sales | | | | | |
| ITE Licensing / Royalties | | | | | |
| Other | | | | | |
| **Total Revenue** | | | | | |

---

## Operating Expenses

### Staff
| Role | Annual Salary | Q1 | Q2 | Q3 | Q4 |
|------|--------------|----|----|----|----|
| xc (Director) | | | | | |
| Contractors | | | | | |
| **Subtotal** | | | | | |

### Infrastructure & Hosting
| Item | Monthly | Annual |
|------|---------|--------|
| Hoopla cPanel hosting | | |
| Domain registrations | | |
| SSL certificates | | |
| Nextcloud / self-hosted | | |
| Kubernetes / Minikube | | |
| **Subtotal** | | |

### Software & Subscriptions
| Item | Monthly | Annual |
|------|---------|--------|
| Claude / Anthropic API | | |
| GitHub | | |
| Other SaaS | | |
| **Subtotal** | | |

### Marketing
| Item | Budget |
|------|--------|
| Website (WordPress) | |
| Advertising | |
| Content / SEO | |
| Events / Networking | |
| **Subtotal** | |

### Legal & Professional
| Item | Budget |
|------|--------|
| Accounting / Audit | |
| Legal (NZ solicitor) | |
| Patent maintenance (ITE) | |
| **Subtotal** | |

### R&D — ITE Product
| Item | Budget |
|------|--------|
| Hardware prototyping | |
| Smart contract audits | |
| Blockchain gas / deploy | |
| **Subtotal** | |

### Travel & Misc
| Item | Budget |
|------|--------|
| NZ domestic travel | |
| International travel | |
| Miscellaneous | |
| **Subtotal** | |

---

## Summary

| | FY Total |
|--|---------|
| Total Revenue | |
| Total Expenses | |
| **Net Profit / (Loss)** | |
| GST (15%) payable | |

---

*Prepared in NZD. GST registered. NZ financial year 1 April – 31 March.*
"""

TEMPLATES["Finance/Quote Template.md"] = """\
# NZRT Network — Professional Services Quote

**Quote #:** Q-[YEAR]-[NNN]
**Date:** [DATE]
**Valid until:** [DATE + 30 days]
**Prepared by:** cas / fin

---

## Client Details

| | |
|--|--|
| Client name | |
| Contact | |
| Email | |
| Phone | |
| Address | |

---

## NZRT Details

| | |
|--|--|
| Company | NZRT Network |
| Contact | xc |
| Email | admin@nzrtnetwork.com |
| GST No. | [GST NUMBER] |

---

## Scope of Work

[Brief description of what is being quoted]

---

## Fee Schedule

| # | Description | Unit | Qty | Rate (NZD) | Total (NZD) |
|---|-------------|------|-----|-----------|------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| | | | | **Subtotal** | |
| | | | | GST (15%) | |
| | | | | **Total** | |

---

## Rate Card (ICS Standard Rates)

| Role | Rate |
|------|------|
| EA Consulting (TOGAF) | $[X]/hr |
| Solution Architecture | $[X]/hr |
| Project Management | $[X]/hr |
| Development | $[X]/hr |
| Discovery / Workshop | $[X]/day |

---

## Payment Terms

- 50% deposit on acceptance
- Balance on delivery / monthly
- Payment due within 14 days of invoice
- Late payment: 2% per month

## Assumptions & Exclusions

- Excludes third-party licences unless stated
- Excludes GST unless stated
- Quote valid for 30 days

---

*Accepted by: _________________________ Date: _____________*
"""

TEMPLATES["Finance/Purchase Order Template.md"] = """\
# NZRT Network — Purchase Order

**PO #:** PO-[YEAR]-[NNN]
**Date:** [DATE]
**Raised by:** sun
**Approved by:** xc

---

## Supplier Details

| | |
|--|--|
| Supplier name | |
| Contact | |
| Email | |
| Phone | |
| Address | |
| Account # | |

---

## Delivery Details

| | |
|--|--|
| Deliver to | NZRT Network |
| Address | [Delivery address] |
| Required by | [DATE] |
| Delivery method | |

---

## Order Items

| # | Description | Part # | Qty | Unit Price (NZD) | Total (NZD) |
|---|-------------|--------|-----|-----------------|------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| | | | | **Subtotal** | |
| | | | | GST (15%) | |
| | | | | Freight | |
| | | | | **Total** | |

---

## Payment Method

- [ ] Bank transfer — NZRT account: [BSB/Account]
- [ ] Credit card
- [ ] Invoice net 20

## Notes

[Special instructions, delivery requirements, etc.]

---

**Authorised by:** xc — admin@nzrtnetwork.com
**PO raised by:** sun — procurement@nzrtnetwork.com
"""

TEMPLATES["Finance/Bank Reconciliation Template.md"] = """\
# NZRT Network — Bank Reconciliation

**Account:** [Bank] — [Account number]
**Period:** [MONTH YEAR]
**Prepared by:** fin
**Date prepared:** [DATE]

---

## Opening Balance

| | NZD |
|--|-----|
| Opening balance per bank statement | |
| Opening balance per Dolibarr | |
| Difference (must be zero from prior period) | |

---

## Reconciliation

### Bank Statement

| Date | Description | Debit | Credit | Balance |
|------|-------------|-------|--------|---------|
| | Opening balance | | | |
| | | | | |
| | | | | |
| | **Closing balance** | | | |

### Dolibarr Ledger

| Date | Reference | Debit | Credit | Balance |
|------|-----------|-------|--------|---------|
| | Opening balance | | | |
| | | | | |
| | **Closing balance** | | | |

---

## Reconciling Items

### In bank, not in Dolibarr
| Date | Description | Amount |
|------|-------------|--------|
| | | |

### In Dolibarr, not in bank
| Date | Description | Amount |
|------|-------------|--------|
| | | |

---

## Summary

| | NZD |
|--|-----|
| Bank closing balance | |
| Add: In Dolibarr not in bank | |
| Less: In bank not in Dolibarr | |
| **Adjusted balance** | |
| Dolibarr closing balance | |
| **Difference (must be zero)** | |

---

*Reviewed by: xc — Date: _____________*
"""

# ─── SALES ──────────────────────────────────────────────────────────────────

TEMPLATES["Sales/Consulting Proposal Template.md"] = """\
# NZRT ICS — Consulting Proposal

**Proposal #:** PROP-[YEAR]-[NNN]
**Date:** [DATE]
**Prepared by:** cas
**Client:** [CLIENT NAME]
**Engagement type:** [ ] Discovery  [ ] Advisory Retainer  [ ] Project Delivery

---

## Executive Summary

[2–3 sentences: the client's problem, NZRT's proposed approach, and the key outcome.]

---

## Client Context

**Organisation:** [CLIENT NAME]
**Industry:** [ ] PropTech  [ ] DeFi / Web3  [ ] Enterprise IT  [ ] Other
**Key stakeholder:** [NAME, ROLE]
**Background:** [Brief description of client's current state and challenge]

---

## Problem Statement

[Detailed description of the challenge or opportunity. What is broken, missing, or needed?]

### Pain Points

-
-
-

---

## Proposed Solution

### Approach

[Description of NZRT's methodology — e.g., TOGAF ADM phases, architecture assessments, platform delivery]

### Scope of Work

| Phase | Description | Deliverable | Duration |
|-------|-------------|-------------|----------|
| 1 — Discovery | | | |
| 2 — Architecture | | | |
| 3 — Delivery | | | |
| 4 — Handover | | | |

### Out of Scope

-
-

---

## Deliverables

| # | Deliverable | Format | Due |
|---|-------------|--------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Team

| Role | Name | Responsibility |
|------|------|---------------|
| Engagement Lead | xc | Overall delivery, client relationship |
| EA Consultant | | Architecture, TOGAF deliverables |
| Solution Architect | | Technical design |

---

## Timeline

```
Week 1–2:   Discovery & stakeholder interviews
Week 3–4:   Current state assessment
Week 5–6:   Future state architecture
Week 7–8:   Roadmap & recommendations
Week 9:     Final presentation & handover
```

---

## Fee Proposal

| Phase | Days | Day Rate | Total (NZD ex GST) |
|-------|------|----------|-------------------|
| Discovery | | | |
| Architecture | | | |
| Delivery | | | |
| Handover | | | |
| **Total** | | | |
| GST (15%) | | | |
| **Total incl. GST** | | | |

**Payment schedule:**
- 25% on engagement commencement
- 25% at end of Phase 2
- 50% on final delivery

---

## Why NZRT ICS

- TOGAF 9.2 certified enterprise architecture practice
- Deep experience in PropTech and DeFi architectures
- Full-stack: strategy through delivery
- New Zealand based, NZBN: [NZBN]

---

## Terms

- Proposal valid for 30 days
- Subject to NZRT standard service terms
- Governed by New Zealand law

---

**Accepted by:** _________________________ **Date:** _____________

**Name/Title:** _________________________
"""

TEMPLATES["Sales/Statement of Work Template.md"] = """\
# NZRT ICS — Statement of Work

**SOW #:** SOW-[YEAR]-[NNN]
**Project:** [PROJECT NAME]
**Client:** [CLIENT NAME]
**Date:** [DATE]
**Version:** 1.0

---

## 1. Project Overview

**Objective:** [One sentence — what this SOW delivers]
**Background:** [Context — why this work is needed]
**Reference:** Proposal [PROP-YEAR-NNN] dated [DATE]

---

## 2. Scope

### 2.1 In Scope

-
-
-

### 2.2 Out of Scope

-
-

### 2.3 Assumptions

- Client will provide access to relevant systems within 5 business days of SOW execution
- Client will make a named point of contact available for weekly check-ins
-

---

## 3. Deliverables

| # | Deliverable | Description | Acceptance Criteria | Due Date |
|---|-------------|-------------|-------------------|---------|
| D1 | | | | |
| D2 | | | | |
| D3 | | | | |

---

## 4. Milestones

| # | Milestone | Due Date | Dependency |
|---|-----------|---------|-----------|
| M1 | SOW signed | | — |
| M2 | Kickoff complete | | M1 |
| M3 | | | |
| M4 | Final delivery accepted | | |

---

## 5. Client Responsibilities

- Provide timely feedback (within 3 business days of deliverable submission)
- Assign a named project sponsor
- Provide system access, data, and documentation as needed
- Attend scheduled review sessions

---

## 6. NZRT Responsibilities

- Assign named engagement lead (xc)
- Deliver per schedule unless impacted by client delays
- Maintain confidentiality per NDA / service agreement
- Provide weekly status updates

---

## 7. Fees and Payment

| Item | Amount (NZD ex GST) |
|------|-------------------|
| Phase 1 | |
| Phase 2 | |
| **Total ex GST** | |
| GST (15%) | |
| **Total incl. GST** | |

Payment due: 14 days from invoice date.
Change requests beyond scope: assessed and quoted separately.

---

## 8. Change Control

Any change to scope, timeline, or budget requires a written Change Request (CR) approved by both parties before work proceeds.

---

## 9. Acceptance

Work is accepted when client provides written sign-off or fails to respond to an acceptance request within 5 business days.

---

**NZRT Network**
Signed: _________________________ Date: _____________
Name: xc

**[CLIENT NAME]**
Signed: _________________________ Date: _____________
Name/Title: _________________________
"""

TEMPLATES["Sales/Client Service Agreement Template.md"] = """\
# NZRT Network — Client Service Agreement

**Agreement #:** CSA-[YEAR]-[NNN]
**Date:** [DATE]
**Version:** 1.0

---

## Parties

**Service Provider:**
NZRT Network (trading name)
NZBN: [NZBN]
Email: admin@nzrtnetwork.com

**Client:**
[CLIENT LEGAL NAME]
[NZBN / Company number]
[Address]
Email: [CLIENT EMAIL]

---

## 1. Services

NZRT Network agrees to provide the services described in the attached Statement of Work (SOW) or Proposal, incorporated by reference.

---

## 2. Fees and Payment

2.1 Fees are as set out in the SOW or Quote.
2.2 Invoices are due within 14 days of issue.
2.3 Late payments incur interest at 2% per month.
2.4 All fees are in NZD and exclude GST unless stated.
2.5 NZRT Network is GST registered (GST No: [GST NUMBER]).

---

## 3. Term and Termination

3.1 This Agreement commences on the date signed and continues until completion of the SOW, or until terminated.
3.2 Either party may terminate with 20 business days' written notice.
3.3 Client must pay for all work completed to the date of termination.

---

## 4. Intellectual Property

4.1 NZRT Network retains ownership of all pre-existing IP, tools, frameworks, and methodologies.
4.2 On full payment, Client receives a licence to use deliverables for their internal business purposes.
4.3 NZRT Network may reference the engagement as a case study (without disclosing confidential information) unless Client objects in writing.

---

## 5. Confidentiality

5.1 Both parties agree to keep confidential information of the other party confidential for 3 years from disclosure.
5.2 Confidential information excludes information that is publicly available, independently developed, or disclosed as required by law.

---

## 6. Liability

6.1 NZRT Network's total liability is limited to the fees paid in the 3 months prior to the claim.
6.2 Neither party is liable for indirect or consequential loss.
6.3 Nothing limits liability for fraud or wilful misconduct.

---

## 7. Warranties

7.1 NZRT Network warrants services will be performed with reasonable skill and care.
7.2 NZRT Network does not warrant that deliverables will be error-free or meet all of Client's requirements beyond those specified in the SOW.

---

## 8. Dispute Resolution

8.1 Parties will attempt to resolve disputes by negotiation within 10 business days.
8.2 If unresolved, disputes are referred to mediation before litigation.
8.3 This Agreement is governed by the laws of New Zealand. Courts of New Zealand have exclusive jurisdiction.

---

## 9. General

9.1 This Agreement (with SOW/Proposal) constitutes the entire agreement between the parties.
9.2 Amendments must be in writing and signed by both parties.
9.3 If any provision is unenforceable, the remainder continues in force.

---

**NZRT Network**
Signed: _________________________ Date: _____________
Name: xc | Role: Director

**[CLIENT NAME]**
Signed: _________________________ Date: _____________
Name: _________________________ Role: _____________
"""

TEMPLATES["Sales/Client Onboarding Checklist.md"] = """\
# NZRT ICS — Client Onboarding Checklist

**Client:** [CLIENT NAME]
**Engagement:** [PROJECT / RETAINER NAME]
**Engagement lead:** xc
**CAS agent:** cas
**Start date:** [DATE]

---

## Pre-Engagement (before Day 1)

- [ ] Proposal / SOW signed and filed in Dolibarr
- [ ] Deposit invoice issued and paid
- [ ] Client added to Dolibarr as Third Party (cas)
- [ ] Engagement created in Dolibarr (cas)
- [ ] NDA signed (if required)
- [ ] CSA / service agreement signed

## Week 1 — Kickoff

- [ ] Kickoff meeting scheduled
- [ ] Client point of contact confirmed
- [ ] Shared Nextcloud folder created and access granted
- [ ] Communication channel established (email / Teams / Slack)
- [ ] Kickoff deck prepared (pam)
- [ ] Kickoff meeting held — notes filed

## Access & Systems

- [ ] Client systems access granted to NZRT team (document in SOW)
- [ ] Any required NDAs for system access signed
- [ ] Client added to relevant Nextcloud /Shared/Sales subfolder

## Documentation

- [ ] Engagement folder created in Dolibarr EDM
- [ ] Kickoff notes uploaded to Nextcloud
- [ ] Contact details recorded in Dolibarr CRM (cas)
- [ ] Project code assigned

## Ongoing

- [ ] Weekly status report scheduled (cas)
- [ ] Invoice schedule set in Dolibarr (fin)
- [ ] Retainer calendar set up (if applicable)

## Completion / Offboarding

- [ ] Final deliverable accepted in writing
- [ ] Final invoice issued and paid
- [ ] Engagement closed in Dolibarr
- [ ] Archive created in Nextcloud /Shared/Archive
- [ ] Retrospective notes filed
- [ ] Case study drafted (pam — if client consents)
"""

TEMPLATES["Sales/Consulting Engagement Letter.md"] = """\
# NZRT ICS — Consulting Engagement Letter

**Date:** [DATE]
**Reference:** EL-[YEAR]-[NNN]

---

[CLIENT NAME]
[ADDRESS]
[CITY, NEW ZEALAND]

Dear [CLIENT CONTACT NAME],

## Re: Engagement of NZRT Network — [SERVICE DESCRIPTION]

Thank you for choosing NZRT Network (ICS division) for your [consulting / architecture / advisory] needs. This letter confirms the terms of our engagement.

---

### 1. Services

We will provide the following services:

[Description of services — may reference attached SOW or Proposal]

### 2. Commencement

The engagement commences [DATE] and is expected to conclude [DATE / on completion of deliverables].

### 3. Fees

Our fees for this engagement are [NZD AMOUNT ex GST], payable as follows:

- [Deposit amount] on engagement commencement
- [Balance] on [milestone / monthly / completion]

All amounts exclude GST (15%). NZRT Network GST No: [GST NUMBER].

### 4. Your Responsibilities

To enable us to deliver effectively, we ask that you:

- Provide a named point of contact
- Make relevant staff and systems available in a timely manner
- Provide prompt feedback on deliverables (within 3 business days)

### 5. Confidentiality

Both parties agree to keep the other's confidential information confidential. Please refer to our standard Client Service Agreement for full terms.

### 6. Governing Law

This engagement is governed by the laws of New Zealand.

---

Please confirm your acceptance of this engagement by signing below and returning a copy to admin@nzrtnetwork.com.

We look forward to working with you.

Yours sincerely,

**xc**
Director, NZRT Network
admin@nzrtnetwork.com

---

**Accepted by:**

Signed: _________________________ Date: _____________
Name: _________________________
Title: _________________________
Organisation: [CLIENT NAME]
"""

TEMPLATES["Sales/RWA Tokenization Term Sheet.md"] = """\
# NZRT ITE — RWA Tokenization Term Sheet

**Term Sheet #:** ITE-TS-[YEAR]-[NNN]
**Date:** [DATE]
**Asset:** [ASSET DESCRIPTION]
**Issuer:** NZRT Network (ITE division)
**Version:** 1.0 — Non-binding indicative terms

---

> ⚠️ This term sheet is indicative only and does not constitute a binding agreement, investment advice, or an offer of financial products. Subject to legal review and regulatory compliance.

---

## 1. Asset Details

| Field | Details |
|-------|---------|
| Asset name | |
| Asset type | [ ] Real estate  [ ] Equipment  [ ] IP / Patent  [ ] Revenue stream  [ ] Other |
| Asset jurisdiction | New Zealand |
| Estimated asset value (NZD) | |
| Asset owner / originator | |
| Underlying legal structure | [ ] NZ company  [ ] Trust  [ ] Partnership  [ ] Other |

---

## 2. Token Structure

| Field | Details |
|-------|---------|
| Token standard | [ ] ERC-20  [ ] ERC-1155  [ ] ERC-721  [ ] Custom |
| Blockchain network | [ ] Base (L2 Ethereum)  [ ] Ethereum mainnet |
| Total token supply | |
| Token price (USD / NZD) | |
| Minimum investment | |
| Token divisibility | |
| Token symbol | |
| Smart contract auditor | |

---

## 3. Ownership and Rights

| Field | Details |
|-------|---------|
| Token represents | [ ] Equity  [ ] Debt / loan  [ ] Revenue share  [ ] Utility  [ ] Other |
| Voting rights | [ ] Yes  [ ] No |
| Dividend / yield rights | [ ] Yes — [FREQUENCY]  [ ] No |
| Redemption / exit mechanism | |
| Lock-up period | |
| Transfer restrictions | |

---

## 4. Distribution

| Tranche | Tokens | % | Price | Allocation |
|---------|--------|---|-------|-----------|
| Seed / private | | | | NZRT, founders |
| Strategic | | | | Partners, advisors |
| Public sale | | | | Open market |
| Reserve | | | | Treasury |
| **Total** | | 100% | | |

---

## 5. Use of Proceeds

| Use | Amount (NZD) | % |
|-----|-------------|---|
| | | |
| | | |
| Operating capital | | |
| **Total** | | 100% |

---

## 6. Compliance and Legal

| Item | Status |
|------|--------|
| NZ Financial Markets Conduct Act review | [ ] Required  [ ] Not required |
| FMA registration | [ ] Required  [ ] Exempt |
| AML/CFT compliance | [ ] In place  [ ] In progress |
| KYC requirement for investors | [ ] Yes  [ ] No |
| Accredited investor requirement | [ ] Yes  [ ] No |
| Legal counsel | |
| Smart contract audit firm | |

---

## 7. Iteasel Platform

| Feature | Details |
|---------|---------|
| Platform | Iteasel (NZRT ITE product) |
| Hardware device required | [ ] Yes  [ ] No |
| Patent reference | [PATENT NUMBER / APPLICATION] |
| Custody solution | |
| Secondary market / DEX | |

---

## 8. Timeline (Indicative)

| Milestone | Target Date |
|-----------|------------|
| Term sheet agreed | |
| Legal structure finalised | |
| Smart contract developed | |
| Smart contract audited | |
| Regulatory filing (if required) | |
| Token deployment (Base testnet) | |
| Token deployment (Base mainnet) | |
| Distribution / public sale | |

---

## 9. Key Contacts

| Role | Name | Contact |
|------|------|---------|
| NZRT ITE Lead | xc | admin@nzrtnetwork.com |
| Legal counsel | | |
| Smart contract developer | | |
| Asset originator | | |

---

*These terms are subject to change. Final terms will be set out in legally binding transaction documents. NZRT Network recommends all parties obtain independent legal and financial advice.*
"""

# ─── HR ─────────────────────────────────────────────────────────────────────

TEMPLATES["HR/Employment Contract Template.md"] = """\
# NZRT Network — Individual Employment Agreement

**Date:** [DATE]
**Reference:** EMP-[YEAR]-[NNN]

---

## Parties

**Employer:** NZRT Network, [ADDRESS], New Zealand
**Employee:** [FULL NAME], [ADDRESS]

---

## 1. Position

| | |
|--|--|
| Job title | |
| Reports to | xc (Director) |
| Department | |
| Location | [LOCATION] / Remote |
| Start date | |
| Employment type | [ ] Permanent full-time  [ ] Permanent part-time  [ ] Fixed term |
| Fixed term end (if applicable) | |
| Hours per week | |

---

## 2. Remuneration

| | |
|--|--|
| Salary / Wage | NZD [AMOUNT] per [year / hour] |
| Payment frequency | Fortnightly |
| Payment method | Bank transfer |
| Bank account | [BSB-ACCOUNT] |
| KiwiSaver | [ ] Enrolled — [3% / 4% / 6% / 8% / 10%]  [ ] Opted out |
| Employer KiwiSaver contribution | 3% (minimum) |

---

## 3. Trial Period

[ ] A 90-day trial period applies under the Employment Relations Act 2000.
The trial period commences on the start date and ends on [DATE].
During the trial period, employment may be terminated without notice and without the right to raise a personal grievance for unjustified dismissal.

[ ] No trial period applies.

---

## 4. Leave Entitlements (Holidays Act 2003)

| Leave type | Entitlement |
|-----------|------------|
| Annual leave | 4 weeks per year (after 12 months) |
| Sick leave | 10 days per year (after 6 months) |
| Public holidays | 12 per year as per NZ Holidays Act |
| Bereavement leave | 3 days (immediate family), 1 day (other) |
| Parental leave | As per Parental Leave and Employment Protection Act 1987 |
| Domestic violence leave | 10 days per year |

---

## 5. Duties

The Employee agrees to:
- Perform the duties outlined in the attached Job Description
- Follow reasonable instructions from the Employer
- Comply with NZRT Network policies and procedures
- Act in good faith

---

## 6. Confidentiality

The Employee must not disclose confidential information of NZRT Network during or after employment, including client information, system credentials, proprietary tools, and business strategies.

---

## 7. Intellectual Property

All work product, code, documents, and inventions created during employment belong to NZRT Network.

---

## 8. Outside Employment

The Employee must not undertake outside employment that conflicts with NZRT Network's interests without prior written approval from xc.

---

## 9. Termination

| Notice period | |
|---|---|
| By Employee | [X] weeks |
| By Employer (without cause) | [X] weeks |
| Serious misconduct | Immediate, no notice |

---

## 10. Dispute Resolution

Disputes will be resolved under the Employment Relations Act 2000, including mediation through the Employment Relations Authority if required.

---

## 11. Governing Law

This agreement is governed by the laws of New Zealand.

---

**Employer — NZRT Network**
Signed: _________________________ Date: _____________
Name: xc | Role: Director

**Employee**
Signed: _________________________ Date: _____________
Name: _________________________

*Employee confirms they have had the opportunity to seek independent advice before signing.*
"""

TEMPLATES["HR/Offer Letter Template.md"] = """\
# NZRT Network — Letter of Offer

**Date:** [DATE]
**Reference:** OFR-[YEAR]-[NNN]

---

[CANDIDATE FULL NAME]
[ADDRESS]
[CITY, NEW ZEALAND]

Dear [FIRST NAME],

## Re: Offer of Employment — [JOB TITLE]

On behalf of NZRT Network, I am pleased to offer you the position of **[JOB TITLE]**, subject to the conditions below.

---

### Position Details

| | |
|--|--|
| Job title | [JOB TITLE] |
| Department | |
| Reports to | xc (Director) |
| Location | [LOCATION] / Remote |
| Start date | [DATE] |
| Employment type | [ ] Permanent full-time  [ ] Part-time — [X] hrs/week |

### Remuneration

| | |
|--|--|
| Salary | NZD [AMOUNT] per annum (gross) |
| Payment | Fortnightly by bank transfer |
| Review | Annually, subject to performance |

### Conditions of Offer

This offer is conditional on:

- [ ] Satisfactory reference checks (minimum 2 referees)
- [ ] Proof of right to work in New Zealand
- [ ] Signing of the Individual Employment Agreement
- [ ] [Other condition if applicable]

### Next Steps

1. Please review this letter and the attached Individual Employment Agreement
2. You are encouraged to seek independent advice before signing
3. Please sign and return both documents by **[RESPONSE DATE]**
4. If you have questions, contact xc at admin@nzrtnetwork.com

We are excited about the contribution you will make to the NZRT Network team.

Yours sincerely,

**xc**
Director, NZRT Network
admin@nzrtnetwork.com

---

**Acceptance**

I, [FULL NAME], accept the offer of employment on the terms set out above and in the attached Individual Employment Agreement.

Signed: _________________________ Date: _____________
"""

TEMPLATES["HR/NDA Template.md"] = """\
# NZRT Network — Non-Disclosure Agreement

**Agreement #:** NDA-[YEAR]-[NNN]
**Date:** [DATE]
**Type:** [ ] Mutual  [ ] One-way (NZRT disclosing)  [ ] One-way (Receiving party disclosing)

---

## Parties

**Disclosing Party (or Party A):**
NZRT Network, [ADDRESS], New Zealand
(and/or its officers, employees, and agents)

**Receiving Party (or Party B):**
[FULL NAME / COMPANY NAME]
[ADDRESS]
[New Zealand / other jurisdiction]

---

## 1. Purpose

The parties wish to explore / undertake [DESCRIPTION OF PURPOSE — e.g., a potential business relationship, employment, engagement, technology evaluation].

In connection with this purpose, the parties may disclose Confidential Information to each other.

---

## 2. Definition of Confidential Information

"Confidential Information" means any information disclosed by one party to the other, whether in writing, orally, electronically, or by any other means, that:

- Is marked as confidential, or
- Would reasonably be understood to be confidential given its nature and the circumstances of disclosure

Including but not limited to: business plans, financial data, client lists, technical specifications, source code, system credentials, AI agent configurations, proprietary tools and methodologies, and trade secrets.

---

## 3. Obligations

Each receiving party agrees to:

3.1 Keep all Confidential Information strictly confidential
3.2 Use Confidential Information only for the Purpose set out above
3.3 Not disclose Confidential Information to any third party without prior written consent
3.4 Limit access to Confidential Information to those who need to know for the Purpose
3.5 Protect Confidential Information with at least the same degree of care used for its own confidential information, but no less than reasonable care

---

## 4. Exclusions

Obligations do not apply to information that:

- Is or becomes publicly available through no fault of the receiving party
- Was already known to the receiving party before disclosure
- Is independently developed by the receiving party without use of Confidential Information
- Must be disclosed by law or court order (receiving party must give prompt notice)

---

## 5. Term

This Agreement commences on the date signed and obligations of confidentiality continue for **3 years** from the date of last disclosure.

---

## 6. Return of Information

On request or termination of the Purpose, the receiving party will promptly return or destroy all Confidential Information and confirm destruction in writing.

---

## 7. No Licence

Nothing in this Agreement grants any licence, right, or interest in any intellectual property of the disclosing party.

---

## 8. Remedies

The parties acknowledge that breach of this Agreement may cause irreparable harm for which monetary damages are inadequate, and that injunctive relief may be appropriate.

---

## 9. Governing Law

This Agreement is governed by the laws of New Zealand. The parties submit to the non-exclusive jurisdiction of the New Zealand courts.

---

**NZRT Network (Party A)**
Signed: _________________________ Date: _____________
Name: xc | Role: Director

**[PARTY B]**
Signed: _________________________ Date: _____________
Name: _________________________ Role: _____________
"""

TEMPLATES["HR/Performance Review Template.md"] = """\
# NZRT Network — Performance Review

**Review period:** [DATE] to [DATE]
**Review type:** [ ] Probation  [ ] Annual  [ ] Mid-year  [ ] Ad hoc
**Employee:** [NAME] — [ROLE]
**Manager:** xc
**Review date:** [DATE]

---

## 1. Self-Assessment (completed by Employee)

### Key Achievements This Period

1.
2.
3.

### Challenges / Areas for Growth

1.
2.

### Support Needed

[What does the employee need from NZRT Network to perform better?]

---

## 2. Goals Review

### Goals Set Last Period

| Goal | Target | Status | Comments |
|------|--------|--------|---------|
| | | [ ] Met  [ ] Partially  [ ] Not met | |
| | | [ ] Met  [ ] Partially  [ ] Not met | |
| | | [ ] Met  [ ] Partially  [ ] Not met | |

### Overall Goal Achievement

[ ] Exceeds expectations  [ ] Meets expectations  [ ] Partially meets  [ ] Does not meet

---

## 3. Manager Assessment

### Performance Rating

| Competency | Rating (1–5) | Comments |
|-----------|-------------|---------|
| Quality of work | | |
| Initiative | | |
| Communication | | |
| Collaboration | | |
| Technical skills | | |
| Reliability / punctuality | | |
| Alignment with NZRT values | | |

**Overall rating:** [ ] 5-Outstanding  [ ] 4-Exceeds  [ ] 3-Meets  [ ] 2-Developing  [ ] 1-Unsatisfactory

### Manager Summary

[Manager's overall assessment of the employee's performance]

---

## 4. Goals for Next Period

| Goal | Measure of success | Due date | Support needed |
|------|-------------------|---------|----------------|
| | | | |
| | | | |
| | | | |

---

## 5. Development Plan

| Development area | Action | Timeline |
|-----------------|--------|---------|
| | | |
| | | |

---

## 6. Remuneration Review

[ ] No change  [ ] Salary increase: NZD [AMOUNT] effective [DATE]  [ ] Bonus: NZD [AMOUNT]
Comments:

---

## 7. Signatures

**Employee**
Signed: _________________________ Date: _____________
Comments:

**Manager (xc)**
Signed: _________________________ Date: _____________
"""

TEMPLATES["HR/Leave Request Form.md"] = """\
# NZRT Network — Leave Request Form

**Request #:** LVE-[YEAR]-[NNN]
**Date of request:** [DATE]
**Employee:** [NAME] — [ROLE]

---

## Leave Details

| | |
|--|--|
| Leave type | [ ] Annual  [ ] Sick  [ ] Bereavement  [ ] Parental  [ ] Domestic violence  [ ] Other |
| From date | |
| To date | |
| Total days | |
| Return to work date | |
| Leave balance before (days) | |
| Leave balance after (days) | |

---

## Cover Arrangements

| | |
|--|--|
| Cover arranged | [ ] Yes  [ ] No  [ ] Not required |
| Cover person | |
| Handover notes location | |

---

## Employee Declaration

I confirm the above information is correct and I have sufficient leave balance for this request.

Signed: _________________________ Date: _____________
Name: [EMPLOYEE NAME]

---

## Manager Approval

[ ] **Approved**  [ ] **Declined** — Reason: _________________________

Signed: _________________________ Date: _____________
Name: xc | Role: Director

---

*Approved leave requests are recorded in Dolibarr by han.*
"""

# ─── GENERAL ────────────────────────────────────────────────────────────────

TEMPLATES["General/SOP Template.md"] = """\
# NZRT Network — Standard Operating Procedure

**SOP #:** SOP-[SERVICE CODE]-[NNN]
**Title:** [SOP TITLE]
**Version:** 1.0
**Owner:** [ROLE CODE]
**Approved by:** xc
**Effective date:** [DATE]
**Review date:** [DATE + 12 months]
**Status:** [ ] Draft  [ ] Active  [ ] Archived

---

## 1. Purpose

[One paragraph: why this SOP exists, what problem it solves, and what outcome it ensures.]

---

## 2. Scope

**Applies to:** [Who or what this SOP covers]
**Does not apply to:** [Exclusions]
**Related systems:** [ ] Dolibarr  [ ] Nextcloud  [ ] WordPress  [ ] GitHub  [ ] Kubernetes  [ ] Other

---

## 3. Definitions

| Term | Definition |
|------|-----------|
| | |
| | |

---

## 4. Responsibilities

| Role | Responsibility |
|------|---------------|
| xc | Approval, escalation |
| [ROLE] | [Primary responsibility] |
| [ROLE] | [Secondary responsibility] |

---

## 5. Procedure

### Step 1 — [Step Name]

**Who:** [ROLE]
**When:** [Trigger / schedule]

1.
2.
3.

### Step 2 — [Step Name]

**Who:** [ROLE]
**When:** After Step 1

1.
2.
3.

### Step 3 — [Step Name]

1.
2.

---

## 6. Verification / Quality Check

| Check | Who | Method |
|-------|-----|--------|
| | | |
| | | |

---

## 7. Exception Handling

| Exception | Action | Escalate to |
|-----------|--------|------------|
| | | xc |
| | | |

---

## 8. References

- [[Related SOP or doc]]
- [[Infrastructure/09 - AI Agents/Agent Tasks|Agent Tasks]]

---

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | xc | Initial version |
"""

TEMPLATES["General/Meeting Minutes Template.md"] = """\
# Meeting Minutes

**Meeting title:** [TITLE]
**Date:** [DATE]
**Time:** [START] – [END] (NZT)
**Location:** [ ] In person — [LOCATION]  [ ] Video call  [ ] Phone
**Facilitator:** [NAME]
**Minuted by:** [NAME]
**Reference:** MTG-[YEAR]-[NNN]

---

## Attendees

| Name | Role | Present |
|------|------|---------|
| xc | Director | [ ] |
| | | [ ] |
| | | [ ] |

**Apologies:**

---

## Agenda

| # | Item | Lead | Time |
|---|------|------|------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | AOB | | |

---

## Previous Action Items Review

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| | | | | [ ] Done  [ ] Carried  [ ] Dropped |
| | | | | [ ] Done  [ ] Carried  [ ] Dropped |

---

## Discussion

### Item 1 — [TITLE]

**Discussion:**

**Decision:**

**Action items:**

---

### Item 2 — [TITLE]

**Discussion:**

**Decision:**

**Action items:**

---

### Item 3 — [TITLE]

**Discussion:**

**Decision:**

**Action items:**

---

### AOB (Any Other Business)

---

## Action Items Summary

| # | Action | Owner | Due | Priority |
|---|--------|-------|-----|---------|
| 1 | | | | [ ] High  [ ] Med  [ ] Low |
| 2 | | | | [ ] High  [ ] Med  [ ] Low |
| 3 | | | | [ ] High  [ ] Med  [ ] Low |

---

**Next meeting:** [DATE / TBC]
**Minutes approved by:** xc — Date: _____________
"""

TEMPLATES["General/Project Status Report Template.md"] = """\
# NZRT Network — Project Status Report

**Project:** [PROJECT NAME]
**Report #:** PSR-[YEAR]-[NNN]
**Reporting period:** [DATE] to [DATE]
**Project manager:** [ROLE / NAME]
**Client:** [CLIENT NAME or Internal]
**Date issued:** [DATE]

---

## Overall Status

| Dimension | Status | Trend |
|-----------|--------|-------|
| **Schedule** | [ ] On track  [ ] At risk  [ ] Behind | [ ] ↑  [ ] →  [ ] ↓ |
| **Budget** | [ ] On track  [ ] At risk  [ ] Over | [ ] ↑  [ ] →  [ ] ↓ |
| **Scope** | [ ] Stable  [ ] Change pending  [ ] Expanded | [ ] ↑  [ ] →  [ ] ↓ |
| **Quality** | [ ] On track  [ ] At risk  [ ] Issue | [ ] ↑  [ ] →  [ ] ↓ |

**Overall RAG:** [ ] 🟢 Green  [ ] 🟡 Amber  [ ] 🔴 Red

**Summary (2–3 sentences):**

---

## Progress This Period

| Milestone / Deliverable | Due | Status |
|------------------------|-----|--------|
| | | [ ] Done  [ ] In progress  [ ] Not started  [ ] Delayed |
| | | [ ] Done  [ ] In progress  [ ] Not started  [ ] Delayed |
| | | [ ] Done  [ ] In progress  [ ] Not started  [ ] Delayed |

**Key achievements:**
-
-

---

## Planned Next Period

| Activity | Owner | Due |
|----------|-------|-----|
| | | |
| | | |
| | | |

---

## Risks and Issues

### Active Risks

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|------|-----------|--------|-----------|-------|
| | | H/M/L | H/M/L | | |

### Active Issues

| # | Issue | Impact | Action | Owner | Due |
|---|-------|--------|--------|-------|-----|
| | | | | | |

---

## Budget Summary

| | Budget (NZD) | Actual to Date | Forecast | Variance |
|--|-------------|---------------|---------|---------|
| Fees | | | | |
| Expenses | | | | |
| **Total** | | | | |

---

## Decisions Required

| # | Decision needed | From whom | By when |
|---|----------------|----------|---------|
| | | | |

---

## Change Requests

| CR # | Description | Status |
|------|-------------|--------|
| | | [ ] Pending  [ ] Approved  [ ] Rejected |

---

*Report prepared by [NAME]. Distributed to: [LIST]*
"""

TEMPLATES["General/Risk Register Template.md"] = """\
# NZRT Network — Risk Register

**Project / Domain:** [PROJECT NAME or NZRT Operational]
**Owner:** xc
**Last updated:** [DATE]
**Review frequency:** Monthly

---

## Risk Rating Matrix

| | Low Impact | Medium Impact | High Impact |
|--|-----------|--------------|------------|
| **High Likelihood** | Medium | High | Critical |
| **Med Likelihood** | Low | Medium | High |
| **Low Likelihood** | Low | Low | Medium |

---

## Risk Register

| ID | Category | Risk Description | Likelihood | Impact | Rating | Mitigation Strategy | Contingency | Owner | Status | Last Reviewed |
|----|----------|-----------------|-----------|--------|--------|-------------------|------------|-------|--------|--------------|
| R001 | Technology | Nextcloud server outage | M | H | High | Daily backups to NAS; documented recovery SOP | Restore from backup within 4 hours | dan | Open | |
| R002 | Technology | AI agent credential compromise | L | H | High | Tailscale VPN; per-agent scoped API keys; audit logging | Revoke keys immediately; rotate all credentials | xc | Open | |
| R003 | Financial | Client non-payment | M | M | Medium | 50% deposit upfront; 14-day payment terms; late payment clause | Legal action; suspend services | fin | Open | |
| R004 | Legal | IP dispute over Iteasel patent | L | H | High | Patent filed and maintained; NDA with all partners | Legal counsel engaged; cease & desist | xc | Open | |
| R005 | Operational | Key person dependency (xc) | M | H | High | Document all procedures in Obsidian vault; SOPs current | Succession plan; contractor engagement | xc | Open | |
| R006 | Technology | Smart contract bug / exploit (ITE) | L | H | High | Third-party audit before mainnet deploy; testnet first | Pause contract; notify holders; patch | xc | Open | |
| R007 | Compliance | GST / tax filing failure | L | H | High | Dolibarr accounting; fin agent monitoring; accountant review | Voluntary disclosure to IRD | fin | Open | |
| R008 | | | | | | | | | Open | |

---

## Closed Risks

| ID | Description | Closed date | Resolution |
|----|-------------|------------|-----------|
| | | | |

---

## Notes

- Ratings reviewed monthly by xc and fin
- Critical risks reported to Board / stakeholders immediately
- Risk register stored in Nextcloud /Shared/Analytics
"""

TEMPLATES["General/EA Deliverable Template.md"] = """\
# NZRT ICS — Enterprise Architecture Deliverable

**Deliverable #:** EA-[PHASE]-[YEAR]-[NNN]
**Title:** [DELIVERABLE TITLE]
**TOGAF ADM Phase:** [ ] Preliminary  [ ] A: Vision  [ ] B: Business  [ ] C: Info Systems  [ ] D: Technology  [ ] E: Opportunities  [ ] F: Migration  [ ] G: Implementation  [ ] H: Change
**Client:** [CLIENT NAME or NZRT Internal]
**Author:** xc
**Reviewer:** [NAME]
**Date:** [DATE]
**Version:** 1.0
**Status:** [ ] Draft  [ ] In Review  [ ] Approved  [ ] Baselined

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [DATE] | xc | Initial draft |
| 1.0 | [DATE] | xc | Approved |

---

## 1. Executive Summary

[2–3 sentences: what this deliverable covers, the key findings or decisions, and the recommended next step.]

---

## 2. Architecture Context

### 2.1 Scope

**In scope:**
-

**Out of scope:**
-

### 2.2 Stakeholders

| Stakeholder | Role | Interest |
|------------|------|---------|
| | | |

### 2.3 Architecture Principles Applied

| Principle | Source | Application |
|-----------|--------|------------|
| | TOGAF 9.2 | |
| | NZRT Architecture Principles | |

---

## 3. Current State (Baseline Architecture)

### 3.1 Overview

[Description of the current state relevant to this phase]

### 3.2 Architecture Diagrams

*[Insert or reference ArchiMate / C4 diagrams here]*

### 3.3 Gaps and Pain Points

| # | Gap | Impact | Priority |
|---|-----|--------|---------|
| | | | H/M/L |

---

## 4. Target State (Target Architecture)

### 4.1 Vision

[Description of the desired future state]

### 4.2 Architecture Diagrams

*[Insert or reference ArchiMate / C4 diagrams here]*

### 4.3 Architecture Decisions

| ID | Decision | Rationale | Alternatives Considered |
|----|---------|-----------|------------------------|
| AD-001 | | | |

---

## 5. Gap Analysis

| Capability | Current | Target | Gap | Priority |
|-----------|---------|--------|-----|---------|
| | | | | H/M/L |

---

## 6. Roadmap

| Initiative | Phase | Dependency | Effort | Business Value |
|-----------|-------|-----------|--------|---------------|
| | | | H/M/L | H/M/L |

---

## 7. Risks and Assumptions

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| | H/M/L | H/M/L | |

### Assumptions

-
-

---

## 8. Next Steps

| # | Action | Owner | Due |
|---|--------|-------|-----|
| | | | |

---

## 9. References

- TOGAF 9.2 — The Open Group
- ArchiMate 3.1
- [[Togaf/NZRT Architecture/Architecture Principles]]
- [[Domains/togaf]]

---

*Approved by: xc — Date: _____________*
"""

TEMPLATES["General/Technical Specification Template.md"] = """\
# NZRT ITE — Technical Specification

**Spec #:** ITE-SPEC-[YEAR]-[NNN]
**Title:** [COMPONENT / SYSTEM / FEATURE NAME]
**Product:** Iteasel
**Author:** dan / xc
**Reviewer:** [NAME]
**Date:** [DATE]
**Version:** 1.0
**Status:** [ ] Draft  [ ] In Review  [ ] Approved

---

## 1. Overview

### 1.1 Purpose

[What this specification covers and why it exists]

### 1.2 Scope

**In scope:**
-

**Out of scope:**
-

### 1.3 References

| Document | Version | Location |
|---------|---------|---------|
| | | |

---

## 2. System Context

### 2.1 Architecture Overview

[High-level description of where this component fits in the Iteasel system]

*[Reference or insert architecture diagram]*

### 2.2 Dependencies

| Dependency | Type | Version | Notes |
|-----------|------|---------|-------|
| Base (L2 Ethereum) | Blockchain | — | RWA token deployment |
| Solidity | Language | ^0.8.x | Smart contracts |
| Hardhat | Dev tooling | latest | Compile, test, deploy |
| | | | |

---

## 3. Functional Requirements

| ID | Requirement | Priority | Notes |
|----|-------------|---------|-------|
| FR-001 | | Must | |
| FR-002 | | Should | |
| FR-003 | | Could | |

---

## 4. Non-Functional Requirements

| ID | Category | Requirement | Target |
|----|---------|-------------|--------|
| NFR-001 | Performance | | |
| NFR-002 | Security | | |
| NFR-003 | Availability | Uptime | 99.9% |
| NFR-004 | Scalability | | |

---

## 5. Hardware Specifications (if applicable)

| Component | Specification | Notes |
|---------|--------------|-------|
| Processor | | |
| Memory | | |
| Storage | | |
| Connectivity | | |
| Power | | |
| Form factor | | |
| Operating temperature | | |
| Patent reference | [PATENT #] | |

---

## 6. Smart Contract Specification (if applicable)

### 6.1 Contract Overview

| Field | Value |
|-------|-------|
| Standard | ERC-20 / ERC-1155 / custom |
| Network | Base (L2 Ethereum) |
| Solidity version | |
| Upgradeable | [ ] Yes (proxy pattern)  [ ] No |
| Audited by | |

### 6.2 Key Functions

| Function | Visibility | Parameters | Returns | Description |
|---------|-----------|-----------|---------|-------------|
| | public / external | | | |

### 6.3 Events

| Event | Parameters | Emitted when |
|-------|-----------|-------------|
| | | |

### 6.4 Access Control

| Role | Capabilities |
|------|-------------|
| Owner | |
| Admin | |
| Minter | |

---

## 7. API Specification (if applicable)

### Endpoint: [METHOD] /path

**Description:**
**Auth:** Bearer token / API key / none
**Request:**
```json
{
  "field": "type"
}
```
**Response (200):**
```json
{
  "field": "type"
}
```
**Error codes:**
| Code | Meaning |
|------|---------|
| 400 | |
| 401 | |
| 500 | |

---

## 8. Security Considerations

-
-
- Credentials: never hardcoded; use environment variables / Nextcloud CREDS
- Smart contract: re-entrancy guards; access control; emergency pause

---

## 9. Testing Requirements

| Test type | Coverage target | Tool |
|----------|----------------|------|
| Unit tests | 90%+ | Hardhat / pytest |
| Integration tests | | |
| Security audit | | External auditor |
| Testnet deployment | | Base Sepolia |

---

## 10. Deployment

| Environment | Network | Notes |
|-------------|---------|-------|
| Development | Local / Hardhat | |
| Staging | Base Sepolia testnet | |
| Production | Base mainnet | Audit required first |

---

*Approved by: xc — Date: _____________*
"""

# ─── UPLOAD ─────────────────────────────────────────────────────────────────

def upload(remote_path, content):
    url = f"{BASE_URL}{NC_BASE}/{remote_path}"
    r = requests.put(url, auth=AUTH,
        headers={"Content-Type": "text/markdown; charset=utf-8"},
        data=content.encode("utf-8"))
    ok = r.status_code in (201, 204)
    print(f"  {'OK' if ok else 'FAIL ' + str(r.status_code)}: {remote_path}")


if __name__ == "__main__":
    for path, content in TEMPLATES.items():
        upload(path, content)
    print(f"\nDone — {len(TEMPLATES)} templates uploaded.")
