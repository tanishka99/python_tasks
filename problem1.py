Problem 1 :

 Create a program that asks the user to enter their name and their age.
 Print out a message that will tell them the year that they will turn 95 years old.

#!usr/bin/python3
n=input("What is your name")
a=int(input("what is your age?"))
year=int(input("what is the current year?"))
diff=year-a
final=diff+95
print("year in which u will be 95 years old is :")
print(final)
