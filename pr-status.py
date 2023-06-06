import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import sys
import concurrent.futures
import os
from datetime import datetime, timedelta

# GitHub API base URL
BASE_URL = "https://api.github.com"

# Get Repository owner and name

if len(sys.argv) < 2:
    print("Usage: python prsummary.py ownername repositoryname")
    sys.exit(1)

# Retrieve the arguments
owner = sys.argv[1]
repo = sys.argv[2]

# Authentication token (optional)
token=os.getenv("gittoken")

# Calculate the date 7 days ago
seven_days_ago = datetime.now() - timedelta(days=7)
seven_days_ago_str = seven_days_ago.strftime("%Y-%m-%dT%H:%M:%SZ")

# Headers for the GitHub API request
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Token {token}" if token else None
}
gitrepo=f"{BASE_URL}/repos/{owner}/{repo}"
# Retrieve all pull requests for the specified state
def get_all_pull_requests(state):
    url = f"{BASE_URL}/repos/{owner}/{repo}/pulls?state={state}"
    pull_requests = []

    while url:
        response = requests.get(url, headers=headers)
        response_json = response.json()
        pull_requests.extend(response_json)

        if "Link" in response.headers:
            links = parse_link_header(response.headers["Link"])
            url = links.get("next")
        else:
            url = None
        # Filter pull requests created in the last 7 days
        pull_requests = [pr for pr in pull_requests if pr["created_at"] >= seven_days_ago_str]
    return pull_requests

# Parse the Link header to extract URL for next page
def parse_link_header(header):
    links = {}

    parts = header.split(", ")
    for part in parts:
        section = part.split("; ")
        url = section[0][1:-1]
        rel = section[1][5:-1]
        links[rel] = url

    return links

# Retrieve all pull requests for each state
opened_pull_requests = get_all_pull_requests("open")
closed_pull_requests = get_all_pull_requests("closed")
draft_pull_requests = get_all_pull_requests("draft")
open_count=len(opened_pull_requests)
closed_count=len(closed_pull_requests)
draft_count=len(draft_pull_requests)

# Create the HTML content for the email body
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Pull Request Summary</title>
</head>
<body>
    <h1 style="background-color:LightGray;">Pull Request Summary for Github Repo {(gitrepo)} </h1>
    <p>Open Pull Requests: {(open_count)}</p>
    <p>Closed Pull Requests: {(closed_count)}</p>
    <p>Draft Pull Requests: {(draft_count)}</p>
    <h1 style="background-color:MediumSeaGreen;">Additional Details of the Pull Requests </h1>
    <h2>Opened Pull Requests:</h2>
    <ul>
        {''.join(f"<li>#{pr['number']}: {pr['title']}</li>" for pr in opened_pull_requests)}
    </ul>

    <h2>Closed Pull Requests:</h2>
    <ul>
        {''.join(f"<li>#{pr['number']}: {pr['title']}</li>" for pr in closed_pull_requests)}
    </ul>

    <h2>Draft Pull Requests:</h2>
    <ul>
        {''.join(f"<li>#{pr['number']}: {pr['title']}</li>" for pr in draft_pull_requests)}
    </ul>
</body>
</html>
"""

#

#html_part = MIMEText(html, "html")

# Attach the HTML content to the email message

#message.attach(html_part)

# Send the email
#with smtplib.SMTP(smtp_server, smtp_port) as server:
#    server.starttls()
#    server.login(sender_email, sender_password)
#   server.sendmail(sender_email, receiver_email, message.as_string())

#print("Email sent successfully!")

# Save the HTML content to a file
filename = "pull_request_summary.html"
with open(filename, "w") as file:
    file.write(html)

print(f"Pull request summary saved to {filename}!")
