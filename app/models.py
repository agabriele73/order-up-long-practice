from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Employee(db.Model, UserMixin):  # Your class definition
    # Mapping attributes, here
    __tablename__ = 'employees'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    items = db.relationship("MenuItem", back_populates='menus')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "items": { item.id: item.to_dict() for item in self.items }
        }

class MenuItem(db.Model):
    __tablename__ = 'menu_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.Integer, db.ForeignKey('menu_item_types.id'), nullable=False)
    menu = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)

    menus = db.relationship("Menu", back_populates='items')
    menu_types = db.relationship("MenuItemType", back_populates='menu_items')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "menu_name": self.menus.name,
            "menu_item_name": self.menu_types.name,
            "price": self.price,
            "type": self.type
        }

class MenuItemType(db.Model):
    __tablename__ = 'menu_item_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    menu_items = db.relationship("MenuItem", back_populates='menu_types')
