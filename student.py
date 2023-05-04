import os 
import sys
import json

student = []

file = open("student.txt", 'r').read().split("\n")

for i in range(len(file)):
    student.append(file[i])

string = """

1. New Student
2. Mark a Student
3. Print All
4. Exit

"""

print(string)


def NStudent(name):
    open("student.txt", 'a').write('\n{}'.format(name))
    student.append(name)

def MStudent(name, mark):
    mark = int(mark)
    if name in student:
        with open("student.json", "r+") as jsonFile:
            data = json.load(jsonFile)

            data["{}".format(name)] = mark

            jsonFile.seek(0)
            json.dump(data, jsonFile)
            jsonFile.truncate()
            jsonFile.close()

def PStudent():
    for i in range(len(student)):
        f = open('student.json', 'r')
        data = f.read()
        f.close()
        std = json.loads( data )[student[i]]
        print('{}:{}'.format(student[i], std))

while True:
    inp = int(input("Enter your choice: "))

    if inp == 1:
        NStudent(input("Enter Student Name: "))
    elif inp == 2:
        MStudent(name=input("Enter Student Name: "), mark=input("Enter your Mark: "))
    elif inp == 3:
        PStudent()
    elif inp == 4:
        sys.exit()
    else:
        print("Your Choice is not valid")
