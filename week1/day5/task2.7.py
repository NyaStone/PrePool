print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
# for every number in the list, map x to either it's division by two if it was even
# or to the multiplication by two if the number was odd