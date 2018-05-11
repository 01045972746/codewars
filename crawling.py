import requests, json
from bs4 import BeautifulSoup

def main():
  url = "https://cloudfunctions.apigw.ntruss.com/common/real/v1/OJJzvNR9aHuI/Crawling-action1?blocking=true&result=true"
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic NjNkY2MyNWEtNjZiMy1kOTRmLTI4OGMtZWE3NmYzMTY5ZGQwOlhsZmZRamdBbm5KTWZ4bVQ5T1pWWjlUWk1mand0WURnQndZVTFpRG5BUUJ2Y0xZUkFKTlJCckJZRDNQdms0UFk=',
    'x-ncp-apigw-api-key': 'DlondC5OhEsyR09smF3N5DI95ARv4rXna0vV1wk9'
  }
  res = requests.post(url, headers=headers)
  print(res.json())
  

main()