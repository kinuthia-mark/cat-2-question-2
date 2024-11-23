
# E-Commerce Flask API

This is a simple REST API built with **Flask** for managing products. The API allows you to **create** new products and **retrieve** a list of all products in the database. It supports **JSON** format for data exchange.



## Features

- **Create a Product**: Allows you to add a product with details like `name`, `description`, and `price`.
- **Retrieve All Products**: Allows you to fetch a list of all products stored in the database.


## Setup Instructions

### Prerequisites

Before running this project, make sure you have the following installed:

- **Python **: Ensure that Python is installed on your system. You can check by running:
  python --version


- **cURL**: A command-line tool for testing HTTP requests (optional).



### Steps to Set Up the Project

1. **Clone the repository**:
   Clone the project to your local machine using the following command:
   
   git clone <repository-url>
   cd ecommerce
   

2. **Create and activate a virtual environment**:
   It's recommended to use a virtual environment to manage dependencies:
  
   python -m venv venv  # Create virtual environment
   venv\Scripts\activate  # On Windows
   

3. **Install dependencies**:
   Once the virtual environment is active, install Flask:

   pip install flask


4. **Run the Flask application**:
   To start the Flask server, run:
   
   python app.py
   
   The server will be running at `http://127.0.0.1:5000/`.


## API Endpoints

### 1. POST `/products`

- **Description**: Adds a new product to the database.
- **Request body (JSON)**:

  {
    "name": "Laptop",
    "description": "A powerful laptop",
    "price": 1500
  }
  ```
- **Response (success)**:
  {
    "id": 1,
    "name": "Laptop",
    "description": "A powerful laptop",
    "price": 1500
  }
  ```
- **Response status**: `201 Created`

### 2. GET `/products`

- **Description**: Retrieves a list of all products.
- **Response**:
 
  [
    {
      "id": 1,
      "name": "Laptop",
      "description": "A powerful laptop",
      "price": 1500
    },
    {
      "id": 2,
      "name": "Smartphone",
      "description": "A high-end smartphone",
      "price": 799.99
    }
  ]

- **Response status**: `200 OK`



## Error Handling

The API returns appropriate status codes and messages for error cases:

- **400 Bad Request**: Returned when the request is invalid (e.g., missing required fields).
- **404 Not Found**: Returned when a requested resource doesn't exist.
- **500 Internal Server Error**: Returned when there's a server-side issue.



## Testing the API

### Using cURL:

To test the API from the terminal, use the following `cURL` commands:

#### **POST `/products`**
This command creates a new product:

curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d "{\"name\": \"Laptop\", \"description\": \"A powerful laptop\", \"price\": 1500}"


#### **GET `/products`**
This command retrieves all products:

curl http://127.0.0.1:5000/products
