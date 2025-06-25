import os

from dotenv import load_dotenv
from openreview.api import OpenReviewClient

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

for note in camera_ready_notes:
    print(note)

print(len(camera_ready_notes), "camera-ready notes")
