#!/usr/bin/python3

a1=[1, 2, 3, 9, 4, 5, 6, 9, 8, 7, 10]

print(a1)

myset=set(a1) # removes the duplicate
print(myset)

sum_a1=sum(a1)
sum_myset=sum(myset)
the_dif=sum_a1-sum_myset

print("The duplicate: " + str(the_dif))



