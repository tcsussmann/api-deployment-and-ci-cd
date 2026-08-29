from flask import jsonify, request
from . import customer_bp
from app.models import Customer
from app.extensions import db
from .schemas import CustomerSchema


@customer_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()

    return jsonify([
        {
            'id': customer.id,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'email': customer.email,
            'phone': customer.phone,
            'address': customer.address
        }
        for customer in customers
    ])


@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.get_json()

    schema = CustomerSchema()
    customer = schema.load(data)

    db.session.add(customer)
    db.session.commit()

    return schema.dump(customer), 201

@customer_bp.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)

    data = request.get_json()

    customer.first_name = data.get('first_name', customer.first_name)
    customer.last_name = data.get('last_name', customer.last_name)
    customer.email = data.get('email', customer.email)
    customer.phone = data.get('phone', customer.phone)
    customer.address = data.get('address', customer.address)

    db.session.commit()

    schema = CustomerSchema()

    return schema.dump(customer), 200

@customer_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)

    db.session.delete(customer)
    db.session.commit()

    return {'message': 'Customer deleted successfully'}, 200