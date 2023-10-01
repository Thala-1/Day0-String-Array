#Write a method to replace all spaces in a string with '%20'.
#You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string.

#Example:
#Input: "Mr John Smith    ", 13
#Output: "Mr%20John%20Smith"

#Approach: Iterate through the string and replace all spaces with '%20'.
#           If the character is not a space, add it to the new string.
#           If the character is a space, add '%20' to the new string.
#           Return the new string.

#Time complexity: O(n) because we iterate through the string once.
#Space complexity: O(n) because we create a new string.

def replace_spaces(string, length):
    new_string=""
    for i in range(length):
        if string[i]==" ":
            new_string+="%20"
        else:
            new_string+=string[i]

    return new_string

print(replace_spaces("Mr John Smith    ", 13)) # Mr%20John%20Smith


