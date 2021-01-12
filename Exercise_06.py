'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
print("Menu Options : ")
print()
print("\t1) - Create a new Account")
print("\t2) - View all your tasks")
print("\t3) - View your completed tasks")
print("\t4) - View Incomplete tasks")
print("\t5) - Create a new task")
print("\t6) - Update an existing task")
print("\t7) - Delete task")

options = {'Create Account': '1', 'View Tasks': '2','View Completed': '3','View Incomplete': '4', 'Create task': '5',
           'Update task': '6','Delete Task': '7'}

action = input("Choose activity you would like to perform: ")
if action == options['Create Account'] and action.isdigit():
    import requests

    fname = input("Enter your first name: ")
    sname = input("Enter your last name: ")
    email = input("Enter your email address: ")

    url = "http://demo.codingnomads.co:8080/tasks_api/users"
    body = {
        "first_name": fname,
        "last_name": sname,
        "email": email

    }
    response = requests.post(url, json=body)
    status = response.status_code

    if status == 200:
        print("Account created. Your request was successful")
        response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
        userdata = response.json()
        x = len(userdata["data"])
        userid = userdata["data"][int(x)-1]["id"]
        print("Your user identification is ", userid)

        """
        taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
        task_details  = { "userId": userid,
                          "name": mytask,
                          "description": "mytaskdescription",
                          "completed": false }
        response = requests.post(taskurlurl, json=task_details)"""
elif action == options['Create task'] and action.isdigit():
    import requests
    myId = eval(input("Enter your user identification: "))
    mytask = input("What task would you love to perform: ")
    desc = input("Describe your task: ")
    task_details = {"userId": myId,
                    "name": mytask,
                    "description": desc,
                    }
    taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    response = requests.post(taskurl, json=task_details)
    status = response.status_code
    if status == 200:
        print("New task creation successful")

elif action == options['View Tasks'] and action.isdigit():
    # Check if user exists in user database
    import requests
    url = "http://demo.codingnomads.co:8080/tasks_api/users"
    response = requests.get(url)
    users = response.json()
    email_list = []
    for i in range(len(users["data"])):
        email_list.append(users["data"][i]["email"])
    user_email = input("Enter your email: ")
    if user_email not in email_list:
        print("Cannot complete your request. You have to first create a user account.")
    else:
        # Pulls out all tasks by a user by using their user identification
        import requests
        from pprint import pprint
        myId = eval(input("Enter your user identification: "))
        taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
        response = requests.get(taskurl)
        tasks = response.json()
        j = 0
        print("Your total number of tasks listed are: ")
        for i in range(0,len(tasks["data"])):
            if myId == tasks["data"][i]["userId"]:
                mytask = tasks["data"][i]["name"]
                j = j + 1
                print(j,"\t",mytask)
elif action == options['View Completed'] and action.isdigit():
    # Pull up completed tasks by user by user id
    import requests

    myId = eval(input("Enter your user identification: "))
    taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    response = requests.get(taskurl)
    tasks = response.json()
    j = 0
    print("Your total number of completed tasks are: ")
    for i in range(0, len(tasks["data"])):
        if myId == tasks["data"][i]["userId"] and tasks["data"][i]["completed"] == 1:
            mytask = tasks["data"][i]["name"]
            j = j + 1
            print(j, "\t", mytask)

elif action == options['Update task'] and action.isdigit():
    # Update a task
    print("Choose your action: 1 to Update Task Info OR 2 to Update status to True if completed")
    action = input("Action: ")
    if action == "1":
        import requests
        url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
        taskid = eval(input("Enter task identification: "))
        taskname = input("New Task name: ")
        taskdesc = input("New Task description: ")
        body = {
            "id": taskid,
            "name": taskname,
            "description": taskdesc
        }
        response = requests.put(url, json=body)
        print(response.status_code)

        
        
    elif action == "2":
        import requests
        myId = eval(input("Enter your user identification: "))
        taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
        response = requests.get(taskurl)
        tasks = response.json()
        for i in range(0, len(tasks["data"])):
            if myId == tasks["data"][i]["userId"] and tasks["data"][i]["completed"] == 0:
                taskid = tasks["data"][i]["id"]
                mytask = tasks["data"][i]["name"]
                taskdesc = tasks["data"][i]["description"]
        url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
        body = {
        "id": taskid,
        "userId": myId,
        "name": mytask,
        "description": taskdesc,
        "completed": 1
        }
        response = requests.put(url, json=body)
        print(response.status_code)
        print("Task status updated")
        

elif action == options['Delete task'] and action.isdigit():
    import requests
    from pprint import pprint
    url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    me = "/51"
    response = requests.delete(url+me)
    print(response.status_code)
    response = requests.get(url)
    print("Done")
    pprint(f"{response.content}")












