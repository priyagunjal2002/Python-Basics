# print("hello world !");


# Taking input from user
str1=input("Enter input\n");
print(type(str1));
print(str1);


# String methods
message="Hello ,Guys"
print(message)
print(message.upper())
print(message.lower())

print(message.find('l'))
print(message.count('l'))


# string formatting
Greeting="Hello"
name="Priya"

# message='{},{}'.format(Greeting,name)
message=f'{Greeting},{name}'
print(message)

# concatenate
greeting="Hello"
name="Priya"

message =greeting + ' ' + name
print( message)