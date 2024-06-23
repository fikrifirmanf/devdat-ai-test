# AI-Based Image Prediction API

This is an AI-powered API built with Flask that allows users to upload images and get predictions from a pre-trained machine learning model. 

## Features

* User registration and login with email/password authentication.
* Image upload and prediction using a pre-trained model.
* Storage of prediction history for each user. 
* API documentation (to be added).
* Containerized deployment using Docker. 

## Installation & Running

### 1. Requirements

* **Python 3.9 or higher:**  Download and install Python from [https://www.python.org/](https://www.python.org/).
* **Virtual Environment (recommended):** Create a virtual environment to manage dependencies for this project:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Activate the virtual environment 
   ```
* **Dependencies:** Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### 2. Configuration

* **Database:** 
   * **Create Database:** Create an empty SQLite database file named `devdat.db` in the project root directory.

### 3. Running Locally Without Docker

1. **Create Tables:** 
   ```bash
   flask shell 
   >>> from utils.db import Base, engine
   >>> Base.metadata.create_all(bind=engine) 
   >>> exit()
   ```

2. **Run the Flask app:**
   ```bash
   flask run
   ```
   * The API will be available at `http://127.0.0.1:5000/`

### 4. Running with Docker

1. **Build Docker Images:**
   ```bash
   docker-compose build
   ```

2. **Start Docker Containers:**
   ```bash
   docker-compose up -d
   ```

3. **Access the API:**
   * The API will be available at `http://devdat-api.fikrifirmanf.com/` (replace with your actual domain).
   * The API documentation using postman please check the file in email that I sent

