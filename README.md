## Overview

This API allows users to perform CRUD operations on a "person" resource. Users can create, read, update, and delete persons by their unique IDs.

## Setup Instructions
Clone the repository:

`git clone https://github.com/kihuni/Hng-Task-2.git`

Navigate to the project directory:

`cd project_name`

Install the required packages:

`pip install -r requirements.txt`

Start the application:

`python run.py`

Your API is now running at http://127.0.0.1:5000/.

## API Endpoints
1. Add a New Person

Endpoint: /api
Method: POST

Payload:
```
}
  "name": "John Doe"
}

```
2. Fetch Details of a Person

Endpoint: /api/<user_id>
Method: GET

3. Modify Details of an Existing Person

Endpoint: /api/<user_id>
Method: PUT

Payload:

```
{
  "name": "Jane Doe"
}

```
4. Remove a Person

Endpoint: /api/<user_id>
Method: DELETE

## Testing the API Endpoints

For testing, we'll use the tool [Postman](https://www.postman.com/downloads/).

1. Add a New Person

Open Postman.
Set the method to POST.
Enter the URL: http://127.0.0.1:5000/api.
Under the Body tab, choose raw and JSON (application/json).
Add the following payload:

```
{
  "name": "John Doe"
}

```
Click Send. You will receive a confirmation message.

```
{
    "message": "New person added!"
}
```

2. Fetch Details of a Person

In Postman, set the method to GET.
Enter the URL: http://127.0.0.1:5000/api/1 (assuming the person's ID is 1).
Click Send. You should receive the details of the person.
```
{
    "name": "John Doe"
}
```
3. Modify Details of an Existing Person

In Postman, set the method to PUT.
Enter the URL: http://127.0.0.1:5000/api/1 (assuming the person's ID is 1).
Under the Body tab, choose raw and JSON (application/json).
Add the following payload:
```
{
  "name": "Jane Doe"
}
```
Click Send. You should receive a confirmation message.
```
{
    "message": "person added!"
}
```

4. Remove a Person

In Postman, set the method to DELETE.
Enter the URL: http://127.0.0.1:5000/api/1 (assuming the person's ID is 1).

Click Send. You should receive a confirmation message.

```
{
    "message": "person deleted!"
}
```

[live link](https://personapi-qey7.onrender.com/)