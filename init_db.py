from app import app, db
from models import Contact, User, Student

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database reset successful!")