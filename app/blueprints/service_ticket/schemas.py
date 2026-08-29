from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from app.models import ServiceTicket
from app.extensions import db


class ServiceTicketSchema(SQLAlchemyAutoSchema):
    id = fields.Integer(dump_only=True)
    customer_id = fields.Integer(required=True)

    class Meta:
        model = ServiceTicket
        load_instance = True
        sqla_session = db.session