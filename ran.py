import random
alpha=["A ",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z","a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z","@", "#", "$", "%", "^", "&", "*", "[", "]", ",", ".",1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

option=input("1.Create new password or"+"\n"+
"2.Access password:")

file=open("password.txt")

def access(passName):
    for line in file:
        if line.startswith(passName):
            arr=line.split()
            print(arr[1])
    quit()


if int(option)==1:
    length=input("Enter Length of Password:")
elif int(option)==2:
    passName=input("Enter Website name:")
    access(passName)
    
count=0
password=[]
while count<int(length):
    password.append(random.choice(alpha))
    count=count+1
actPassword="".join(map(str,password))
print(actPassword)

file=open("password.txt","a")
choice=input("yes or no?:")

if choice=="yes":
    purpose=input("Password for?:")
    file.write(purpose+"  "+actPassword+"\n")
    print("Password has been saved successfuly!")
else:
    quit()
