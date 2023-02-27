import requests
import json

url = "https://reqres.in"

def getSingleUser():
    request_url = "/api/users/"
    u_id = 7
    
    response = requests.get(f"{url}{request_url}{u_id}")

    data = response.json()['data']
    support = response.json()['support']

    # print(response.status_code)
    # print(data, support)
    # print(response.text)
    # print(response.content)
    # print(response.url)
    # print(response._content_consumed)
    # print(response.cookies)
    # print(response.elapsed)
    # print(response.encoding)
    # print(response.headers)
    # print(response.apparent_encoding)
    # print(response.history)
    # print(response.links)
    # print(response.ok)


    print("ID is: ",data['id'],"\n","Name is: ",data['first_name'],data['last_name'],"\n","URL is:",support['url'])


# getSingleUser()


def getListUser():
    request_url = "/api/users"
    pageNo = {
        "page": 2
    }
    response = requests.get(f"{url}{request_url}",params=pageNo)
    print(response.status_code)

    data = response.json()['data']
    
    print(data)

# getListUser()

def usernotfound():
    u_id = 23


    response = requests.get(f"{url}{request_url}{u_id}")
    print(response.status_code)

# usernotfound()  

def createUser():
    request_url = "/api/users"
    user_data = open('data.json', 'r').read()

    response = requests.post(f"{url}{request_url}", data=json.loads(user_data))
    print(response.status_code)
    print(response.json())
# createUser() 

# update user using put method
def updateUserPut():
    request_url = "/api/users/"
    user_data = open('data.json', 'r').read()
    u_id = 2

    response = requests.put(f"{url}{request_url}+{u_id}", data=json.loads(user_data))
    print(response.status_code)
    print(response.json())
    
# updateUserPut()   

# update user using patch method
def updateUserPatch():
    request_url = "/api/users/"
    
    user_data = {
        'name': "aman",
    }
    u_id = 2

    response = requests.patch(f"{url}{request_url}+{u_id}", data=user_data)
    print(response.status_code)
    print(response.json())
    # print(response.text)
    # print(response.content)

    
# updateUserPatch()

def deleteUser():
    request_url = "/api/users/"
    u_id = 2

    res = requests.delete(f"{url}{request_url}{u_id}")
    print(res.status_code)

# deleteUser()

def listOfUsers():
    request_url = "/api/unknown"

    res = requests.get(f"{url}{request_url}")

    print(res.status_code)
    print(res.json())
    # print(res.json()['data'][0])

# listOfUsers()

def resisterUser():
    request_url = "/api/register" 
    user_data ={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }

    res = requests.post(f"{url}{request_url}", data=user_data)
    print(res.status_code)
    # print(res.json())
    # print(res.json()['token'])

# resisterUser()

def loginUser():
    request_url = "/api/login"
    user_data ={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    res = requests.post(f"{url}{request_url}", data=user_data)
    print(res.status_code)
    print(res.json()['token'])

# loginUser() 

def delayResponse():
    request_url = "/api/users"
    delay = {"delay": 5}

    res = requests.get(f"{url}{request_url}", params=delay)
    print(res.status_code)

delayResponse()


def delayResponseTimeout():
    request_url = "/api/users"
    delay = {"delay": 5}

    res = requests.get(f"{url}{request_url}", params=delay , timeout =3)
    print(res.status_code)

# delayResponseTimeout()
