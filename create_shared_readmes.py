"""
Upload README.md files to every /Shared/ subfolder via WebDAV.
Auth: xc app token (owner of all /Shared/ folders).
"""

import requests
from requests.auth import HTTPBasicAuth
import time

NC_URL = "https://cloud.nzrtnetwork.com/nextcloud"
XC_USER = "xc"
XC_TOKEN = "fgqWc-bsYFS-FWfk4-zPrbc-arY5Q"
AUTH = HTTPBasicAuth(XC_USER, XC_TOKEN)
WEBDAV = f"{NC_URL}/remote.php/dav/files/{XC_USER}"

READMES = {
    "Shared/Marketing/Brand": """# Brand

Logos, colour palette, typography, and brand guidelines for NZRT Network (ICS and ITE).

## Contents
- Logo files (SVG, PNG) in multiple sizes
- Colour palette reference
- Typography guide
- Brand usage guidelines

## Managed by
pam — Products and Marketing agent. Contact pam for brand asset requests or updates.
""",
    "Shared/Marketing/Campaigns": """# Campaigns

Campaign briefs, assets, and documentation organised by campaign name.

## Structure
Each campaign gets its own subfolder: `/Campaigns/[Campaign_Name]/`

## Contents
- Campaign briefs
- Creative assets (images, copy, design files)
- Performance notes

## Managed by
pam
""",
    "Shared/Marketing/Social": """# Social

Social media content, schedules, and platform-specific assets.

## Contents
- Post copy and captions
- Image/video assets sized per platform
- Content calendars and schedules

## Platforms
LinkedIn, Instagram, Facebook — primary channels for ICS and ITE.

## Managed by
pam
""",
    "Shared/Marketing/Product_Sheets": """# Product Sheets

One-page product and service sheets for ICS consulting services and ITE hardware product.

## Contents
- ICS service one-pagers
- ITE product sheets
- Feature comparison sheets

## Managed by
pam — coordinates with cas for client-facing versions.
""",
    "Shared/Marketing/Blog_Drafts": """# Blog Drafts

Draft blog posts before upload to WordPress (nzrtnetwork.com).

## Workflow
1. Draft created here as Markdown or ODT
2. pam reviews and edits
3. pam uploads final version to WordPress via WP REST API
4. File moved to /Archive after publish

## Managed by
pam
""",
    "Shared/Marketing/Media": """# Media

Images, videos, and graphics for all marketing channels.

## Contents
- Product photography (ITE hardware)
- Team photos
- Video assets
- Infographics and diagrams

## File naming
`[type]-[subject]-[YYYY-MM-DD].[ext]` — e.g. `photo-ite-device-2026-04-01.jpg`

## Managed by
pam
""",
    "Shared/Sales/Clients": """# Clients

One folder per client containing all documents for that relationship.

## Structure
```
/Clients/[Client_Name]/
  /Contracts
  /Proposals
  /Quotes
  /Correspondence
```

## Managed by
cas — Customer and Sales agent.
""",
    "Shared/Sales/Active_Deals": """# Active Deals

Documents for deals currently in the sales pipeline.

## Contents
- Active proposals awaiting sign-off
- In-progress negotiation documents
- Meeting notes for open deals

## Note
Closed/won deals move to `/Clients/[Name]/Contracts`. Lost deals move to `/Archive`.

## Managed by
cas
""",
    "Shared/Sales/CRM_Export": """# CRM Export

CSV and JSON exports from Dolibarr CRM for offline analysis and reporting.

## Contents
- Third-party (client) records export
- Proposal pipeline exports
- Order history exports

## Schedule
cas exports as needed; dai reads for analytics.

## Managed by
cas (writes), dai (reads)
""",
    "Shared/Sales/Onboarding": """# Onboarding

New client onboarding documentation and checklists.

## Contents
- Client onboarding checklist (template in /Shared/Templates/Sales/)
- Welcome packs
- System access instructions for new clients

## Managed by
cas
""",
    "Shared/Procurement/Purchase_Orders": """# Purchase Orders

All purchase orders issued by NZRT, organised by year.

## Structure
```
/Purchase_Orders/[YEAR]/
  PO-[YEAR]-[NNN].pdf
```

## Source
sun generates POs in Dolibarr and uploads PDFs here.

## Retention
3 years

## Managed by
sun — Supplier and Purchase agent.
""",
    "Shared/Procurement/Vendors": """# Vendors

Vendor contracts and pricing, one folder per vendor.

## Structure
```
/Vendors/[Vendor_Name]/
  /Contracts
  /Pricing
```

## Managed by
sun
""",
    "Shared/Procurement/RFQs": """# RFQs

Requests for Quotation sent to suppliers.

## Contents
- RFQ documents (PDF)
- Supplier responses
- Evaluation notes

## Managed by
sun
""",
    "Shared/Procurement/Invoices_Received": """# Invoices Received

Vendor invoices received by NZRT — input to Dolibarr Accounts Payable.

## Workflow
1. Vendor invoice received (email/post)
2. sun saves PDF here
3. sun creates matching record in Dolibarr
4. fin reconciles against payment

## Retention
3 years (7 years recommended for tax purposes — consider moving to Finance)

## Managed by
sun
""",
    "Shared/Procurement/Delivery_Notes": """# Delivery Notes

Delivery dockets and goods received notes.

## Contents
- Supplier delivery notes (PDF/scan)
- Goods received confirmations

## Managed by
sun
""",
    "Shared/Finance/Invoices": """# Invoices

Sales invoices issued by NZRT to clients, organised by year and month.

## Structure
```
/Invoices/[YEAR-MM]/
  INV-[NNN]-[YEAR].pdf
```

## Source
fin exports invoices from Dolibarr Billing module.

## Retention
7 years (NZ IRD requirement)

## Managed by
fin — Finance and Accounting agent.
""",
    "Shared/Finance/Bank_Statements": """# Bank Statements

**WARNING: End-to-end encrypted folder. xc and fin access only.**

Bank statements from all NZRT accounts, organised by year.

## Structure
```
/Bank_Statements/[YEAR]/
  [BANK]-[ACCOUNT]-[YYYY-MM].pdf
```

## Retention
7 years (NZ IRD requirement)

## Managed by
fin (E2EE — handle with care)
""",
    "Shared/Finance/Reconciliations": """# Reconciliations

Monthly bank and account reconciliation workbooks.

## Contents
- Monthly reconciliation spreadsheets (ODS)
- Discrepancy notes
- Signed-off reconciliation summaries

## Managed by
fin
""",
    "Shared/Finance/Budget": """# Budget

Annual budgets and quarterly forecasts.

## Structure
```
/Budget/
  [YEAR]_Budget.xlsx
  [YEAR]_Q[N]_Forecast.xlsx
```

## Managed by
fin — with input from xc for strategic targets.
""",
    "Shared/Finance/Reports": """# Reports

Financial reports — monthly P&L, cash flow, and annual summaries.

## Structure
```
/Reports/
  /Monthly/   — [YYYY-MM]_[Report_Type].pdf
  /Annual/    — [YYYY]_Annual_Report.pdf
```

## Managed by
fin (dai reads for analytics cross-reference)
""",
    "Shared/Finance/Tax_GST": """# Tax / GST

GST returns, IRD correspondence, and tax documents.

## Contents
- GST return workbooks (NZ GST 15%)
- IRD filing confirmations
- Tax invoices where required

## NZ compliance
GST returns filed two-monthly via Dolibarr (fin) and submitted to IRD.

## Retention
7 years (IRD requirement)

## Managed by
fin
""",
    "Shared/Finance/Purchase_Orders": """# Purchase Orders (Finance copy)

Purchase orders received from sun for payment processing.

## Purpose
fin matches POs against vendor invoices in Accounts Payable workflow.

## Source
Copies from /Shared/Procurement/Purchase_Orders/ — fin reads for payment approval.

## Managed by
fin
""",
    "Shared/HR/Employees": """# Employees

**CONFIDENTIAL — E2EE mandatory. xc and han access only.**

Individual employee records.

## Structure
```
/Employees/
  /Active/
    /[Employee_Name]/   — Contract, ID copy, review history
  /Departed/
    /[Employee_Name]/   — Retained per NZ employment law
```

## NZ law
Employment Relations Act 2000 — retain records for 6 years after employment ends.

## Managed by
han — Human Resources agent.
""",
    "Shared/HR/Payroll": """# Payroll

**CONFIDENTIAL — E2EE mandatory. xc and han access only.**

Payroll files organised by year.

## Structure
```
/Payroll/[YEAR]/
  [YYYY-MM]_Payroll.ods
```

## NZ compliance
Holidays Act 2003 — leave entitlements calculated by han via Dolibarr HR module.

## Managed by
han
""",
    "Shared/HR/Onboarding": """# Onboarding

Employee onboarding checklists and forms.

## Contents
- New employee checklists (template: /Shared/Templates/HR/)
- Tax code declaration (IR330)
- KiwiSaver enrolment forms
- Equipment issue records

## Managed by
han
""",
    "Shared/HR/Policies": """# Policies

HR policy documents for NZRT Network.

## Contents
- Employment policy manual
- Leave policy (annual, sick, bereavement — Holidays Act 2003)
- Code of conduct
- Health and safety policy
- Remote work policy

## Managed by
han — updates approved by xc.
""",
    "Shared/HR/Leave_Records": """# Leave Records

Employee leave requests and approvals.

## Contents
- Leave request forms
- Approved leave records
- Leave balance summaries

## Source
han manages leave in Dolibarr HR module; PDF records stored here.

## Managed by
han
""",
    "Shared/HR/Performance_Reviews": """# Performance Reviews

**CONFIDENTIAL — E2EE mandatory. xc and han access only.**

Annual and mid-year performance reviews.

## Structure
```
/Performance_Reviews/
  /[Employee_Name]/
    [YYYY]_Annual_Review.pdf
    [YYYY]_H1_Checkin.pdf
```

## Managed by
han
""",
    "Shared/Analytics/Reports": """# Reports

Analytics reports — weekly, monthly, and annual summaries across all NZRT systems.

## Structure
```
/Reports/
  /Weekly/   — [YYYY-WNN]_Weekly_Summary.md
  /Monthly/  — [YYYY-MM]_Monthly_Report.md
  /Annual/   — [YYYY]_Annual_Analytics.md
```

## Source
dai generates from Dolibarr exports, NC activity data, and WordPress stats.

## Managed by
dai — Data and Analytics agent.
""",
    "Shared/Analytics/Exports": """# Exports

Raw data exports from Dolibarr and cross-system sources.

## Structure
```
/Exports/
  /Dolibarr_Exports/  — Raw Dolibarr CSV/JSON
  /Cross_System/      — Combined data from multiple sources
```

## Retention
Rolling 1 year — older exports purged by dai.

## Managed by
dai
""",
    "Shared/Analytics/Dashboards": """# Dashboards

Dashboard snapshots and configuration files.

## Contents
- KPI dashboard exports (PDF/PNG snapshots)
- Dashboard config files
- Chart data sources

## Managed by
dai
""",
    "Shared/Database/Backups": """# Backups

Automated database backups — daily and weekly MySQL dumps.

## Structure
```
/Backups/
  /Daily/   — nzrt_[YYYY-MM-DD].sql.gz  (30-day retention)
  /Weekly/  — nzrt_weekly_[YYYY-WNN].sql.gz  (1-year retention)
```

## Schedule
Daily backups: 2 AM NZST via dan automated job.

## Managed by
dan — DBA agent.
""",
    "Shared/Database/Logs": """# Logs

System and error logs from NZRT infrastructure.

## Structure
```
/Logs/
  /System_Logs/  — General system activity
  /Error_Logs/   — Errors and warnings
```

## Retention
90 days rolling.

## Managed by
dan
""",
    "Shared/Database/Archive": """# Archive

Backups beyond active retention period — kept for compliance.

## Structure
```
/Archive/[YEAR]/
  Compressed annual backup archives
```

## Managed by
dan
""",
    "Shared/Database/Maintenance_Reports": """# Maintenance Reports

Database maintenance logs and health reports.

## Contents
- Weekly maintenance run reports
- Index optimisation logs
- Disk usage reports
- Schema change records

## Managed by
dan
""",
    "Shared/Dolibarr_EDM/Invoices": """# Invoices (EDM)

Invoices auto-synced from Dolibarr Electronic Document Management module.

## Structure
```
/Invoices/[YEAR-MM]/
  Dolibarr-generated invoice PDFs
```

## Sync
Nightly at 2 AM via Dolibarr REST API webhook (managed by ema).

## Managed by
ema — EDM agent. dai reads for analytics.
""",
    "Shared/Dolibarr_EDM/Contracts": """# Contracts (EDM)

Contracts auto-synced from Dolibarr EDM.

## Contents
- Client contracts (from cas in Dolibarr)
- Vendor contracts (from sun in Dolibarr)

## Sync
Nightly auto-sync. ema monitors for sync errors via /Sync_Log/.

## Managed by
ema
""",
    "Shared/Dolibarr_EDM/Purchase_Orders": """# Purchase Orders (EDM)

Purchase orders auto-synced from Dolibarr EDM.

## Structure
```
/Purchase_Orders/
  /Active/     — Open POs
  /Completed/  — Fulfilled POs
```

## Managed by
ema
""",
    "Shared/Dolibarr_EDM/Sync_Log": """# Sync Log

Dolibarr EDM sync status and error logs.

## Contents
- Nightly sync run logs
- Error reports (failed uploads, missing files)
- Manual sync records

## Purpose
ema monitors this folder for sync failures and re-runs as needed.

## Managed by
ema
""",
    "Shared/Archive/Projects": """# Projects Archive

Closed engagement and project archives.

## Structure
```
/Projects/[Project_Name]_[YYYY]/
  All documents from the completed engagement
```

## Process
ema moves completed project folders here from /Shared/Sales/ or other active folders.

## Retention
7 years minimum — legal hold capability.

## Managed by
ema — EDM and Archive agent. dai reads for historical analytics.
""",
    "Shared/Archive/Compliance": """# Compliance Archive

Legal holds and audit records.

## Contents
- Documents under legal hold
- Audit trail records
- Regulatory correspondence
- IRD audit support documents

## WARNING
Do not delete or modify any document in this folder without xc authorisation.

## Managed by
ema (writes) — xc authorises legal holds.
""",
    "Shared/Archive/Historical": """# Historical Archive

Pre-2024 records migrated to Nextcloud.

## Contents
- Documents predating the current Nextcloud system
- Migrated records from previous storage

## Retention
7 years from document date.

## Managed by
ema
""",
    "Shared/Templates/Finance": """# Finance Templates

Starter templates for financial documents.

## Templates
- `Invoice.ods` / `Invoice.odt` — NZ GST invoice (15%)
- `Expense report.ods` — Employee expense claims
- `Timesheet.ods` — Staff timesheet
- `Annual Budget Template.md` — Budget planning framework
- `Quote Template.md` — Client quote / price proposal
- `Purchase Order Template.md` — PO for vendor orders
- `Bank Reconciliation Template.md` — Monthly reconciliation

## Usage
Copy template to working location — do not edit originals here.

## Maintained by
ema — all agents read.
""",
    "Shared/Templates/Sales": """# Sales Templates

Starter templates for sales and client engagement documents.

## Templates
- `Pitch deck.odp` — Presentation framework
- `Business model canvas.ods` / `.odg` — BMC worksheet
- `Letter.odt` / `Report.odt` — Generic business letter / report
- `Consulting Proposal Template.md` — ICS consulting proposals
- `Statement of Work Template.md` — Project scope and deliverables
- `Client Service Agreement Template.md` — NZ-law service agreement
- `Client Onboarding Checklist.md` — New client setup checklist
- `Consulting Engagement Letter.md` — Engagement confirmation letter
- `RWA Tokenization Term Sheet.md` — ITE tokenization deal terms

## Usage
Copy template to working location. cas customises for each client.

## Maintained by
ema — all agents read.
""",
    "Shared/Templates/HR": """# HR Templates

Starter templates for human resources documents.

## Templates
- `Resume.odt` — CV / resume template
- `Onboarding.odp` — New employee onboarding presentation
- `Certificate.odt` — Certificate of completion / attendance
- `Org chart.odg` — Organisational chart
- `Syllabus.odt` — Training course syllabus
- `Employment Contract Template.md` — NZ ERA 2000 compliant
- `Offer Letter Template.md` — Job offer letter
- `NDA Template.md` — Non-disclosure agreement
- `Performance Review Template.md` — Annual / mid-year review
- `Leave Request Form.md` — Holidays Act 2003 compliant

## NZ law
All employment templates aligned to Employment Relations Act 2000 and Holidays Act 2003.

## Maintained by
ema — all agents read.
""",
    "Shared/Templates/General": """# General Templates

Starter templates for cross-functional use.

## Templates
- `Meeting notes.md` / `Meeting Minutes Template.md`
- `Product plan.md` — Product/feature planning
- `Checklist.ods` — Generic checklist
- `Flowchart.odg` / `.whiteboard`
- `Brainstorming.whiteboard`
- `Kanban board.whiteboard`
- `Timeline.whiteboard`
- `Mind map.whiteboard` / `Mindmap.odg`
- `SOP Template.md` — Standard operating procedure
- `Project Status Report Template.md`
- `Risk Register Template.md`
- `EA Deliverable Template.md` — TOGAF-aligned architecture deliverable
- `Technical Specification Template.md` — ITE hardware/software spec

## Maintained by
ema — all agents read.
""",
}

def put_file(path, content):
    """Upload a file via WebDAV PUT."""
    url = f"{WEBDAV}/{path}"
    resp = requests.put(
        url,
        data=content.encode("utf-8"),
        headers={"Content-Type": "text/markdown; charset=utf-8"},
        auth=AUTH,
    )
    return resp.status_code

def main():
    ok = 0
    fail = 0
    for subfolder, content in READMES.items():
        path = f"{subfolder}/README.md"
        code = put_file(path, content)
        status = "OK" if code in (200, 201, 204) else f"FAIL {code}"
        print(f"  {status}  /{path}")
        if code in (200, 201, 204):
            ok += 1
        else:
            fail += 1
        time.sleep(0.3)

    print(f"\nDone: {ok} uploaded, {fail} failed")

if __name__ == "__main__":
    main()
