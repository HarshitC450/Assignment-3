#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ques 1

string = input("enter the string: ")
words = string.split() if " " in string else list(string)
counts = {}
for word in words:
    if word in counts:
        counts[word]+= 1
    else:
        counts[word] = 1
        
print(counts)


# In[ ]:


# ques 2

import datetime
year = int(input("enter the year="))
month = int(input("enter the month= "))
day = int(input("enter the day= "))
if not (1<=month<=12) or not (1<=day<=31) or not (1800<=year<=2025):
    print("invalid input date")
    
else:
        input_date = datetime.datetime(year,month,day)
        
        next_date = input_date + datetime.timedelta(days =1)
        print("Next date:", next_date.strftime("%Y-%m-%d"))


# In[ ]:


# ques 3

num1 = int(input("enter the 1st number = "))
num2 = int(input("enter the 2nd number = "))
num3 = int(input("enter the 3rd number = "))
num4 = int(input("enter the 4th number = "))
num5 = int(input("enter the 5th number = "))
my_list=[num1, num2, num3, num4, num5]
print("The list is:")
print(my_list)
print("The resultant tuple is :")
my_result = [(val, pow(val,2)) for val in my_list]
print(my_result)


# In[ ]:


# ques 4

grade = int(input("enter your grade ="))

if grade<4 or grade >10 :
    print("error, grade must be between 4 and 10")
else:
    if grade>=9:
        letter_grade= "A+"
        performance= "Outstanding"
    elif grade>=8:
        letter_grade= "A"
        performance = "Excellent"
    elif grade>=7:
        letter_grade = "B+"
        performance = "Very Good"
    elif garde>=6:
        letter_grade = "B"
        performance = "Good"
    elif grade>=5:
        grade = "C+"
        performance = "Average"
    elif grade>=4:
        grade = "C"
        performance = "Below Average"
    elif grade>=3:
        grade = "D"
        performance = "Poor"
    print("Your Grade is {} and {} performance".format(letter_grade,performance))


# In[ ]:


# ques 5

for i in range(10,0,-1):
    for j in range(11-i):
        print(" ", end="")
    for k in range(i):
        print(chr(65+k),end=" ")
    print()


# In[ ]:


# ques 6

students = {}
while True:
    name = input("Enter the name of student=")
    sid = input("Enter the SID of the student=")
    students[sid] = name
    more = input("Do you want to add more students (Y/N)")
    if more.upper() =='N':
        break
    print("\nStudents' Details:")
    for sid, name in students.items():
        print("SID:{sid}, Name:(name)")
        
    sorted_students = sorted(students.items(), key=lambda x:x[1])
    print("\nSorted Students (byname):")
    for sid, name in sorted_students:
        print("SID:{sid},Name:{name}" )
        
    sorted_students = sorted(students.items(), key=lambda x:x[0])
    print("\nSorted Students (byname):")
    for sid, name in sorted_students:
        print("SID:{sid},Name:{name}" )
        sid = input("\nEnter the SID of the student you want to search: ")
    if sid in students:
        print("Name of the student with SID {sid}:{students[sid]}")
    else:
        print("No student found with SID {sid}")


# In[ ]:


#question 7

n= int(input("enter the no. of values= "))
a,b= 0,1
sum= 0
print(a)
print(b)
sum= a+b
for i in range(2,n):
    c= a+b
    print(c)
    sum+=c
    a,b = b,c
    
average = sum/n
print("average:", average)


# In[ ]:


# question 8

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

#a 
print(" Q8(a)")
print("A new set of all elements that are in set1 and set2 but not both is:",)
set_sym_dif=set1.symmetric_differnce(set2)
print(set_sym_dif)

#b
print("\nQ8(b)")
print("\nA new set of all elements that are in only one of the three sets Set1,Set2 and Set3 is:")
set_u1 = set1.union(set2)
set_uf = set2.union(set3)
set_i1 = set1.intersection(set2)
set_if = set2.intersection(set3)
set_12 = set1.intersection(set2)
set_23 = set2.intersection(set3)
set_13 = set1.intersection(set3)
set_f1 = set_uf-set_23-set_13
print(set_f1)

#c

print("\nQ8(c)")
set_c1 = set_12.union(set_23)
set_c2 = set_c1.union(set_13)
set_final = set_c2-set_if
print("\nA new set of all elements that are exactly in two of the sets Set1, Set2 and Set3 is:")
print(set_final)

#d

print("\nQ8(d)")
set_d = [1,2]
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new = set_d-set1
#printing final set
print("\nAnew set of all integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)


#e
print("\nQ8(e)")
set_e-set_uf
print("\nAnew set of all integers in the 'range 1 to 10' that are not in Set1,Set2 and Set3 is:")
print(set_e)

