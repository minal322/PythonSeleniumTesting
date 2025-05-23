##########################################
#reverse a number
num = 65423
rev =0
while num > 0:
    q = num %10
    rev = 10 * rev + q
    num = num //10

print(rev)

#############################
#count number of digits in number
num = 123689
count = 0
while num !=0:
    count +=1
    num = num // 10
print(count)

##################################################
# count vowels and consonants
str = "MinalPatil"
vow = 0
cons = 0

for i in str:
    if i in "aeiou" or i in "AEIOU":
        vow +=1
    else:
        cons +=1
print("vowels-",vow)
print("Consonantr - ",cons)

#####################################################
#fib series is number of previous two numbers
def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)

print("fibonacci Series-",fibo(5))
###############################################
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num -1)
print("factorial-",factorial(5))

#####################################################
arr = [1,6,9,8,3,7,6]

arr.sort()
print(arr[0])
print(arr[len(arr) - 1])
###############################
palindrome_or_not = "anhdna" # a word or number or that reads the same backward as forward
print(palindrome_or_not == palindrome_or_not[::-1])

#################################################################
str = "Hello minutu"
rev = ''

for i in str:
    rev = i + rev
print(rev)
print(str[::-1])

###########################################################
str = "hello"

print(str[::-1])
rev = ""
for i in str:
    rev = i + rev
print(rev)

##############################################################
arr = [8,9,1,2,3,7,8,9]
lst= [1,5,6,89,65]
lst.extend(arr)
print("Extends",set(lst))
print(arr[::-1])
arr.sort(reverse=True)
print(arr)
print(sorted(arr))

