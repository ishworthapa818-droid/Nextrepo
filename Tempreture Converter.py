Choice = input("Convert from (C/F): ").upper()
temp = float(input("Enter tempreture: "))
if Choice == 'C':
    f = (temp * 9/5) + 32
    print("Tempreture in Fahrenheit:", f)
elif Choice == 'F':
    c = (temp - 32) * 5/9
    print("Tempreture in Celsius:", c)
else:
    print("Invalid Choice")