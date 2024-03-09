# Online Shop API

This API provides a way to manage an online shop's inventory, specifically food and technological products. It allows clients to create, retrieve, update, and delete product information from a database.

## Features

- List all products in the inventory
- Add new products to the inventory
- Retrieve details of a specific product
- Update details of a product
- Delete a product from the inventory

## Installation

To set up the Online Shop API on your local machine, follow these steps:

1. Clone the repository to your local machine.
2. Ensure that you have Python 3.x installed.
3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python api.py
    ```

The API will be accessible on `http://localhost:5000`.

## Usage

Here is a brief overview of how to use the API endpoints:

### Food Products

- `GET /food_product/`: Retrieves all food products.
- `POST /food_product/`: Adds a new food product.
- `GET /food_product/{id}`: Retrieves a food product by ID.
- `PUT /food_product/{id}`: Updates a food product by ID.
- `DELETE /food_product/{id}`: Deletes a food product by ID.

### Tech Products

- `GET /tech_product/`: Retrieves all tech products.
- `POST /tech_product/`: Adds a new tech product.
- `GET /tech_product/{id}`: Retrieves a tech product by ID.
- `PUT /tech_product/{id}`: Updates a tech product by ID.
- `DELETE /tech_product/{id}`: Deletes a tech product by ID.

## Contributing

If you wish to contribute to this project, please fork the repository and propose your changes via a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

