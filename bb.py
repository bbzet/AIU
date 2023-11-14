import os

name = input("Enter your name: ")
surname = input("Enter your surname: ")

input(f'Welcome to international univesity Ala-too {name.title()} {surname.title()}.\n If you want to be a student of international universty Ala-Too these are our requirements.\n1. Ort score have to be more than 110.\n2. The english proficiency level should not to be less than intermediate(B1).\n3. Provide your presence of school education certificate.\nIf you want to continue just print Enter.')

os.system("cls")


school_educaation_certificate = bool(int(input("Do you have school education certificate? If you have print 1. If you don't have print 0 ")))
if school_educaation_certificate == False:
    print("You're not admited due to not having school certificate.")
    exit()

ort_score = None
while(True):
    ort_score = int(input("Enter your ORT score: "))

    if ort_score > 240:
        print("Enter right amount of ORT score. ")
    elif ort_score <= 109:
        print("You don't have enough scores.")
        exit()
    elif(ort_score > 109 and ort_score < 241):
        break


inputLevel = input('''
Enter your english level                   
Beginner (A1) 
Preintermediate (A2)
Intermediate (B1)
Upperintermediate (B2)
Advanced (C1)
Academic (C2)
''')

test = None 
if(str.upper(inputLevel) == str.upper("A1") or str.upper(inputLevel) == str.upper("A2")):
    test = "You're not availavle for studying 1st course.\nWe have foundation year where you can improve your english.\nAfter foundation year you can study 1st course."
    print(test)
    exit()
elif(
    str.upper(inputLevel) == str.upper("B1") or
    str.upper(inputLevel) == str.upper("B2") or
    str.upper(inputLevel) == str.upper("C1") or
    str.upper(inputLevel) == str.upper("C2")):
    test = "You're enough good at english to study 1st course."
    print(test)
else:
    test = "You're not availavle for studying 1st course.\nWe have foundation year where you can improve your english.\n After foundation year you can study 1st courese."
    print(test)
    exit()


os.system("cls")


faculty_number = int(input('''
Choose your faculty.
                       
1 computer engineering = 2500$
2 artificial intellegence = 2200$
3 psychology = 1900$ 
4 journalism = 1700$
5 internationals relations = 2200$
6 law = 1800$
7 managment = 2200$
8 medicine = 3300$
'''))

os.system("cls")



faculties_list = ["Computer Engineering", "Artificial Intelligence", "Psychology", "Journalism", "International Relations", "Law", "Management", "Medicine"]
faculties_costs = [2500, 2200, 1900, 1700, 2200, 1800, 2200, 3300]

def greeting_message(name, surname, ort_score, faculty_number):
    print("Dear, " + name + " " + surname + " we congratulate you! You have been admitted to the " + faculties_list[faculty_number - 1] + " program at Ala-Too International University.")
    discount = 0
    discountPrice = 0

    if ort_score < 140:
        print("Your tuition is"  + str(faculties_costs[faculty_number]) +"$")
        return
    else:     
        print('''These are our discounts depending on your ORT results.
        110-140 discount 0% 
        140-155 discount 5% 
        156-174 discount 10% 
        175-199 discount 25% 
        200-209 discount 50% 
        210-218 disscount 75% 
        219-240 discount 100% 
        ''')   
        if ort_score >= 140 and ort_score <= 155:
            discount = 5
            discountPrice = 0.95 * faculties_costs[faculty_number - 1]
        elif ort_score >= 156 and ort_score <= 174:
            discount = 10
            discountPrice = 0.9 * faculties_costs[faculty_number - 1]
        elif ort_score >= 175 and ort_score <= 199:
            discount = 25
            discountPrice = 0.75 * faculties_costs[faculty_number - 1]
        elif ort_score >= 200 and ort_score <= 209:
            discount = 50
            discountPrice = 0.5 * faculties_costs[faculty_number - 1]
        elif ort_score >= 210 and ort_score <= 218:
            discount = 75
            discountPrice = 0.25 * faculties_costs[faculty_number - 1]
        elif ort_score >= 219 and ort_score <= 240:
            discount = 100

    print(f"The cost of your tuition with a {discount}%")
    print(f"Your tuition is {discountPrice}$")

greeting_message(name, surname, ort_score, faculty_number)
