print("****************************")
print("Welcome to My Quiz Game!!!")


Question_bank=[
    {
        "text":"The ability of one class acquire methods and attributes of anoher class is called_____.","answer":"A"},
    {"text":"Which of the following is a type of inheritance?","answer":"D"},
    {"text":"Which  type of inheritance has mulitple subclass to a single superclass?","answer":"C"},
    {"text":"What is the depth of multilevel inheritance in Python?","answer":"C"},
    {"text":"What does MRD stands for?","answer":"B"}
]

options=[["A.inheritance","B.Abstraction","C.Polymorphism","D.Objects"],
        ["A.single","B.Double","C.Multiple","D.both A annd C"],
        ["A.Multiple Inheritance","B.Multilevel Inheritance","C.Hierarchical Inheritance","D.None of these"],
        ["A.wo level","B.Three level","C.Any level","D.None of these"],
        ["A.Method Recursive Object","B.Method Resolution Order","C.Main Resoluion Order","D.Metod Resoluion Object"]]
score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
for Question_num  in range(len(Question_bank)):  #0 1 2 3 4
    print("*********************")
    print(Question_bank[Question_num]["text"])
    for i in options[Question_num]:
        print(i)

    quess=input("Enter your answer(A/B/C/D): ").upper()
    is_correct=check_answer(quess,Question_bank[Question_num]["answer"])
    if is_correct:
        print("Corect Answer")
        score+=1
    else:
        print("Incorrect answer")
        print(f"The correct answer is {Question_bank[Question_num]['answer']}")
    print(f"Your current score is {score}/{Question_num+1}")
print(f"You have given {score} correct answers")
print(f"Your score is {(score/len(Question_bank))*100}%")