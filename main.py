from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def index():
    return "Welcome to the User Management API!"

@app.route("/get-user/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route("/update-user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    
    db.session.commit()
    return jsonify({"message": "User updated successfully", "user": {"id": user.id, "name": user.name, "email": user.email}}), 200

@app.route("/delete-user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
