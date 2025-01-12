import requests
import json
import argparse
import base64

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
        # with open('/tmp/try.json', 'w') as file:
        #     json.dump(response_json, file, indent=4)
        # print("Response stored in /tmp/try.json")

    except requests.exceptions.RequestException as e:
        print(f"Failed to create JIRA ticket: {e}")
        print(response.text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload_data",help="payload of the service", required=True)
    parser.add_argument("--jira_key", help="JIRA API token", required=True)
    parser.add_argument("--jira_user", help="JIRA username", required=True)
    args = parser.parse_args()
    payload_data = args.payload_data
    jira_key = args.jira_key
    jira_user = args.jira_user
    print(payload_data)
    
    create_jira_ticket(jira_user, jira_key, payload_data)

if __name__ == "__main__":
    main()
