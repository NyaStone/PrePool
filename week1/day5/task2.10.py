first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
magic = [* zip ( first_name , last_name [:: -1]) ] # zip is used to create a tupple  ([:: -1] just reverses the list before matching them)
print ( magic [0]) #prints the first tuple
print ( magic [3])
print ( magic [1][0]) #prints the first name of the second tuple
print ( magic [0][1]) #prints the last name of the first tuple
print ( magic [2])
