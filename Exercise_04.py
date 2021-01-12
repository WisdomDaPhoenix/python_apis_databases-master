'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
body = {
    "id": 72,
    "userId": 230,
    "name": "Book Writing",
    "description": "Write two chapters",
    "completed": 1
}
response = requests.put(url, json=body)
print(response.status_code)



"""
import requests
from pprint import pprint
url = "http://demo.codingnomads.co:8080/tasks_api/users"
body = {
    "id": 220,
    "first_name": "Wizzy",
    "last_name": "Tron",
    "email": "wisdomene@yahoo.com"

}
response = requests.put(url, json=body)

print(response.status_code)

response = requests.get(url)
pprint(f"{response.content}") """