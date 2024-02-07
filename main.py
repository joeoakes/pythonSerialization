import json

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["grade"])

# Creating an instance of the Student class
student1 = Student("Alice", 17, "11th")

# Serialization: Converting the student object to JSON string
student_json = json.dumps(student1.to_dict())

print("Student object serialized to JSON string:")
print(student_json)

# Deserialization: Converting the JSON string back to a student object
loaded_student_dict = json.loads(student_json)
loaded_student = Student.from_dict(loaded_student_dict)

print("\nStudent object deserialized from JSON string:")
print("Name:", loaded_student.name)
print("Age:", loaded_student.age)
print("Grade:", loaded_student.grade)

