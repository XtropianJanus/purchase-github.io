from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_details = db.Column(db.String(200), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(200), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(200), nullable=False)

class Spoilage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(50), nullable=False)

class Intertransfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(50), nullable=False)
    from_location = db.Column(db.String(100), nullable=False)
    to_location = db.Column(db.String(100), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
