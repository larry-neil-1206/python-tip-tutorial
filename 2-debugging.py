'''
python -m pdb my_script.py

c: continue execution
w: shows the context of the current line it is executing.
a: print the argument list of the current function
s: Execute the current line and stop at the first possible occasion.
n: Continue execution until the next line in the current function is reached or it returns.
'''
import pdb
import logging

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())

# Configure the logging module to output diagnostic information
logging.basicConfig(filename='logfile.log', level=logging.WARNING)

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an informational message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error message')