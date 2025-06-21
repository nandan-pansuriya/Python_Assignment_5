dict={ "Alice": 85 , "Bob": 75 , "Elon": 65 }

name = input("Enter the stusent's name: ")
try:
    print(f"{name}'s marks: {dict[name]}")
except Exception :
    print("Student not found.")