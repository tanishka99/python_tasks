#Problem 3 : 

 #take a list say  adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
#write the program that will do
 # i)  print only those numbers greater than 5
  #ii)  also print those numbers those are less than or  equals to 2  ( <= 2 )
  #iii)  store these answers in in two different list also

#!usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
x=[i for i in adhoc if i>5]
print(x)
y=[i for i in adhoc if i<=2]
print(y)

or 

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
less=[]
greater=[]
for i in adhoc:
    if i<=2:
        less.append(i)
    elif i>5:
        greater.append(i)
print("values less than or equal to 2:\n")
print(less)
print("values greater than 5:")
print(greater)
