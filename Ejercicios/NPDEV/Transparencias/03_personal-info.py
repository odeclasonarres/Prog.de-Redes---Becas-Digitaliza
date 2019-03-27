#Create and run a script to collect personal information.

#Open a blank script file and save it as 03_personal-info.py.
#Create a script that asks for four pieces of information such as: first name, last name, location, and age.
#Create a variable for a space: space = " ".
#Add a print statement that that combines all the information in one sentence.
#Your script should run without any errors, as shown in Example 1.


fn=input("¿Cuál es tu nombre? ")
ln=input("¿Cuáles son tus apellidos? ")
loc=input("¿Dónde vives? ")
age=input("¿Cuál es tu edad? ")
space= " "

print("Te llamas"+space+fn+space+ln+", vives en"+space+loc+space+"y tienes"+space+age+space+"años.")
