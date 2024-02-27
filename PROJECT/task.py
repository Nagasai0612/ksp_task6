#operators
#arithmatic op + - * / % **

num1=10
num2=15
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)

#assignment operators: =,+=,-=,*=,/=,**=,%=

number3=20
number4=10
print(number3)
number3+=2
print(number3)
number3-=3
print(number3)
number3*=6
print(number3)
number3/=3
print(number3)
number4%=2
print(number4)
number4//=5
print(number4)
number3**=3
print(number3)

#comparision operators ==,!=,<,>,<=,>=
print(num1=num2)
print(num1!=num2)
print(number3<number4)
print(number3>number4)
print(num1>=number3)
print(num2<=number4)

#logical operators
print(num1 < 11 and number4 > 3)
print(number3 < 11 or num2 > 3)
print(not(number3 < 11 and number4 > 3))

#strings
name1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
print(len(name1))
print(name1[2:50])
name2 = num1+" "+num2
print(name2)

##camelcase
x="zero"
print(x)

#for
for anand in range(5):
    print("iloveindia")

#while
    number5 = 12
    while number5<30:
        print(number5)
        number5 +=1

#if else, elif
if number3==8:
    print("corect")
elif number4<10:
    print("hello")
else:
    print("bye")

#input
    name=input("enter your name")
print(name)