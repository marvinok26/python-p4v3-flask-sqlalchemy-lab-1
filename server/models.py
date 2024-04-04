from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class Earthquake(db.Model, db.Serializers):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"


class EarthquakeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Earthquake
        load_instance = True
        include_relationships = True

    id = fields.Int(dump_only=True)