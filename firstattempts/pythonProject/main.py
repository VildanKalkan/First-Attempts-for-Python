
#1
side1= int(input("Write side1"))
side2= int(input("Write side2"))
area= int((side1*side2))
perimeter= int((side1+side2)*2)
print("The area of the rectangle is", area)
print("The perimeter of the rectangle is", perimeter)

#2
weight= int(input("What is your weight"))
height= int(input("What is your lenght"))
index= int((height**2)/weight)
print("Your body mas index is", index)

#3
gaso_1hour= float(input("How many litres gasoline uses your car in a hour"))
km_1hour= float(input("How many kilometers do your car in a hour"))
gaso_dolar= float(input("How much is a litre of gasoline"))
sum_of_cash_hour= float(gaso_dolar*gaso_1hour)
sum_of_cash_1km= float((gaso_1hour/km_1hour)*gaso_dolar)
print("How much cash do my car uses in a hour", sum_of_cash_hour)
print("How much cash do my car uses in a kilometer", sum_of_cash_1km)


