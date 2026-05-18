import requests
from requests.auth import HTTPBasicAuth
import re

BASE_URL = "https://cloud.nzrtnetwork.com/nextcloud"
XC_USER = "xc"
XC_TOKEN = "fgqWc-bsYFS-FWfk4-zPrbc-arY5Q"

AGENTS = {
    "cas": {
        "fn":    "CAS — Customer & Sales",
        "title": "AI Agent — Customer & Sales",
        "org":   "NZRT Network",
        "note":  "Manages customer relationships, sales pipeline, and CRM data for NZRT Network.",
        "email": "sales@nzrtnetwork.com",
    },
    "pam": {
        "fn":    "PAM — Products & Marketing",
        "title": "AI Agent — Products & Marketing",
        "org":   "NZRT Network",
        "note":  "Handles product catalogue, marketing campaigns, and website content for NZRT Network.",
        "email": "products@nzrtnetwork.com",
    },
    "sun": {
        "fn":    "SUN — Supplier & Procurement",
        "title": "AI Agent — Supplier & Procurement",
        "org":   "NZRT Network",
        "note":  "Manages supplier relationships, purchase orders, and procurement for NZRT Network.",
        "email": "procurement@nzrtnetwork.com",
    },
    "fin": {
        "fn":    "FIN — Finance & Accounting",
        "title": "AI Agent — Finance & Accounting",
        "org":   "NZRT Network",
        "note":  "Handles invoicing, payments, financial reporting, and accounts for NZRT Network.",
        "email": "finance@nzrtnetwork.com",
    },
    "han": {
        "fn":    "HAN — Human Resources",
        "title": "AI Agent — Human Resources",
        "org":   "NZRT Network",
        "note":  "Manages HR records, onboarding, and staff administration for NZRT Network.",
        "email": "hr@nzrtnetwork.com",
    },
    "ema": {
        "fn":    "EMA — EDM & Communications",
        "title": "AI Agent — EDM & Communications",
        "org":   "NZRT Network",
        "note":  "Manages email campaigns and external digital communications for NZRT Network.",
        "email": "edm@nzrtnetwork.com",
    },
    "dai": {
        "fn":    "DAI — Data & Analytics",
        "title": "AI Agent — Data & Analytics",
        "org":   "NZRT Network",
        "note":  "Handles reporting, analytics, and data pipeline management for NZRT Network.",
        "email": "data@nzrtnetwork.com",
    },
    "dan": {
        "fn":    "DAN — Database Admin",
        "title": "AI Agent — Database Administration",
        "org":   "NZRT Network",
        "note":  "Manages database operations and data integrity for NZRT Network.",
        "email": "dba@nzrtnetwork.com",
    },
}

AUTH = HTTPBasicAuth(XC_USER, XC_TOKEN)
HEADERS = {"OCS-APIREQUEST": "true"}


def find_vcard_url(userid):
    """PROPFIND system address book to find agent's vCard URL."""
    url = f"{BASE_URL}/remote.php/dav/addressbooks/system/system/"
    resp = requests.request(
        "PROPFIND", url,
        auth=AUTH,
        headers={"Depth": "1", "Content-Type": "application/xml"},
        data="""<?xml version="1.0"?>
<d:propfind xmlns:d="DAV:">
  <d:prop><d:getetag/><d:displayname/></d:prop>
</d:propfind>""",
    )
    # find href containing userid
    pattern = rf'<d:href>([^<]*{userid}[^<]*\.vcf)</d:href>'
    match = re.search(pattern, resp.text, re.IGNORECASE)
    if match:
        return BASE_URL + match.group(1) if match.group(1).startswith("/") else match.group(1)
    return None


def get_vcard(url):
    resp = requests.get(url, auth=AUTH)
    if resp.status_code == 200:
        return resp.text
    return None


def set_vcard_field(vcard, field, value):
    """Replace or add a vCard field."""
    pattern = rf'^{field}[;:][^\r\n]*(\r?\n( [^\r\n]+)*)?'
    if re.search(pattern, vcard, re.MULTILINE | re.IGNORECASE):
        return re.sub(pattern, f"{field}:{value}", vcard, flags=re.MULTILINE | re.IGNORECASE)
    # insert before END:VCARD
    return vcard.replace("END:VCARD", f"{field}:{value}\r\nEND:VCARD")


def put_vcard(url, vcard):
    resp = requests.put(
        url, auth=AUTH,
        headers={"Content-Type": "text/vcard; charset=utf-8"},
        data=vcard.encode("utf-8"),
    )
    return resp.status_code in (200, 201, 204)


def populate_contact(userid):
    data = AGENTS[userid]
    print(f"\n=== {userid} ===")

    url = find_vcard_url(userid)
    if not url:
        print(f"  vCard URL: NOT FOUND in system address book")
        return

    print(f"  vCard URL: {url}")
    vcard = get_vcard(url)
    if not vcard:
        print(f"  GET vCard: FAIL")
        return

    for field, key in [("FN", "fn"), ("TITLE", "title"), ("ORG", "org"),
                       ("NOTE", "note"), ("EMAIL", "email")]:
        vcard = set_vcard_field(vcard, field, data[key])

    ok = put_vcard(url, vcard)
    print(f"  PUT vCard: {'OK' if ok else 'FAIL'}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        populate_contact(sys.argv[1])
    else:
        for agent in AGENTS:
            populate_contact(agent)
