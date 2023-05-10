from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, MenuItem, Menu, MenuItemType


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")
    dinner = Menu(name="Dinner")
    db.session.add(employee)
    db.session.add(beverages)
    db.session.add(entrees)
    db.session.add(sides)
    db.session.add(dinner)
    db.session.commit()
    fries = MenuItem(name="French fries", price=3.50, type=sides.id, menu=dinner.id)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages.id, menu=dinner.id)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees.id, menu=dinner.id)
    db.session.add(fries)
    db.session.add(drp)
    db.session.add(jambalaya)
    db.session.commit()
    # print(dinner.to_dict())
