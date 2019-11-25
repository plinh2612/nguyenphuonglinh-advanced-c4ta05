#Chuyen mục học hỏi:
'''
loop = True
while loop:
    inp = input('Enter a number: ')
    try:
        number = int(inp)
        print("Good girl")
        loop = False
    except ValueError:
        print('Bad girl')
'''


# Task1:
'''
first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))
print("Sum:", first + second)
'''

# Task2 (1st way):
'''
year = int(input("Enter a year:"))
if year%4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
'''
'''
modulus = number % 4
floor_division = number // 4

'''

#Task 2 (2nd way):
'''
year = int(input("Enter a year: "))
if year%4 == 0:
    print('year {} is a leap year'.format(year))
else:
    print('year {} is not a leap year'.format(year)) 
    # Với format là thứ truyền biến vào trong string
'''

#Task3:
'''
num = int(input("Enter a number: "))
counter = 0
for i in range (2,num):
    if num%i == 0:
        counter +=1
if counter == 0:
    print('{} is a primative'.format(num))
else:
    print('{} is not a primative'.format(num))
'''

#Task4:
'''
for num in range(1,21,1):
    print(num)
'''

#Task5:
'''
for num in range(2,21,2):
   print(num)
'''


#Task6:
'''
counter = 1
for num in range(20,0,-1):
    true = num%2
    while true == 0:
        print(num)
        break
'''

#Task7:
# '''
number = int(input("Enter a number: "))
loop = True
counter = 0
while loop:
    number = number // 10
    counter +=1
    if number == 0:
        loop = False
print('Số trên có {} chữ số'.format(counter))
# '''

#Task8:
'''
loop = True
set1 = 1
set2 = 100
while loop:
    num = (set1 + set2)//2
    print('Có phải số {} này không?'.format(num))
    ans = input('Enter your answer:')
    if ans == 'c':
        print('Đấy bố đoán đúng mà :)')
        break
    elif ans == "l":
        # print('hey')
        set1 = num
    elif ans == "s":
        set2 = num
'''








