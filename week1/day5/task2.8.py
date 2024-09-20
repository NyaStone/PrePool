print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))
# lambda is a function to determine if the number is greater than 10 (returns boolean)
# filter will run that function to determine which items to filter to keep while filtering
# list is used to get it back to a list type