# Learning_Practicing List Comprehension https://youtu.be/SNq4C988FjU
# Developer Angela Tackett              12/26/2022

fruits = ['apples', 'bananas', 'strawberries']

# Not using list comprehension (Append Method)
new_fruits = []

for fruit in fruits:
   fruit = fruit.upper()
   new_fruits.append(fruit)

fruits = new_fruits
print(fruits)

# List comprehension
fruits = ['apples', 'bananas', 'strawberries']
fruits = [fruit.upper() for fruit in fruits]       
print(fruits)

# **************************************************
# old append method .append()

bits = [False, True, False, False, True, False, False, True]

new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

print(bits)
print(new_bits)


# list comprehension
super_bits = [1 if b == True else 0 for b in bits]
scott_trick = [1 if b else 0 for b in bits]

# print(super_bits)
print(scott_trick)


# # *****************************************************
# String to list Example
my_string = "HelloMyNameIsAngela"

# Turn string into list
my_string = [i for i in my_string]
print(my_string)

# Join to bring characters back together
my_string = "".join(
        [i for i in my_string]
        )
print(my_string)

# Space between each word
my_string = "".join(
    [i if i.islower() else " " + i for i in my_string]
)[1:]                     # slice first space from first word
print(my_string)