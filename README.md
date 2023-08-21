# Python REST API with Flask and SQLAlchemy

This is a simple RESTful API implementation using Flask and SQLAlchemy that provides CRUD operations for a `User` model.

<img width="1016" alt="Screenshot 2023-08-21 at 1 30 19 AM" src="https://github.com/oskccy/python_rest_api/assets/118501673/ee983800-f69d-445f-96b5-2c192812113e">

## Table of Contents

- [Setup and Installation](#setup-and-installation)
- [Database Configuration](#database-configuration)
- [Routes](#routes)
  - [Root Route](#root-route)
  - [Fetch All Users](#fetch-all-users)
  - [Fetch User by ID](#fetch-user-by-id)
  - [Add a New User](#add-a-new-user)
  - [Delete User by ID](#delete-user-by-id)
- [Data Fetcher](#data-fetcher)
- [Contributions](#contributions)

## Setup and Installation

1. Ensure you have Flask and Flask-SQLAlchemy installed. If not, install them via pip:
    ```bash
    pip install Flask Flask-SQLAlchemy

2. Clone this repository and navigate to its directory.

3. Run the main server file to start the application.

## Database Configuration

The database is configured using SQLAlchemy ORM with SQLite. The current configuration uses a local SQLite database named `data.db`. The User table/model consists of fields like `id`, `first_name`, `last_name`, `phone_number`, `social_insurance`, and `credit_card`.

_Note: The credit card and social insurance numbers should be encrypted before being stored in the database._

## Routes

### Root Route

- **URL**: `/`
- **Method**: `GET`
- **Description**: A simple route to check if the server is running.
- **Response**: Returns a string "Hello World!".

### Fetch All Users

- **URL**: `/users`
- **Method**: `GET`
- **Description**: Retrieves all the users from the database.
- **Response**: Returns a list of users in JSON format.

### Fetch User by ID

- **URL**: `/users/<id>`
- **Method**: `GET`
- **Description**: Retrieves a single user based on its ID.
- **Response**: Returns the user details in JSON format.

### Add a New User

- **URL**: `/users`
- **Method**: `POST`
- **Data Params**: JSON object with user details.
<img width="628" alt="screenshot" src="https://github.com/oskccy/python_rest_api/assets/118501673/3db23ad6-78d3-4418-961d-e98a769217e6">

  ```json
  {
    "first_name": "Devin",
    "last_name": "Dubb",
    "phone_number": "1234567890",
    "social_insurance": "XYZ123",
    "credit_card": "1234-5678-9012-3456"
  }
  ```
- **Description**: Adds a new user to the database.
- **Response**: Returns the added user details in JSON format.

### Delete User by ID

- **URL**: `/users/<id>`
- **Method**: `DELETE`
- **Description**: Deletes a user based on its ID.
- **Response**: Confirmation of deletion with the deleted user's ID.
<img width="1040" alt="Screenshot 2023-08-21 at 1 35 55 AM" src="https://github.com/oskccy/python_rest_api/assets/118501673/44537023-9ace-47f3-9972-adee84cc9744">

## Data Fetcher

There's an additional script that fetches random user data from an external API. This script uses the `requests` module to make a GET request and fetch data for 2 random users.

To run this script, ensure you have the `requests` module installed:
  ```bash
  pip install requests
  ```
Run the data fetcher script to get random user data.

## Contributions

While this is primarily a solo project, feedback, suggestions, or pull requests are always appreciated. If you find any bugs or see room for improvement, please feel free to fork the repository, make your changes, and initiate a pull request.

Steps to Contribute:

1. **Fork the Repository**: If you're interested in making changes, start by forking this repository.

2. **Clone and Create a New Branch**: Clone your fork to your local machine and create a new branch for your suggestions or fixes.

3. **Commit Changes**: Make your modifications and commit your changes. Aim to have clear and descriptive commit messages.

4. **Pull Request**: Create a pull request to this repository. Provide a brief overview of the changes you've made.
