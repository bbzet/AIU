n = int(input("Enter your amount of grades:  "))


def evaluate_grades(count: int) -> str:
    if count > 100 or count < 0:
        exit()
    grades = None 
    if count < 50:
        grades = "F"
    elif count >= 50 and count < 60:
        grades = "D"
    elif count >= 60 and count < 75:
        grades = "C"
    elif count >= 75 and count < 90:
        grades = "B"
    elif count >= 90 and count < 101:
        grades = "A"
    else:
        return "Nothing."
    
    if grades != None:
        return grades

A = 0 
B = 0 
C = 0
D = 0
F = 0

    
for i in range(1, n+1):
    count = evaluate_grades(int(input("Enter your grades: ")))

    if count == "F":
        F += 1
    elif count == "D":
        D += 1
    elif count == "C":
        C += 1
    elif count == "B":
        B += 1
    elif count == "A":
        A += 1 
    else:
        print('Nothing.')

def percent_evaluate(grade):
    percent = round((grade / n) * 100)
    return percent

def check_for_ammount(grade):
    return "grades" if grade > 1 else "grade"

print(f'''
A = {A} {check_for_ammount(A)} ({percent_evaluate(A)}%)
B = {B} {check_for_ammount(B)} ({percent_evaluate(B)}%)
C = {C} {check_for_ammount(C)} ({percent_evaluate(C)}%)
D = {D} {check_for_ammount(D)} ({percent_evaluate(D)}%)
F = {F} {check_for_ammount(F)} ({percent_evaluate(F)}%)
''')