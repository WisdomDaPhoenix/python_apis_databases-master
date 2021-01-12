'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url)
users = response.json()
email_list = []
for i in range(len(users["data"])):
    email_list.append(users["data"][i]["email"])
pprint(email_list)
