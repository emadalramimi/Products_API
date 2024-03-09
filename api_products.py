from flask import Flask, request
from flask_restx import Api, Resource, fields
import db_products as db_client  # Assuming db_produits.py is now db_products.py

app = Flask(__name__)
api = Api(app, version='0.1', title='Online Shop API',
          description='This API allows for the creation, modification, and deletion of products. It also enables product search and purchase.')

# Namespaces
ns_food = api.namespace('food_product', description="Operations on food products.")
ns_tech = api.namespace('tech_product', description="Operations on technological products.")

# Models
food_product_model = api.model('Food Product', {
    'id': fields.Integer(readonly=True, description="Unique product identifier"),
    'label': fields.String(required=True, description="Product label"),
    'category': fields.String(required=True, description="Product category"),
    'price': fields.Float(required=True, description="Product price")
})

tech_product_model = api.model('Tech Product', {
    'id': fields.Integer(readonly=True, description="Unique product identifier"),
    'label': fields.String(required=True, description="Product label"),
    'category': fields.String(required=True, description="Product category"),
    'description': fields.String(required=True, description="Product description"),
    'brand': fields.String(required=True, description="Product brand"),
    'price': fields.Float(required=True, description="Product price")
})

# Food Product Endpoints
@ns_food.route('/')
class FoodList(Resource):
    @ns_food.doc('list_food_products', description='Retrieve a list of all food products.')
    @ns_food.marshal_list_with(food_product_model)
    def get(self):
        """Gets all food products"""
        return db_client.list_food_products()

    @ns_food.doc('create_food_product', description='Create a new food product with the specified details.')
    @ns_food.expect(food_product_model)
    def post(self):
        """Creates a new food product"""
        data = request.json
        product_id = db_client.add_food_product(data['label'], data['category'], data['price'])
        return {'id': product_id}, 201

@ns_food.route('/<int:id>')
@ns_food.response(404, 'Product not found')
@ns_food.param('id', 'The product identifier')
class Food(Resource):
    @ns_food.doc('get_food_product', description='Retrieve a specific food product by its ID.')
    @ns_food.marshal_with(food_product_model)
    def get(self, id):
        """Gets a specific food product by ID"""
        product = db_client.get_food_product(id)
        if product:
            return product
        api.abort(404, f"Food product with ID {id} not found")

    @ns_food.doc('update_food_product', description='Update the details of an existing food product by its ID.')
    @ns_food.expect(food_product_model)
    def put(self, id):
        """Updates a food product by ID"""
        data = request.json
        db_client.update_food_product(id, data['label'], data['category'], data['price'])
        return {'message': 'Product successfully updated'}, 200

    @ns_food.doc('delete_food_product', description='Delete a food product from the database by its ID.')
    def delete(self, id):
        """Deletes a food product by ID"""
        db_client.delete_food_product(id)
        return {'message': 'Product successfully deleted'}, 204

# Tech Product Endpoints
@ns_tech.route('/')
@ns_tech.response(404, 'Product not found')
class TechList(Resource):
    @ns_tech.doc('list_tech_products', description='Retrieve a list of all tech products.')
    @ns_tech.marshal_list_with(tech_product_model)
    def get(self):
        """Gets all tech products"""
        return db_client.list_tech_products(), 200

    @ns_tech.doc('create_tech_product', description='Create a new tech product with the specified details.')
    @ns_tech.expect(tech_product_model)
    def post(self):
        """Creates a new tech product"""
        product_data = request.json
        product_id = db_client.add_tech_product(**product_data)
        if product_id:
            return api.marshal(db_client.get_tech_product(product_id), tech_product_model), 201
        else:
            api.abort(400, "Failed to create product")

@ns_tech.route('/<int:id>')
@ns_tech.param('id', 'The product identifier')
class Tech(Resource):
    @ns_tech.doc('get_tech_product', description='Retrieve a specific tech product by its ID.')
    @ns_tech.marshal_with(tech_product_model)
    def get(self, id):
        """Gets a specific tech product by ID"""
        product = db_client.get_tech_product(id)
        if product is None:
            api.abort(404, f"Tech product with ID {id} not found")
        else:
            return product, 200

    @ns_tech.doc('delete_tech_product', description='Delete a tech product from the database by its ID.')
    def delete(self, id):
        """Deletes a tech product by ID"""
        db_client.delete_tech_product(id)
        return '', 204

    @ns_tech.doc('update_tech_product', description='Update the details of an existing tech product by its ID.')
    @ns_tech.expect(tech_product_model)
    def put(self, id):
        """Updates a tech product by ID"""
        product_data = request.json
        db_client.update_tech_product(id, **product_data)
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
