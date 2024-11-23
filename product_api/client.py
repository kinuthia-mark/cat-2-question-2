import requests

BASE_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    payload = {
        'name': name,
        'description': description,
        'price': price,
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Product added successfully:", response.json())
    else:
        print("Error:", response.json())

def list_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Error:", response.json())

# Example usage
if __name__ == '__main__':
    add_product("Smartphone", "A high-end smartphone", 799.99)
    list_products()
