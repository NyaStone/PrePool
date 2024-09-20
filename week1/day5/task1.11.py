my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list.extend( my_second_list )

my_third_list = [7 , 8 , 9]
my_fourth_list = [4 , 5 , 6]
my_fifth_list = [* my_third_list , * my_fourth_list ]

print(my_first_list)
print(my_fifth_list)
print(my_third_list)

