# Please write a program which asks for the names and ages of two persons.
# The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

# Write your code here:
firstname = input("What is the name of the first person? : ")
firstage = int(input("What is the age of the first person?: "))
secondname = input("What is the name of the second person?: ")
secondage = int(input("What is the age of the second person?: "))

if firstage>secondage:
    print("The first person is the elder")
if secondage>firstage:
    print("The second person is the elder")