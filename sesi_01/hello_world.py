print('Python Introduction')

# ? string
print("hello world")
print(type("10"))

# ? number
print(123 + 1)
print(type(10))

# ? float
print(4.2e-4)
print(type(4.2e-4))

# ? boolean
print(True)
print(type(True))

print(1>2)
print(type(1>2))

# ? variable assignment
n = 300
print(n)

a = b = c = 300
print(a, b, c)

name = "Hacktiv8"
age = 54
has_laptops = True
print(name, age, has_laptops)

# ? aritmathic
a = 4
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #*floor division
print(a%b)
print(a**b) #*pangkat

# ? comparison
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

# ? string manipulation

s = 'foo'
t = 'bar'
# + and * Operators
print(s + t )
print(s * 4)
# Case Conversion
print(s.capitalize())
print(s.lower())
print(s.swapcase())

# ? python list
a = ['foo', 'bar', 'baz', 'qux']
print(a)


a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

#  ? tuples

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])
# * ini error karena tuples immutable
# // t[1] = 'foos'  

# packing and unpacking
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
print(s1)

# ? dictionary

MLB_team = {    
    'Colorado': 'Rockies',    
    'Boston': 'Red Sox',    
    'Minnesota': 'Twins',
}
print(MLB_team['Minnesota'])
#Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)

person = {}
person['fname'] = 'Hack'
person['lname'] = '8'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])
