import os
import requests

from dotenv import load_dotenv
from openreview.api import OpenReviewClient
from openreview.tools import get_profiles

load_dotenv()

client = OpenReviewClient(
    baseurl="https://api2.openreview.net",
    username=os.getenv("OPENREVIEW_USER"),
    password=os.getenv("OPENREVIEW_PASSWORD"),
)

invs = client.get_invitations(
    prefix="appliedtopology.org/ATMCS/2025/Conference"
)
for inv in invs:
    print(inv.id)

note = client.get_note(id="BV4pBJywx2")

venue_id = "appliedtopology.org/ATMCS/2025/Conference"
venue_group = client.get_group(venue_id)

client.impersonate(venue_id)

profiles = get_profiles(
    client, ["~António_Leitão2", "~Buddha_Nath_Sharma1", "~Dylan_Peek1"]
)

for profile in profiles:
    user_email = profile.get_preferred_email()
    print(user_email)

raise "heck"

# notes = client.get_all_notes(invitation=f"{venue_id}/-/Submission")
notes = client.get_all_notes(content={"venueid": venue_id})

camera_ready_notes = []

print(len(notes))

for note in notes:
    camera_ready_invitation = (
        f"{venue_id}/Submission{note.number}/-/Camera-Ready"
    )
    if camera_ready_invitation in note.invitations:
        camera_ready_notes.append(note)
    else:
        print("Missing:", note.number)

print(len(camera_ready_notes), "camera-ready notes")

for note in camera_ready_notes:
    rel_url = note.content["pdf"]["value"]
    url = f"https://openreview.net{rel_url}"

    response = requests.get(url, cookies=client.session.cookies)
    if response.status_code == 200:
        filename = f"/tmp/{note.number:02d}.pdf"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Saved: {filename}")
    else:
        print(f"Failed: {url} ({response.status_code})")
