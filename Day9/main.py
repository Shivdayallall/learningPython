#Dictionaries allows you to group related data together. Using key and value.
programming_dictionary = {
    "bug": "an error that prevents code from running correctly",
    "function": "Blocks of code you can invoke",
}
#Retrieving an item
print(programming_dictionary["bug"])

#Adding an item
programming_dictionary["loop"] = "concept to run a task repeatedly"

#Edit item
programming_dictionary["bug"] = "A nice butterfly"

#Clear out the dictionary
#programming_dictionary = {}

#Iterate over a dictionary
for key in programming_dictionary:
    #print the key in the dictionary
    print(key)

    #print the value using the current key
    print(programming_dictionary[key])