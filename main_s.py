from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()



students={
    "s001":{"name":"jonnu", "marks":72, "grade": "B"},
    "s002":{"name":"jony", "marks":85, "grade": "A"},
    "s003":{"name":"jonny", "marks":92, "grade": "A"},
    "s004":{"name":"jack", "marks":65, "grade": "C"},
    "s005":{"name":"jeck", "marks":78, "grade": "B"},
    "s006":{"name":"jon", "marks":55, "grade": "D"}
}

class MarksSubmission(BaseModel):
    student_id: str
    marks: int
    subject: str

@app.get("/student/{student_id}")
def get_student(student_id: str):

    if student_id not in students:
        raise HTTPException(status_code=404, detail=f"student with ID {student_id} not found")

    return students[student_id]

@app.post("/submit_marks")
def submit_marks(submission:MarksSubmission):
    
    #error1: student doesnot exist
    if submission.student_id not in students:
        raise HTTPException(status_code=404, detail=f"student with ID {submission.student_id} not found")

    #error2: valid range 0 - 100
    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(status_code=400, detail={
            "error": "marks must be between 0 - 100",
            "marks_received":submission.marks,
            "fix":"enter a valid value between 0 and 100",
        })

    #error3: subject name empty
    if submission.subject.strip() == "":
            raise HTTPException(status_code=400, detail={
                "error":"Subject name cannot be empty",
                "submitted_subject":submission.subject,
                "fix":"Please enter a valid subject"
            })

    try:
        students[submission.student_id]["marks"]=submission.marks

        return{
        "message":"Marks submitted successfully",
        "student":students[submission.student_id]["name"],
        "subject":submission.subject,
        "marks":submission.marks
    }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")



    

    

    


   