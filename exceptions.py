a = 5

try:
    print("a is: " + str(a))
    print(a/2)
except TypeError as e:
    print('Error happened')
except ZeroDivisionError as e:
    print('We can not divide into 0')
else:
    print('No error')
finally:  