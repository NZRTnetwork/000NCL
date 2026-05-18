import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://cloud.nzrtnetwork.com/nextcloud"

AGENTS = {
    "cas": "59QudZ6quSB&waXs8E$B^r87@&Sox#b7",
    "pam": "$*Zr!6rxh5Fzi4JTX&^EyDsC8m9tns#2",
    "sun": "9k%lDC6rfTFJa#I9Wn%8&4vlcxFmdR^*",
    "fin": "RahP7@cR2U0iRBO**5pli%8Zx$joAS22",
    "han": "MR&1BHA*dqXX^3suF4bOwXnc91dVN^2g",
    "ema": "xEpd^96$fQHhAbE9#6cS6ImVfKXqV%!%",
    "dai": "oMq%9JuFXkU&3^I*tVGFl*dh&0yj*Z7h",
    "dan": "!6KhCM48B0xs0%ZPT^@m$&Kf!Vk2Y0%N",
}

DEFAULT_ITEMS = [
    "Documents",
    "Photos",
    "Talk",
    "Templates",
    "Nextcloud.png",
    "Nextcloud Manual.pdf",
    "Nextcloud intro.mp4",
]


def delete_item(userid, password, item):
    url = f"{BASE_URL}/remote.php/dav/files/{userid}/{item}"
    resp = requests.delete(url, auth=HTTPBasicAuth(userid, password))
    if resp.status_code == 204:
        print(f"  deleted : {item}")
    elif resp.status_code == 404:
        print(f"  missing : {item}")
    else:
        print(f"  FAIL {resp.status_code}: {item}")


def cleanup_agent(userid):
    password = AGENTS[userid]
    print(f"\n=== {userid} ===")
    for item in DEFAULT_ITEMS:
        delete_item(userid, password, item)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cleanup_agent(sys.argv[1])
    else:
        for agent in AGENTS:
            cleanup_agent(agent)
