from fastapi import FastAPI,HTTPException

app=FastAPI(title= "Silver is the best")

@app.get("/")
def home():
    return{"message": "Messi is the GOAT"}


Student=[
    {"id": 1,
     "Name": "Silver",
     "Age": 17,
     "Course":"FastApi"
    },
    {
        "id":2,
        "Name": "James",
        "Age": 25,
        "Course": "Computer Science"  
    },
    {
        "id":3,
        "Name": "Gold",
        "Age": 20,
        "Course": "Micro-Biology"
    },
    {
        "id":4,
        "Name": "Fidelia",
        "Age": 39,
        "Course": "Marketing",
    }
]

@app.get("/students")
def get_Student():
    return Student

@app.get("/students/{student_id}")
def get_student(student_id:int):
        for student in Student:
              if student["id"] == student_id:
                 return student

        raise HTTPException(
            status_code= 404,
            detail="Studennt Not found"
        )

# CREATING PYDANTIC CALL OR  MODEL
from pydantic import BaseModel

class CreateStudent(BaseModel):
    name:str
    age:int
    course:str

@app.post("/students")
def Create_Student(student: CreateStudent):
    new_student = {
        "id": len(Student) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    Student.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_Student(student_id:int,student:CreateStudent):

    for existing_student in Student:

      if existing_student["id"]==student_id:
        existing_student["name"]=student.name
        existing_student["age"]=student.age
        existing_student["course"]=student.course
        return existing_student


#Delete

@app.delete("/students/{student_id}")
def delete(student_id: int):

    for user in Student:
        if user["id"] == student_id:
            Student.remove(user)
            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )