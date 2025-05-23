from http.client import responses

import requests
import json


base_url = "https://gorest.co.in"

#berrear token
auth_token = "Bearer 12518dd4eef5ca2146f7a6eccf9804cbbad465c15f1be21a0eda845f78452d7e"

#get request
def get_request():
    get_url = base_url+"/public/v2/users"
    headers = {"Authorization" : auth_token}
    response = requests.get(get_url,headers=headers)
    assert response.status_code == 200
    data = response.json()
    json_sdr = json.dumps(data)
    print(json_sdr)

#get specific user
def get_user_details(userid):
    get_user_url = base_url + f'/public/v2/users/{userid}'
    headers = {"Authorization" : auth_token}
    response = requests.get(get_user_url,headers=headers)
    assert response.status_code == 200
    user_data = json.dumps(response.json(),indent=4)
    print()
    print(user_data)


#post request
def post_create_user():
    post_user_url = base_url + "/public/v2/users/"
    headers = {"authorization": auth_token}
    data = {
    "name": "dimple kapadia",
    "email": "dimpuuuu@gmail.com",
    "gender": "female",
    "status": "active"
}
    response = requests.post(post_user_url,headers=headers,json=data)
    print(response.status_code)
    assert response.status_code == 201
    json_data = response.json()
    user_data = json.dumps(json_data,indent=4)
    print(user_data)
    user_id = json_data["id"]
    print(user_id)
    assert "name" in json_data
    assert  json_data["name"] == "dimple kapadia"
    return user_id

#put request
def update_user_details(user_id):
    put_user_url = base_url + f"/public/v2/users/{user_id}"
    headers = {"authorization": auth_token}
    data = {
        "name": "dimmp",
        "email": "meenal_p@gmail.com",
        "gender": "female",
        "status": "inactive"
    }
    response = requests.put(url=put_user_url,headers=headers,json=data)
    assert response.status_code == 200
    data = response.json()
    user_updated = json.dumps(data,indent=4)
    print(user_updated)




#delete request
def delete_user_details(user_id):
    delete_url = base_url + f"/public/v2/users/{user_id}"
    headers = {"authorization" : auth_token}
    response = requests.delete(url=delete_url,headers=headers)
    print(response.status_code)
    assert response.status_code == 204
    print(response.status_code)



#call
# get_request()
# get_user_details(7896444)
# user_id = post_create_user()
# update_user_details(user_id)
delete_user_details(7896713)