import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", help="Path to the JSON file", default="")
    parser.add_argument("--summary", help="Type of the service", default="")
    args = parser.parse_args()
    tag = args.tag
    summary_input = args.summary
    
    if tag.startswith("noti"):
        summary = "notification deployment on tag " + tag
    else:
        summary = "service deployment"

    
  #   return {
  # "fields": {
  #   "project": {
  #     "id": "10113"
  #   },
  #   "assignee": {
  #     "id": "712020:89e17fe4-7635-42c7-bdb7-11ab1f4c7dc8"
  #   },
  #   "summary": summary,
  #   "issuetype": {
  #     "id": "10148"
  #   },
  #   "customfield_10166": {
  #     "type": "doc",
  #     "version": 1,
  #     "content": [
  #       {
  #         "type": "paragraph",
  #         "content": [
  #           {
  #             "type": "text",
  #             "text": "Deploy following stacks using the job - Independent Services:- https://jenkins.lucideus.tech/job/CloudOps/job/Production/job/(Safe One) Independent Service Upgrade/"
  #           }
  #         ]
  #       }
  #     ]
  #   },
  #   "customfield_10167": {
  #     "type": "doc",
  #     "version": 1,
#       "content": [
#         {
#           "type": "paragraph",
#           "content": [
#             {
#               "type": "text",
#               "text": "Use the same job for rolling back to the previous version, JOB ----> https://jenkins.lucideus.tech/job/CloudOps/job/Production/job/(Safe One) Independent Service Upgrade/"
#             }
#           ]
#         }
#       ]
#     }
#   }
# }
    payload_data = {
  "fields": {
    "project": {
      "id": "10113"
    },
    "assignee": {
      "id": "712020:89e17fe4-7635-42c7-bdb7-11ab1f4c7dc8"
    },
    "summary": summary,
    "issuetype": {
      "id": "10148"
    },
    "customfield_10166": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Deploy following stacks using the job - Independent Services:- https://jenkins.lucideus.tech/job/CloudOps/job/Production/job/(Safe One) Independent Service Upgrade/"
            }
          ]
        }
      ]
    },
    "customfield_10167": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Use the same job for rolling back to the previous version, JOB ----> https://jenkins.lucideus.tech/job/CloudOps/job/Production/job/(Safe One) Independent Service Upgrade/"
            }
          ]
        }
      ]
    }
  }
}
    print(payload_data)


if __name__ == "__main__":
    main()
