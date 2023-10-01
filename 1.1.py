#Question:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Solution:

# You can determine if a string has all unique characters by using a simple algorithm 
# that doesn't use additional data structures. One way to do this is to sort the string 
# and then check if adjacent characters are the same.

def has_unique_chars(string):
    string = sorted(string)
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

#the time complexity of this algorithm is O(n log n) because of the sorting step.

# Another way to do this is to use a hash table. We can first initialize a hash table
# with all characters set to false. Then we can iterate through the string and set each
# character to true. If we ever encounter a character that is already true, we know the
# string has duplicate characters.

def has_unique_chars(string):
    hash_table = {}
    for char in string:
        if char in hash_table:
            return False
        else:
            hash_table[char] = True
    return True

# The time complexity of this algorithm is O(n) because we iterate through the string

print(has_unique_chars("hello")) # False
print(has_unique_chars("helo")) # True