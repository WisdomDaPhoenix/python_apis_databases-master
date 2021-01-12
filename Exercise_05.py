'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"
me = "/235"
response = requests.delete(url+me)

print(response.status_code)

response = requests.get(url)
print("done")
#pprint(f"{response.content}")