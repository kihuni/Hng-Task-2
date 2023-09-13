# Persons Data API Documentation

## Overview

The Persons data API allows for basic CRUD operations on a "person" resource.

## Setup Instructions

First, Fork and clone the project

### Environment Setup:

It's recommended to use a virtual environment to keep the project dependencies isolated.

```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

```
### Install Dependencies:
Install required packages from requirements.txt.

`pip install -r requirements.txt`

### Run the Application:

Start the Flask development server.

`python run.py`

## Endpoints

1. Add a New Person

    URL: /api
    Method: POST
    Request Payload: JSON object containing a person's name.

### Sample Request
```
json

{
    "name": "John Doe"
}

```

### Sample Response
```
json

{
    "message": "New person added!"
}
```


2. Fetch Details of a Person

    URL: /api/<user_id>
    Method: GET

### Sample Request
`GET /api/1`

### Sample Response

```
json

{
    "name": "John Doe"
}
```

3. Update Details of a Person

    URL: /api/<user_id>
    Method: PUT
    Request Payload: JSON object containing the updated name.

### Sample Request
`PUT /api/1`

```
json

{
    "name": "Johnathan Doe"
}

```

### Sample Response
```
json

{
    "message": "Person updated!"
}

```

4. Remove a Person
    URL: /api/<user_id>
    Method: DELETE

### Sample Request
`DELETE /api/1`

### Sample Response
```
json

{
    "message": "Person deleted!"
}
```

## Error Responses
In case of errors, the API will return appropriate status codes and messages. For instance:

    400 Bad Request: Sent if the data format is incorrect or validation fails.
    404 Not Found: If the resource (person) is not found.
    405 Method Not Allowed: If the wrong HTTP method is used.

## Assumptions and Limitations

- Database: This model uses SQLite a lightweight database suitable for development and testing. For production scenarios, consider using a more scalable database of your choice.

- Validation: The current implementation primarily validates the name for uniqueness. More comprehensive validation can be added based on requirements.

- Security: This is a basic model without authentication or authorization layers. Before moving to a production environment, consider adding security mechanisms.

## Conclusion

This documentation provides a basic overview and usage instructions for the Persons data API. Always ensure that you're using the correct HTTP methods and providing data in the required format to ensure smooth operations.

[live link](https://personapi-qey7.onrender.com/)
