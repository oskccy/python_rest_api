from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

app.app_context().push()
db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.String(50))
    social_insurance = db.Column(db.String(60))
    credit_card = db.Column(db.String(60))

    def __repr__(self):  # represent this as a dictionary
        return f"User({self.first_name, self.last_name, self.id})"


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/users')
def get_users():
    users = User.query.all()

    formatted_obj = []
    for user in users:
        formatted_obj.append(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "social_insurance": user.social_insurance,
                "credit_card": user.credit_card,
            }
        )

    return formatted_obj


@app.route('/users/<id>')
def get_user_by_id(id):
    user = User.query.get_or_404(id)
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_number": user.phone_number,
        "social_insurance": user.social_insurance,
        "credit_card": user.credit_card,
    }

@app.route('/users', methods=["POST"])
def add_user():
    user = User(
        first_name=request.json["first_name"], 
        last_name=request.json["last_name"], 
        phone_number=request.json["phone_number"],
        social_insurance=request.json["social_insurance"],
        credit_card=request.json["credit_card"]
    )
    db.session.add(user)
    db.session.commit()

    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_number": user.phone_number,
        "social_insurance": user.social_insurance,
        "credit_card": user.credit_card,
    }

@app.route('/users/<id>', methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return {
            "ERROR": "id not found"
        }
    db.session.delete(user) 
    db.session.commit()
    return {
        "successfully deleted user!": id
    }
