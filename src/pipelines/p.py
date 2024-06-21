import sys
import os

# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

sys.path.append(
    os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)))

print (os.getcwd())

# In the root directory of the project:
# sys.path.append('./src') # WORKING
# sys.path.append('src') # WORKING
# sys.path.append('/src') # NOT WORKING

# In the src directory of the project:
# NONE OF THE ABOVE WORKS
# sys.path.append('.') # WORKING
# sys.path.append('./') # WORKING
# sys.path.append('/') # NOT WORKING

# print the formatted variable: `sys.path`:
print('-------- sys.path --------')
print('\n'.join(sys.path))
print('-------- sys.path --------')

from my_modules import m


def p():
    m.foo()
    print('p')


p()
