import requests

# Create
r = requests.post('http://localhost:5000/api', json={"name": "Stephen kihuni"})
print(r.text)

# Read
user_id = 1
r = requests.get(f'http://localhost:5000/api/{user_id}')
print(r.text)

# Update
r = requests.put(f'http://localhost:5000/api/{user_id}', json={"name": "Updated Name"})
print(r.text)

# Delete
r = requests.delete(f'http://localhost:5000/api/{user_id}')
print(r.text)
