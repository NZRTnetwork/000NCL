"""
Write README.md files to local Shared folder dirs that are missing them.
Skips CREDS. Writes directly to filesystem — NC desktop client syncs up.
"""

import os

BASE = r"C:\Users\Natha\Nextcloud2\Shared"

READMES = {
    "": """# /Shared/

Root of all NZRT Network shared folders. Each subfolder is owned by xc and shared
with the relevant AI agent(s) via Nextcloud.

| Folder | Manager | Access |
|--------|---------|--------|
| Marketing | pam | pam R+W, dai R |
| Sales | cas | cas R+W, dai R |
| Procurement | sun | sun R+W, dai R |
| Finance | fin | fin R+W, dai R |
| HR | han | han R+W — E2EE, xc+han only |
| Analytics | dai | dai R+W |
| Database | dan | dan R+W |
| Dolibarr_EDM | ema | ema R+W, dai R |
| Archive | ema | ema R+W, dai R |
| CREDS | xc | xc only — never share |
| Templates | ema | ema R+W, all agents R |

Shares set 2026-04-25 via OCS API. See xc Access Master List for share IDs.
""",
    "Marketing": """# /Shared/Marketing

Marketing materials, campaign assets, and brand resources for NZRT Network (ICS and ITE).

**Manager:** pam — Products and Marketing agent
**Analytics read:** dai

## Subfolders
- `Brand/` — Logos, colour palette, brand guidelines
- `Campaigns/` — Campaign briefs and assets by campaign
- `Social/` — Social media content and schedules
- `Product_Sheets/` — ICS and ITE one-pagers
- `Blog_Drafts/` — Drafts before WordPress upload
- `Media/` — Images, videos, graphics
""",
    "Sales": """# /Shared/Sales

Client documents, proposals, contracts, and CRM exports.

**Manager:** cas — Customer and Sales agent
**Analytics read:** dai

## Subfolders
- `Clients/` — One folder per client (Contracts, Proposals, Quotes, Correspondence)
- `Active_Deals/` — Current pipeline documents
- `CRM_Export/` — Dolibarr CRM CSV/JSON exports
- `Onboarding/` — New client onboarding docs

**Retention:** 3 years
""",
    "Procurement": """# /Shared/Procurement

Purchase orders, vendor contracts, delivery records, and RFQs.

**Manager:** sun — Supplier and Purchase agent
**Analytics read:** dai

## Subfolders
- `Purchase_Orders/` — POs by year (PO-[YEAR]-[NNN].pdf)
- `Vendors/` — Vendor contracts and pricing
- `RFQs/` — Requests for quotation
- `Invoices_Received/` — Vendor invoices (input to Dolibarr AP)
- `Delivery_Notes/` — Goods received dockets

**Retention:** 3 years
""",
    "Finance": """# /Shared/Finance

Financial documents — invoices, bank statements, budgets, and reports.

**Manager:** fin — Finance and Accounting agent
**Analytics read:** dai
**E2EE:** Bank_Statements subfolder — end-to-end encrypted

## Subfolders
- `Invoices/` — Sales invoices by year-month
- `Bank_Statements/` — E2EE — bank statements by year
- `Reconciliations/` — Monthly reconciliation workbooks
- `Budget/` — Annual budgets and quarterly forecasts
- `Reports/` — Monthly and annual financial reports
- `Tax_GST/` — GST returns and IRD correspondence
- `Purchase_Orders/` — POs received from sun for payment

**Retention:** 7 years (NZ IRD requirement)
""",
    "HR": """# /Shared/HR

Employee records, payroll, and HR documents.

**CONFIDENTIAL — End-to-end encrypted. xc and han access only.**

**Manager:** han — Human Resources agent

## Subfolders
- `Employees/` — Active and departed employee records
- `Payroll/` — Payroll files by year (E2EE)
- `Onboarding/` — Checklists and forms
- `Policies/` — HR policy documents
- `Leave_Records/` — Leave requests and approvals
- `Performance_Reviews/` — Annual and mid-year reviews

**NZ law:** Employment Relations Act 2000, Holidays Act 2003, Privacy Act 2020
**Retention:** 7 years
""",
    "Database": """# /Shared/Database

Database backups, system logs, and maintenance records.

**Manager:** dan — DBA agent

## Subfolders
- `Backups/Daily/` — Daily MySQL dumps (30-day retention)
- `Backups/Weekly/` — Weekly full backups (1-year retention)
- `Logs/System_Logs/` — General system activity
- `Logs/Error_Logs/` — Errors and warnings
- `Archive/` — Backups beyond active retention
- `Maintenance_Reports/` — Weekly maintenance run reports
""",
    "Dolibarr_EDM": """# /Shared/Dolibarr_EDM

Dolibarr Electronic Document Management auto-sync folder.

**Manager:** ema — EDM agent
**Analytics read:** dai

Documents are auto-synced nightly at 2 AM from Dolibarr via REST API webhook.

## Subfolders
- `Invoices/` — Invoices by year-month
- `Contracts/` — Client and vendor contracts
- `Purchase_Orders/Active/` — Open POs
- `Purchase_Orders/Completed/` — Fulfilled POs
- `Sync_Log/` — Nightly sync status and error logs

**Retention:** 7 years (mirrors Dolibarr EDM retention)
""",
    "Archive": """# /Shared/Archive

Long-term retention of completed project documents and older records.

**Manager:** ema — EDM and Archive agent
**Analytics read:** dai

ema moves completed items here from active folders.

## Subfolders
- `[YEAR]/` — Archived documents by year
- `Projects/` — Closed engagement archives
- `Compliance/` — Legal holds and audit records
- `Historical/` — Pre-2024 records

**Retention:** 7 years minimum — legal hold capability
""",
    "Templates": """# /Shared/Templates

Document templates for all NZRT business functions.

**Manager:** ema (R+W) — all agents read

## Subfolders
- `Finance/` — Invoice, budget, reconciliation, expense templates
- `Sales/` — Proposals, SOW, client agreement, onboarding templates
- `HR/` — Employment contracts, offer letters, review templates (NZ ERA 2000)
- `General/` — Meeting minutes, SOP, project status, risk register templates

**Usage:** Copy template to working location. Do not edit originals here.
""",
    "Analytics/Reports/Annual": """# Annual Reports

Annual analytics summaries for NZRT Network.

**File naming:** `[YYYY]_Annual_Analytics.md`

## Contents
- Year-end KPI summary
- Cross-system performance review
- Trend analysis vs prior year

**Managed by:** dai
""",
    "Analytics/Reports/Monthly": """# Monthly Reports

Monthly analytics reports.

**File naming:** `[YYYY-MM]_Monthly_Report.md`

**Managed by:** dai
""",
    "Analytics/Reports/Weekly": """# Weekly Reports

Weekly analytics summaries.

**File naming:** `[YYYY-WNN]_Weekly_Summary.md`

**Managed by:** dai
""",
    "Analytics/Exports/Dolibarr_Exports": """# Dolibarr Exports

Raw CSV and JSON exports pulled from Dolibarr by dai.

## Contents
- Product and stock exports
- CRM and sales pipeline exports
- Financial summary exports
- HR headcount exports

**Retention:** Rolling 1 year

**Managed by:** dai
""",
    "Analytics/Exports/Cross_System": """# Cross-System Exports

Combined data exports drawing from multiple NZRT systems.

## Contents
- Dolibarr + WordPress combined reports
- Financial + sales combined exports
- Custom cross-system datasets for reporting

**Managed by:** dai
""",
    "Archive/2026": """# Archive 2026

Documents archived in 2026.

**Process:** ema moves completed or expired documents here from active folders.

**Retention:** 7 years minimum from archive date.

**Managed by:** ema
""",
    "Database/Backups/Daily": """# Daily Backups

Automated daily MySQL database dumps.

**Schedule:** 2 AM NZST daily (dan automated job)
**File naming:** `nzrt_[YYYY-MM-DD].sql.gz`
**Retention:** 30 days — older files purged automatically

**Managed by:** dan
""",
    "Database/Backups/Weekly": """# Weekly Backups

Weekly full database backups.

**Schedule:** Sunday 3 AM NZST
**File naming:** `nzrt_weekly_[YYYY-WNN].sql.gz`
**Retention:** 1 year

**Managed by:** dan
""",
    "Database/Logs/System_Logs": """# System Logs

General system activity logs from NZRT infrastructure.

**Retention:** 90 days rolling

**Managed by:** dan
""",
    "Database/Logs/Error_Logs": """# Error Logs

Error and warning logs from NZRT services.

**Retention:** 90 days rolling

**Managed by:** dan — review weekly for issues.
""",
    "Dolibarr_EDM/Purchase_Orders/Active": """# Active Purchase Orders (EDM)

Open purchase orders currently being processed — auto-synced from Dolibarr EDM.

**Sync:** Nightly 2 AM via ema webhook

**Managed by:** ema
""",
    "Dolibarr_EDM/Purchase_Orders/Completed": """# Completed Purchase Orders (EDM)

Fulfilled purchase orders — auto-synced from Dolibarr EDM.

**Managed by:** ema
""",
    "Finance/Reports/Annual": """# Annual Financial Reports

Year-end financial reports exported by fin from Dolibarr.

**File naming:** `[YYYY]_Annual_Report.pdf`

**Retention:** 7 years (NZ IRD requirement)

**Managed by:** fin
""",
    "Finance/Reports/Monthly": """# Monthly Financial Reports

Monthly P&L, cash flow, and summary reports.

**File naming:** `[YYYY-MM]_[Report_Type].pdf`

**Managed by:** fin
""",
    "HR/Employees/Active": """# Active Employees

**CONFIDENTIAL — E2EE. xc and han access only.**

Records for current employees.

## Structure
```
/[Employee_Name]/
  Employment_Contract.pdf
  Offer_Letter.pdf
  ID_Copy.pdf
  Review_[YYYY].pdf
```

**NZ law:** Employment Relations Act 2000

**Managed by:** han
""",
    "HR/Employees/Departed": """# Departed Employees

**CONFIDENTIAL — E2EE. xc and han access only.**

Records for former employees — retained per NZ employment law.

**Retention:** 6 years after employment end (Employment Relations Act 2000)

**Managed by:** han
""",
    "HR/Onboarding/Checklists": """# Onboarding Checklists

New employee onboarding checklists.

**Template:** /Shared/Templates/HR/Client Onboarding Checklist.md

**Managed by:** han
""",
    "HR/Onboarding/Forms": """# Onboarding Forms

New employee forms — tax code declaration, KiwiSaver enrolment, equipment issue.

## Key forms
- IR330 Tax code declaration (IRD)
- KiwiSaver enrolment form (KS2)
- Equipment issue record

**Managed by:** han
""",
}

def main():
    ok = 0
    skip = 0
    for rel_path, content in READMES.items():
        readme_path = os.path.join(BASE, rel_path, "README.md") if rel_path else os.path.join(BASE, "README.md")
        if os.path.exists(readme_path):
            print(f"  SKIP (exists)  {readme_path}")
            skip += 1
            continue
        os.makedirs(os.path.dirname(readme_path), exist_ok=True)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  OK  {readme_path}")
        ok += 1

    print(f"\nDone: {ok} written, {skip} skipped (already exist)")

if __name__ == "__main__":
    main()
