# Python FAST API

A brief description of what the project does.

## Overview

- This project is a CRUD API for managing items.
- It uses FastAPI and SQLAlchemy for the web framework and database, respectively.
- Users can perform CRUD operations on items using the provided endpoints.

## Installation

To run this code, ensure you have the following dependencies installed:

- Python (version 3.11)
- Database (e.g., MySQL db)

Follow these steps to set up the development environment:

1. Clone the repository: `git clone https://github.com/Shaijujin/fast_api.git`
2. Install the required Python packages: `pip install -r requirements/requirements.txt`
3. Run the application cmd: `uvicorn main:app`

## Folder Structure
```
FAST_API_EXAMPLE/
├── function_api/
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── route.py
│   ├── schemas.py
│   └── services.py
├── main.py
├── requirements.txt
└── README.md
```
- function_api/: This folder contains the main modules and components of your API.

  - crud.py: Defines the CRUD operations for the items in your API.
  - database.py: Sets up the database connection and provides the session maker.
  - models.py: Defines the SQLAlchemy model for the Item entity.
  - route.py: Defines the API routes and their corresponding handlers.
  - schemas.py: Contains the Pydantic models for the request and response schemas.
  - services.py: Contains the business logic and interacts with the CRUD operations.
- main.py: This is the entry point of your application, where the FastAPI app is created, routes are added, and the server is started.

- requirements.txt: This file lists the dependencies required for your project. You can use the pip freeze > requirements.txt command to generate this file, which includes all the installed packages and their versions.

- README.md: This is the file where you document your project, its usage, installation instructions, and any other relevant information. You can provide an overview of the project, describe the API endpoints and their functionalities, explain how to set up and run the project, and include any other relevant details.

## API Endpoints
- GET `/items/{item_id}`: Retrieve an item by ID.
- POST `/items`: Create a new item.
- PUT `/items/{item_id`}: Update an existing item.
- DELETE `/items/{item_id}`: Delete an item.


# Example
### Request:

```
POST /items
Content-Type: application/json

{
  "name": "Item 1",
  "description": "This is the first item"
}
```
### Response:
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Item 1",
  "description": "This is the first item"
}
```