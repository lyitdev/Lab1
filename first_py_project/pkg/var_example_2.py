#Python strings

choice = 'a'
str = "This is a long string with nothing to say"
paragraph = '''This is a very long string which can run over multiple lines if desired
 and can still contain single ' or double " quotes within it'''

print(str[0])#prints the first letter in the string
print(str[3:8])#print from index 3 to 8
print(str[8:])# print from index 8 to end
print(str[-1])#prints the last character in the string
print(str[-2])#print the 2nd last character in the string
print(str[-3])
len(str)
print("Student {0}, Age {1}".format(12345,21))
print("Student {0:7d}, Age {1}".format(12345,21)) # add leading zeros
print("Student {0:>10d}, Age {1}".format(12345,21)) # right align
print("Student {0:<10d}, Age {1}".format(12345,21)) # left align
print("Student {0:^10d}, Age {1}".format(12345,21)) # center
print("Footballer Wages {:9,.2f} euros".format(1234567)) # add comma's as appropriate
print("Footballer total matches {:4,d} ".format(12345)) # don't put a space after the comma!
print("\t"*2+"Title")

