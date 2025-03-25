import requests

def get_user_agents():
  response = requests.get("https://fake-useragent.herokuapp.com/browsers/0.1.11")
  print(response.json())
