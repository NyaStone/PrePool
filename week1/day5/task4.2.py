mylist = ["a", "b", "a", "c", "c"]
mydict = dict.fromkeys(mylist) # converting the list into a dict forces the removal of duplicate keys
mylist = list(mydict) #and then convert it back
print(mylist)