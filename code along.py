##type conversion
print(type(str(100)))

##escape sequence
## add \

weather= "It\'s \"kind of\" sunny"

print(weather)

# you can add a new line
weather= "It\'s \"kind of\" sunny \n hope you have a good day!"

print(weather)

##formated string - add f in the beginning

name = 'Timileyin'
Age = 32

print(f'Hi! {name}, you are {Age} year old today')

## string indexing

## variable[start:stop:stepover]
selfish = 'me me me'

print(selfish[:4:2])

#reverse order
print(selfish[::-1])

##immutability

#strings are immutable, you can reasign a new value to an index of a string


