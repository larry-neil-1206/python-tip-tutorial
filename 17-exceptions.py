try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
except Exception as e:
  print('An Exception occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")
    
    
try:
  number = int('not a number')
except IOError as e:
  print('An IOError occurred. {}'.format(e.args[-1]))
except Exception as e: # ValueError
  print('An Exception occurred. {}'.format(e.args[-1]))
else:
  # any code that should only run if no exception occurs in the try,
  # but for which exceptions should NOT be caught
  print('This would only run if no exception occurs. And an error here '
        'would NOT be caught.')
finally:
  print("This would be printed whether or not an exception occurred!")