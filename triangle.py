side1 = int(input("Enter Length of Side 1 : "))
side2 = int(input("Enter Length of Side 2 : "))
side3 = int(input("Enter Length of Side 3 :3 "))
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2) :
    print("It is a Valid Triangle")
else:
    print("It is an invalid Triangle")