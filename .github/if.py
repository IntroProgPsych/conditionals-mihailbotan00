# if = does a code ONLY IF the condition is TRUE
# else = is not going to do anything

age = int(input("Type your age: "))
if age>=16 and age<100:
    print("You are an adult")
elif age>=100:
    print("Your time has passed")
elif age<0:
    print("You're not even born yet")
else:
    print("You are a child")