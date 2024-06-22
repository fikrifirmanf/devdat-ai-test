# DevDat.AI API Documentation

This repository contains the API for DevDat.AI, a platform for plant disease detection.

## API Endpoints

### 1. Users

**Endpoint:** `/users`

**Methods:**

- **POST:** Create a new user.
  - **Request Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
  - **Response:**
    ```json
    {
        "data": {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaWtyaTJAZmlrcmlmaXJtYW5mLmNvbSJ9.n13ZIjpLi5h_Xr7eisz68Mz3ntjQyu3aQORn4C7A1CQ",
            "email": "fikri2@fikrifirmanf.com",
            "id": 3,
            "name": "user@example.com",
            "token_type": "bearer"
        },
        "message": "User created successfully"
    }   
    ```

- **GET:** Get all users.
  - **Response:**
    ```json
    {
        "data": [
            {
                "email": "fikri@devdat.ai",
                "id": 1,
                "name": "Test User"
            },
            {
                "email": "fikri@fikrifirmanf.com",
                "id": 2,
                "name": "Fkri Firman F"
            },
            {
                "email": "fikri2@fikrifirmanf.com",
                "id": 3,
                "name": "Fkri Firman F2"
            }
        ],
        "message": "Users retrieved successfully"
    }
    ```

- **GET:** Get a specific user by ID.
  - **URL:** `/users/{user_id}`
  - **Response:**
    ```json
    {
        "data": {
            "email": "fikri@devdat.ai",
            "id": 1,
            "name": "Test User"
        },
        "message": "User retrieved successfully"
    }
    ```

- **PUT:** Update a specific user by ID.
  - **URL:** `/users/{user_id}`
  - **Request Body:**
    ```json
    {"name": "Joss"}
    ```

  - **Response:**
    ```json
    {
        "data": {
            "email": "fikri@devdat.ai",
            "id": 1,
            "name": "Test User"
        },
        "message": "User retrieved successfully"
    }
    ```

### 2. Predictions

**Endpoint:** `/predictions`

**Methods:**

- **POST:** Create a new prediction.
  - **Request Body:**
    ```json
    {
      "image": (Image file)
    }
    ```
  - **Response:**
    ```json
    {
      "data": {
        "message": "Prediction created successfully",
        "prediction_id": 123
      }
    }
    ```

### 3. Interactions

**Endpoint:** `/interactions`

**Methods:**

- **GET:** Get all interactions.
  - **Response:**
    ```json
    {
      "data": [
        {
          "id": 123,
          "user_id": 123,
          "prediction_id": 123,
          "timestamp": "2023-12-12T12:34:56.789Z",
          "data": "Image uploaded: image.jpg"
        },
        ...
      ]
    }
    ```

- **GET:** Get interactions for a specific user.
  - **URL:** `/interactions/{user_id}`
  - **Response:**
    ```json
    {
      "data": [
        {
          "id": 123,
          "prediction_id": 123,
          "timestamp": "2023-12-12T12:34:56.789Z",
          "data": "Image uploaded: image.jpg"
        },
        ...
      ]
    }
    ```

- **GET:** Get interactions for a specific prediction.
  - **URL:** `/interactions/prediction/{prediction_id}`
  - **Response:**
    ```json
    {
      "data": [
        {
          "id": 123,
          "user_id": 123,
          "timestamp": "2023-12-12T12:34:56.789Z",
          "data": "Image uploaded: image.jpg"
        },
        ...
      ]
    }
    ```

## Authentication

The API uses JWT (JSON Web Token) for authentication. To access protected endpoints, you need to obtain an access token by logging in.

**Endpoint:** `/auth/login`

**Method:** POST

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "password123"
}
