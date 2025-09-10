from pydantic import BaseModel, EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str
    age:Optional[int] = None
    email: EmailStr
    cgpa : float = Field(gt=0, lt=10, description="CGPA must be between 0 and 10")


new_student = {'name': "ajay",'age':25,'email':'abc@mail.com','cgpa':0.5}

student = Student(**new_student)
print(type(Student))
print(student)

#we con convert pytdant
print(dict(student))
print(student.model_dump_json())

