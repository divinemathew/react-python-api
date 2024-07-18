from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  #  Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb://localhost:27017/school"
app.config["JWT_SECRET_KEY"] = "123"

mongo = PyMongo(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({'username': username, 'password': hashed_password})
    return jsonify({"msg": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    username = data.get('username')
    password = data.get('password')
    user = mongo.db.users.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/students', methods=['POST'])
@jwt_required()
def add_student():
    data = request.get_json()
    mongo.db.students.insert_one(data)
    return jsonify({"msg": "Student added successfully"}), 201

@app.route('/students', methods=['GET'])
@jwt_required()
def get_students():
    students = list(mongo.db.students.find())
    for student in students:
        student['_id'] = str(student['_id'])
    return jsonify(students), 200

@app.route('/students/<student_id>', methods=['GET'])
# @jwt_required()
def get_student(student_id):
    student = mongo.db.students.find_one({'_id': ObjectId(student_id)})
    if student:
        student['_id'] = str(student['_id'])
        return jsonify(student), 200
    return jsonify({"msg": "Student not found"}), 404

@app.route('/students/<student_id>', methods=['PUT'])
# @jwt_required()
def update_student(student_id):
    data = request.get_json()
    mongo.db.students.update_one({'_id': ObjectId(student_id)}, {"$set": data})
    return jsonify({"msg": "Student updated successfully"}), 200

@app.route('/students/<student_id>', methods=['DELETE'])
# @jwt_required()
def delete_student(student_id):
    mongo.db.students.delete_one({'_id': ObjectId(student_id)})
    return jsonify({"msg": "Student deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
