from app.db import db


class User(db.Model):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    role = db.Column(db.String(128), default="viewer")
    
    __table_args__ = (
        db.CheckConstraint(role.in_(["viewer", "contributor", "manager"]), name="role_types"),
    )
    
    def __init__(self, username, created_at, role):
        self.username = username
        self.created_at = created_at
        self.role = role

    def __repr__(self):
        return "<User: {}>".format(self.username)
    
    def register_if_not_exist(self):
        db_user = User.query.filter(User.username == self.username).all()
        if not db_user:
            db.session.add(self)
            db.session.commit()
        return True
    
    def get_by_username(self, username):
        db_user = User.query.filter(User.username == username).first()
        return db_user
