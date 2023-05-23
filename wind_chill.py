temperature=float(input("enter the temp:"))
wind=float(input("enter the win speed:"))
windchill=13.12+0.6215*temperature-11.37*wind **0.16+0.3965*temperature*wind**0.16
print(windchill)
 