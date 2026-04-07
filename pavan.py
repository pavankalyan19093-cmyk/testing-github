name=input("enter your name: ")
age=int(input("enter your age: "))
height=float(input("enter height:"))
student=input("are you a student ? (yes/no):")
print(f"name:{name}| age:{age}|height:{height} |student:{student}")
months=age*12
days=age*365+(age%4)
power=age**2
remainder=age//7
print(f"months: {months}, days: {days}, power: {power}, remainder: {remainder}")