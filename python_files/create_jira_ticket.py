import requests
import json
import argparse
import base64
import os

def create_jira_ticket(jira_user, jira_key, payload_data):
    print("Creating JIRA ticket")

    url = "https://safe-security.atlassian.net/rest/api/3/issue"
    payload = json.dumps(payload_data)
    auth_str = f"{jira_user}:{jira_key}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        'Authorization': f'Basic {b64_auth_str}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        response_json = response.json()  # Extract JSON content from the response
        print(json.dumps(response_json))  # Print the JSON content

        # Store the response in a file
        with open('/tmp/try.json', 'w') as file:
            json.dump(response_json, file, indent=4)
        print("Response stored in /tmp/try.json")

    except requests.exceptions.RequestException as e:
        print(f"Failed to create JIRA ticket: {e}")
        print(response.text)

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--jira_key", help="JIRA API token", required=True)
    # parser.add_argument("--jira_user", help="JIRA username", required=True)
    # args = parser.parse_args()
    jira_key = "ATATT3xFfGF0t0fuP5NiOz8ZQrmfUSplX9XeY6AzjDHqBl-fOl3Et-EYrWSRNbI3VFrD-jhqgEBW7q5ZtDiZQJyRdZGnkHUmGtSnMgsh2M_CtFTx7Dy8YswhYSqo7u_tjpQvj23HzVU63fDWYogCtswL-TDnhFZ0eotGigRT3foEr0CwgtGgsJE=E80AA246"
    
    jira_user = "deepak.m@safe.security"
    payload_file = "/tmp/jira_ticket_payload.json"

    # Check if the file exists
    if not os.path.isfile(payload_file):
        print(f"Payload file {payload_file} does not exist.")
        return

    # Read the JSON payload from the file
    try:
        with open(payload_file, 'r') as file:
            payload_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON from {payload_file}: {e}")
        return

    create_jira_ticket(jira_user, jira_key, payload_data)

if __name__ == "__main__":
    main()