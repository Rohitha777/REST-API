**Objective**:
To build a simple REST API using Flask that allows you to manage user data using CRUD operations:

Create

Read

Update

Delete

**Tools Used**:
Python – programming language

Flask – lightweight web framework to build APIs

VS Code – code editor

Thunder Client – API testing tool (built into VS Code)

 **Step-by-Step Process**:
1. **Environment Setup**
Installed Python and Flask

Set up a folder in VS Code

(Optional) Created a virtual environment using python -m venv venv

2. **Flask App Creation**
Created a file named app.py

Wrote a basic Flask app with routes:

/users – for listing or adding users

/users/<id> – for updating or deleting users

3. **Data Handling**
Used a Python list (users = []) to store users in memory

Each user is a dictionary with:

id

name

email

4.**Implemented API Endpoints**
GET /users – returns list of users

POST /users – adds a new user

PUT /users/<id> – updates an existing user

DELETE /users/<id> – deletes a user

5. **Testing with Thunder Client**
Used Thunder Client in VS Code to send API requests

Verified responses like user creation, update, and delete
