#Given two strings, write a method to decide if one is a permutation of the other.

#Approach: Sort the strings and compare them. If they are equal, they are permutations of each other.   

def is_permutation(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        return True
    else:
        return False

# The time complexity of this algorithm is O(n log n) because of the sorting step.

# Solution 2: Use a hash table to count the number of times each character appears in each string. 
# If the hash tables are equal, the strings are permutations of each other.

# example:
# string1 = "hello"
# string2 = "elloh"
# hash_table1 = {"h": 1, "e": 1, "l": 2, "o": 1}
# hash_table2 = {"e": 1, "l": 2, "o": 1, "h": 1}   

def is_permutation(string1, string2):
    hash_table1 = {}
    hash_table2 = {}
    for char in string1:
        if char in hash_table1:
            hash_table1[char] += 1
        else:
            hash_table1[char] = 1
    for char in string2:
        if char in hash_table2:
            hash_table2[char] += 1
        else:
            hash_table2[char] = 1
    if hash_table1 == hash_table2:
        return True
    else:
        return False
    
# The time complexity of this algorithm is O(n) because we iterate through the strings once.

print(is_permutation("hello", "elloh")) # True
print(is_permutation("hello", "ello")) # False

