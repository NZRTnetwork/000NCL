import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://cloud.nzrtnetwork.com/nextcloud"

# Each agent authenticates as itself (xc uses web login / 2FA — no Basic Auth)
AGENTS = {
    "cas": {
        "password": "59QudZ6quSB&waXs8E$B^r87@&Sox#b7",
        "fields": {
            "displayname": "CAS — Customer and Sales",
            "headline": "AI Agent — Customer and Sales",
            "biography": "Manages customer relationships, sales pipeline, and CRM data for NZRT Network.",
            "email": "sales@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — Customer and Sales",
        },
    },
    "pam": {
        "password": "$*Zr!6rxh5Fzi4JTX&^EyDsC8m9tns#2",
        "fields": {
            "displayname": "PAM — Products and Marketing",
            "headline": "AI Agent — Products and Marketing",
            "biography": "Handles product catalogue, marketing campaigns, and website content for NZRT Network.",
            "email": "products@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — Products and Marketing",
        },
    },
    "sun": {
        "password": "9k%lDC6rfTFJa#I9Wn%8&4vlcxFmdR^*",
        "fields": {
            "displayname": "SUN — Supplier and Procurement",
            "headline": "AI Agent — Supplier and Procurement",
            "biography": "Manages supplier relationships, purchase orders, and procurement for NZRT Network.",
            "email": "procurement@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — Supplier and Procurement",
        },
    },
    "fin": {
        "password": "RahP7@cR2U0iRBO**5pli%8Zx$joAS22",
        "fields": {
            "displayname": "FIN — Finance and Accounting",
            "headline": "AI Agent — Finance and Accounting",
            "biography": "Handles invoicing, payments, financial reporting, and accounts for NZRT Network.",
            "email": "finance@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — Finance and Accounting",
        },
    },
    "han": {
        "password": "MR&1BHA*dqXX^3suF4bOwXnc91dVN^2g",
        "fields": {
            "displayname": "HAN — Human Resources",
            "headline": "AI Agent — Human Resources",
            "biography": "Manages HR records, onboarding, and staff administration for NZRT Network.",
            "email": "hr@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — Human Resources",
        },
    },
    "ema": {
        "password": "xEpd^96$fQHhAbE9#6cS6ImVfKXqV%!%",
        "fields": {
            "displayname": "EMA — EDM and Communications",
            "headline": "AI Agent — EDM and Communications",
            "biography": "Manages email campaigns and external digital communications for NZRT Network.",
            "email": "edm@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — EDM and Communications",
        },
    },
    "dai": {
        "password": "oMq%9JuFXkU&3^I*tVGFl*dh&0yj*Z7h",
        "fields": {
            "displayname": "DAI — Data and Analytics",
            "headline": "AI Agent — Data and Analytics",
            "biography": "Handles reporting, analytics, and data pipeline management for NZRT Network.",
            "email": "data@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — Data and Analytics",
        },
    },
    "dan": {
        "password": "!6KhCM48B0xs0%ZPT^@m$&Kf!Vk2Y0%N",
        "fields": {
            "displayname": "DAN — Database Admin",
            "headline": "AI Agent — Database Administration",
            "biography": "Manages database operations and data integrity for NZRT Network.",
            "email": "dba@nzrtnetwork.com",
            "organisation": "NZRT Network",
            "role": "AI Agent — Database Administration",
        },
    },
}


def set_user_field(userid, password, key, value):
    url = f"{BASE_URL}/ocs/v2.php/cloud/users/{userid}"
    resp = requests.put(
        url,
        auth=HTTPBasicAuth(userid, password),
        headers={"OCS-APIREQUEST": "true"},
        data={"key": key, "value": value},
    )
    ok = "<statuscode>200</statuscode>" in resp.text or resp.status_code == 200
    print(f"  {key:15s}: {'OK' if ok else 'FAIL'} ({resp.status_code})")
    if not ok:
        print(f"    {resp.text[:300]}")
    return ok


def populate_agent(userid):
    agent = AGENTS[userid]
    print(f"\n=== {userid} ===")
    for key, value in agent["fields"].items():
        set_user_field(userid, agent["password"], key, value)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # single agent: python populate_nc_profiles.py cas
        populate_agent(sys.argv[1])
    else:
        # all agents
        for agent in AGENTS:
            populate_agent(agent)
