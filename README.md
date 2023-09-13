## Overview

This API allows users to perform CRUD operations on a "person" resource. Users can create, read, update, and delete persons by their unique IDs.

## Setup Instructions
Clone the repository:

`git clone https://github.com/kihuni/Hng-Task-2.git`

Navigate to the project directory:

`cd project_name`

Environment Setup:

It's recommended to use a virtual environment to keep the project dependencies isolated.
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

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
    "message": "Person updated!"
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

## Error Responses
In case of errors, the API will return appropriate status codes and messages. For instance:

  400 Bad Request: Sent if the data format is incorrect or validation fails.
  404 Not Found: If the resource (person) is not found.
  405 Method Not Allowed: If the wrong HTTP method is used.
  
## Assumptions and Limitations
Database: This model uses SQLite, a lightweight database suitable for development and testing. For production scenarios, consider using a more scalable database.

Validation: The current implementation primarily validates the name for uniqueness. More comprehensive validation can be added based on requirements.

Security: This is a basic model without authentication or authorization layers. Before moving to a production environment, consider adding security mechanisms.

Conclusion
This documentation provides a basic overview and usage instructions for the Persons API. Always ensure that you're using the correct HTTP methods and providing data in the required format to ensure smooth operations.

[live link](https://personapi-qey7.onrender.com/)
