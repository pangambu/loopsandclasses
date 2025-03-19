# Errors and Exceptions

try:
    a = 5/0  
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everything is fine')
finally:
    print('Cleaning up...')