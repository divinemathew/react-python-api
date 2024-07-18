from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')
db = client.school

students = []
teachers = []

# Create 100 students
for i in range(100):
    students.append({
        "name": f"Student {i+1}",
        "age": random.randint(10, 18),
        "grade": random.choice(['A', 'B', 'C', 'D', 'E']),
        "subjects": random.sample(['Math', 'Science', 'History', 'Art', 'Physical Education'], 3)
    })

# Create 10 teachers
for i in range(10):
    teachers.append({
        "name": f"Teacher {i+1}",
        "subject": random.choice(['Math', 'Science', 'History', 'Art', 'Physical Education'])
    })

db.students.insert_many(students)
db.teachers.insert_many(teachers)
# db.teachers.delete_many({})
# db.students.delete_many({})