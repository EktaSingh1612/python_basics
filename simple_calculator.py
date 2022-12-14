num1 = float(input('1st number:'))
num2 = float(input('2nd number:'))
print(
  'Enter 1 for addition \n 2 for substraction \n 3 for multiplication \n 4 for division'
)
entered_num = int(input('any num between 1 to 4: '))

if entered_num==1:
  print('addtion of 1st num is:', num1+num2)
elif entered_num==2:
  print('subtraction of 1st num is:', num1-num2)
elif entered_num==3:
  print('multiplication of 1st num is:', num1*num2)
elif entered_num==4:
  print('division of 1st num is:', num1/num2)
else:
  print('invalid input')