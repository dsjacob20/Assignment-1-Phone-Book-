           
            #PROGRAM FINAL....

#Import the doc with all the information
import variable1
h= variable1.h
p= variable1.p
f= variable1.f
b= variable1.b
c= variable1.c


    #BEGINING PROGRAM...
#For space
print()                             
print()

#For the user's name
name = input("Please enter your first and last name…, ") 

#For space
print()
print()

#Show the user the options
print(name,",Select one of the following options")
print()             #For space
print("h - Contact information regarding MEDICAL EMERGENCY ")
print("p - For contact information regarding POLICE ")
print("f - FIRE DEPARTMENT contact information ")
print("b - To reach the BANK ")
print("c - Contact information for the CAB")

print()             #For space

#User choosing the option
print("Please enter the coresponding alphabet")
lookup = (input("to the service you are trying to reach, "))

#For space
print("")

print("--------------------------------------------------------------------------")

#Begining the selection
if lookup=="h":
    print(h)
elif lookup== "p":
    print(p)
elif lookup== "f":
    print(f)
elif lookup== "b":
    print(b)
elif lookup== "c":
    print(c)
else:
    print("This contact does not exist")

print("--------------------------------------------------------------------------")

#For space
print()

print ("Hope u found what you were looking for,", name)
print("Have a great rest of the day!")

#For space
print()
print()

#END PROGRAM...