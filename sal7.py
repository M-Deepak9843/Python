salary=int(input("enter the curent salary"))
work=int(input("enter the year of services"))
if(work>10):
    bonus=salary*0.1
    print("bonus",bonus)
elif(work<=10 and work>6):
    bonus=salary *0.08
    print("bonus",bonus)
else:
    bonus=salary*0.05
    print("bonus",bonus)