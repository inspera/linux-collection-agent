import base64
import json
import pickle
import socket
import subprocess
import sys
from email.mime.text import MIMEText
from pathlib import Path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
HOST = socket.gethostname()
script_dir = Path(__file__).parent.parent.absolute()
config_path = script_dir / "config.json"
if not config_path.exists():
    print("Please make a file 'config.json' as described in README.")
    sys.exit(1)

with open(config_path) as f:
    config = json.load(f)


def authenticate():
    creds = None
    pickle_path = script_dir / "token.pickle"
    if pickle_path.exists():
        with open(pickle_path, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                script_dir / "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(pickle_path, "wb") as token:
            pickle.dump(creds, token)

    service = build("gmail", "v1", credentials=creds)
    return service


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_dump():
    service = authenticate()
    message = create_message(
        sender="me",
        to="security@inspera.com",
        subject=f"Linux collection report for {config['name']} ({HOST})",
        message_text=subprocess.check_output(
            [f"{script_dir / 'system-state-dump.sh'}"]
        ).decode(),
    )
    service.users().messages().send(userId="me", body=message).execute()


if __name__ == "__main__":
    send_dump()
