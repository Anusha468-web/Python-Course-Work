student_name=input("Enter student name: ")
age=int(input("Enter age: "))
passed_out_date=input("Enter passedout date: ")
cgpa=float(input("Enter cgpa: "))
college_name=input("Enter clg name: ")
stream=input("Enter stream: ")
                    
#Input for programming lang known using list
programming_lang=[]
while True:
    prgm=input("Enter prgmming lang you know: ")
    if prgm.lower()=="none":
        break
    programming_lang.append(prgm)

#Input for languages known using tuple
languages=[]
while(True):
    lang=input("Enter languages you kown: ")
    if lang.lower()=="none":
        break
    languages.append(lang)
languages_known=tuple(languages)

#Input for subjects using set
subjects=set()
while(True):
    sub=input("Enter subjects in your degree: ")
    if sub.lower()=="none":
        break
    subjects.add(sub)

#Input for project details using dict
print("Enter project Details")
project={"Title":"","Duration":"","Role":""}
project["Title"]=input("Enter project title: ")
project["Duration"]=input("Enter project duration: ")
project["Role"]=input("Enter your role in project: ")

#Input for backlogs using bool
any_backlog=False
backlog=input("Enter if u have any backlog(yes/no): ")
if backlog.lower()=="yes":
    any_backlog=True

#Ouput stmts
#ouput type1
print("="*50)
print("Admission Details of a Student")
print("="*50)
print(f"Student Name:{student_name}")
print(f"Passed out year:{passed_out_date}")
print(f"CGPA:{cgpa}")
print(f"College Name:{college_name}")
print(f"Stream:{stream}")
print("Programming langs known:",programming_lang)
print("Languages known:",languages_known)
print("Subjects in Degree:",subjects)
print("Project:",project)
print("Any backlog:",backlog)
print("="*50)
