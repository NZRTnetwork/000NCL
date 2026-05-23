#!/usr/bin/env python3
"""
ncl-pubshare.py — Create or retrieve a Nextcloud public share link for a vault file/folder.

Usage:
    python ncl-pubshare.py "NZRT NETWORK/Work_Packages/Business Units/ITE/HOME.md"
    python ncl-pubshare.py "API/HOME.md" --label "API Gateway HOME"
    python ncl-pubshare.py "API" --label "API folder"

Outputs the public share URL, e.g.:
    https://cloud.nzrtnetwork.com/nextcloud/index.php/s/AbCdEfGhIjKl (label)
"""

import sys
import argparse
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://cloud.nzrtnetwork.com/nextcloud"
XC_USER = "xc"
XC_TOKEN = "fgqWc-bsYFS-FWfk4-zPrbc-arY5Q"
VAULT_PREFIX = "/Documents/Obsidian/"

AUTH = HTTPBasicAuth(XC_USER, XC_TOKEN)
HEADERS = {"OCS-APIREQUEST": "true", "Accept": "application/json"}


def to_ncl_path(vault_relative: str) -> str:
    """Convert vault-relative path to Nextcloud user-root path."""
    # Normalise slashes
    clean = vault_relative.replace("\\", "/").strip("/")
    return VAULT_PREFIX + clean


def get_existing_share(ncl_path: str) -> str | None:
    """Return existing public share URL for path, or None."""
    resp = requests.get(
        f"{BASE_URL}/ocs/v2.php/apps/files_sharing/api/v1/shares",
        auth=AUTH,
        headers=HEADERS,
        params={"path": ncl_path, "reshares": "false"},
    )
    if resp.status_code != 200:
        return None
    try:
        data = resp.json()
        shares = data.get("ocs", {}).get("data", [])
        for share in shares:
            if share.get("share_type") == 3:
                url = share.get("url") or f"{BASE_URL}/index.php/s/{share['token']}"
                return url
    except Exception:
        pass
    return None


def create_public_share(ncl_path: str) -> str | None:
    """Create a public read-only share link. Return URL or None on failure."""
    resp = requests.post(
        f"{BASE_URL}/ocs/v2.php/apps/files_sharing/api/v1/shares",
        auth=AUTH,
        headers=HEADERS,
        data={
            "path": ncl_path,
            "shareType": 3,       # 3 = public link
            "permissions": 1,     # 1 = read-only
        },
    )
    try:
        data = resp.json()
        meta = data.get("ocs", {}).get("meta", {})
        statuscode = meta.get("statuscode")

        if statuscode in (100, 200):  # OCS v1=100, v2=200
            share = data["ocs"]["data"]
            return share.get("url") or f"{BASE_URL}/index.php/s/{share['token']}"

        if statuscode in (403, 400):
            # May already exist — try fetching existing
            message = meta.get("message", "")
            if "already" in message.lower() or "shared" in message.lower():
                return get_existing_share(ncl_path)

        print(f"ERROR: OCS returned statuscode={statuscode} message={meta.get('message')}", file=sys.stderr)
        print(f"  HTTP status: {resp.status_code}", file=sys.stderr)
    except Exception as e:
        print(f"ERROR parsing response: {e}", file=sys.stderr)
        print(f"  Raw: {resp.text[:500]}", file=sys.stderr)
    return None


def main():
    parser = argparse.ArgumentParser(description="Create Nextcloud public share link for a vault path.")
    parser.add_argument("path", help="Vault-relative path (file or folder)")
    parser.add_argument("--label", default="", help="Optional label for display in output")
    parser.add_argument("--no-create", action="store_true", help="Only check existing shares, don't create")
    args = parser.parse_args()

    ncl_path = to_ncl_path(args.path)

    # Check for existing share first (idempotent)
    url = get_existing_share(ncl_path)

    if url:
        label_str = f" ({args.label})" if args.label else ""
        print(f"{url}{label_str}")
        return

    if args.no_create:
        print("No existing share found.", file=sys.stderr)
        sys.exit(1)

    # Create new share
    url = create_public_share(ncl_path)
    if url:
        label_str = f" ({args.label})" if args.label else ""
        print(f"{url}{label_str}")
    else:
        print("Failed to create share.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
