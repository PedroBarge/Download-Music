import json
import re
import sys

import requests

from Enum_Support_Sources import SupportSource


def extract_playlist_embed(url, source):
    headers = {"User-Agent": "Mozilla/5.0"}
    cookies = {}

    if source == SupportSource.YOUTUBE:
        cookies["CONSENT"] = "YES+cb"

    resp = requests.get(url, headers=headers, cookies=cookies)
    resp.raise_for_status()

    match = None

    if source == SupportSource.SPOTIFY:
        match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
    elif source == SupportSource.APPLE_MUSIC:
        match = re.search(r'<script type="application/json" id="serialized-server-data">(.*?)</script>', resp.text)
    elif source == SupportSource.YOUTUBE:
        match = re.search(r'var\s+ytInitialData\s*=\s*(\{.*?\});\s*</script>', resp.text, re.DOTALL)

    if not match:
        print("Error extracting playlist data.")
        print(resp.text)
        sys.exit(1)

    data = json.loads(match.group(1))

    return data
