import requests
import json
import argparse
import base64


def create_jira_ticket(jira_user, jira_key, jira_ticket_id, payload_data):
    print(jira_ticket_id)
    print(payload_data)
    print("Updating JIRA ticket")
    
    url = f"https://safe-security.atlassian.net/rest/api/3/issue/{jira_ticket_id}/transitions"

    payload = json.dumps(payload_data)
    print(payload)
    
    auth_str = f"{jira_user}:{jira_key}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        'Authorization': f'Basic {b64_auth_str}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print("JIRA ticket status updtaed successfully")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--jira_key", help="Git branch of safe-deployments repo", default="")
    parser.add_argument("--jira_user", help="Git branch of safe-deployments repo", default="")
    parser.add_argument("--jira_ticket_id", help="Git branch of safe-deployments repo", default="")
    parser.add_argument("--status", help="Git branch of safe-deployments repo", default="")
    args = parser.parse_args()
    jira_key = args.jira_key
    jira_user = args.jira_user
    jira_ticket_id = args.jira_ticket_id
    status = args.status

    status_mapping = {
        "complete": "9028",
        "fail": "9152",
        "mark_as_canceled": "9172",
        "back_to_awaiting_implementation": "9222",
        "implement": "9212",
        "override": "9252"
    }

    project_id = {
        "id": "10212" #"name" = "SISD" 
    }
    
    transition_id = status_mapping[status]
    if transition_id == "9152":
        {
            "transition": {
                "id": 9152
            },
            "fields": {
                "resolution": {
                "name": "Incomplete"
                }
            },
            "update": {
                "comment": [
                {
                    "add": {
                    "body": {
                        "type": "doc",
                        "version": 1,
                        "content": [
                        {
                            "type": "paragraph",
                            "content": [
                            {
                                "type": "text",
                                "text": "Deployment has been failed. Please check the logs and try again."
                            }
                            ]
                        }
                        ]
                    }
                    }
                }
                ]
            }
            }
    else:
        payload_data = {
            "transition": {
                "id": transition_id
                }
            }

    create_jira_ticket(jira_user, jira_key, jira_ticket_id, payload_data)


if __name__ == "__main__":
    main()
