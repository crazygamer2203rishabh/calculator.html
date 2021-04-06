def marksheet():
    name=str(input("enter your name = "))
    subject1_marks=float(input("enter your english marks = "))
    subject2_marks=float(input("enter your sst marks = "))
    subject3_marks=float(input("enter your maths marks = "))
    subject4_marks=float(input("enter your hindi marks = "))
    subject5_marks=float(input("enter your computer marks = "))
    subject6_marks=float(input("enter your science marks = "))
    total_marks=(subject1_marks+subject2_marks+subject3_marks+subject4_marks+subject5_marks+subject6_marks)
    percentage=(total_marks/600*100)
    print(name,"your percentage is",percentage,"%")

marksheet()
