from sqlalchemy import ForeignKeyConstraint

from app.db import db
from app.users.models import User


class House(db.Model):
    
    __tablename__ = "houses"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint([owner_id], [User.id], ondelete="NO ACTION"),
    )
    
    def __init__(self, address, owner_id):
        self.address = address
        self.owner_id = owner_id
    
    def to_dict(self):
        return {
            "address": self.address,
            "owner_id": self.owner_id
        }
    
    def build(self):
        record = House.query.filter(House.id == self.id).first()
        if not record:
            db.session.add(self)
            db.session.commit()
        return True
    
    def get_owner_houses(owner_id):
        records = House.query.filter(House.id == owner_id).all()
        return [r.to_dict() for r in records]
    
    def __repr__(self):
        return f"<House: {self.address}>"
