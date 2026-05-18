import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://cloud.nzrtnetwork.com/nextcloud"
XC_USER = "xc"
XC_TOKEN = "fgqWc-bsYFS-FWfk4-zPrbc-arY5Q"

# Permissions: 1=read, 2=update, 4=create, 8=delete
READ_WRITE = 15
READ_ONLY = 1

# Share matrix from Users & Groups.md
# (path, shareWith, permissions)
SHARES = [
    ("/Shared/Marketing",    "pam", READ_WRITE),
    ("/Shared/Marketing",    "dai", READ_ONLY),
    ("/Shared/Sales",        "cas", READ_WRITE),
    ("/Shared/Sales",        "dai", READ_ONLY),
    ("/Shared/Procurement",  "sun", READ_WRITE),
    ("/Shared/Procurement",  "dai", READ_ONLY),
    ("/Shared/Finance",      "fin", READ_WRITE),
    ("/Shared/Finance",      "dai", READ_ONLY),
    ("/Shared/HR",           "han", READ_WRITE),
    ("/Shared/Analytics",    "dai", READ_WRITE),
    ("/Shared/Database",     "dan", READ_WRITE),
    ("/Shared/Dolibarr_EDM", "ema", READ_WRITE),
    ("/Shared/Dolibarr_EDM", "dai", READ_ONLY),
    ("/Shared/Archive",      "ema", READ_WRITE),
    ("/Shared/Archive",      "dai", READ_ONLY),
]


def create_share(path, share_with, permissions):
    url = f"{BASE_URL}/ocs/v2.php/apps/files_sharing/api/v1/shares"
    resp = requests.post(
        url,
        auth=HTTPBasicAuth(XC_USER, XC_TOKEN),
        headers={"OCS-APIREQUEST": "true"},
        data={
            "path": path,
            "shareType": 0,  # 0 = user share
            "shareWith": share_with,
            "permissions": permissions,
        },
    )
    ok = "<statuscode>100</statuscode>" in resp.text or resp.status_code == 200
    perm_label = "R+W" if permissions == READ_WRITE else "R"
    print(f"  {path:30s} -> {share_with:6s} [{perm_label}]: {'OK' if ok else 'FAIL'} ({resp.status_code})")
    if not ok:
        print(f"    {resp.text[:300]}")
    return ok


if __name__ == "__main__":
    if not XC_TOKEN:
        print("ERROR: set XC_TOKEN first")
        raise SystemExit(1)

    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else None

    for path, share_with, perms in SHARES:
        if target and share_with != target:
            continue
        create_share(path, share_with, perms)
