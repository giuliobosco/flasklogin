""" Database models. """
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    """User account Model."""

    __tablename__ = 'flasklogin-users'
    id = db.Column(
            db.Integer,
            primary_key=True
    )
    name = db.Column(
            db.String(100),
            nullable=False,
            unique=False
            )
    email = db.Column(
            db.String(40),
            nullable=False,
            unique=True
            )
    password = db.Column(
            db.String(200),
            primary_key=False,
            unique=False,
            nullable=False
            )
    website = db.Column(
            db.String(60),
            index=False,
            unique=False,
            nullable=True
            )
    created_on = db.Column(
            db.DateTime,
            index=False,
            unique=False,
            nullable=True
            )
    last_login = db.Column(
            db.DateTime,
            index=False,
            unique=False,
            nullable=True
            )
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_passwordhash(
           password,
           method='sha256'
        )

    def check_password(self, password):
        """check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
