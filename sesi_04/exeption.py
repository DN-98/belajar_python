# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# x = 10
# if x > 5:
#     raise Exception('your custom exception')

import sys
# print(sys.platform)
# # assert ('linux' in sys.platform), "This code runs on Linux only."
# # assert ('windows' in sys.platform), "This code runs on Windows only."
# assert ('win32' in sys.platform), "This code runs on Windows only."


# TODO: The try and except Block: Handling Exceptions

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

# * try except

# -- example 1
# try:
#     os_interaction()
# except:
#     pass

# ? example 2
# try:
#     os_interaction()
# except:
#     print('Windows function was not executed')

# ? example 3
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
#     print('The os_interaction() function was not executed')


try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

try:
    os_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('os_interaction() function was not executed')

# TODO: The else Clause

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

# TODO: Cleaning Up After Using finally

# Have a look at the following example:

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')