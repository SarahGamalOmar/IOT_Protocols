import requests

# GET
response = requests.get('http://localhost:5000/temperature')
print("GET:", response.json())

# POST
new_temp = {"temperature": 30}
response = requests.post('http://localhost:5000/temperature', 
json=new_temp)
print("POST:", response.json())

# GET again to verify
response = requests.get('http://localhost:5000/temperature')
print("GET after update:", response.json())

