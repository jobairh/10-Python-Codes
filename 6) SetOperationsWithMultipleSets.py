# Example 6: Set Operations with Multiple Sets
# Performing Union, Intersection, and Symmetric Difference with Sets.

# Example Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 6, 7, 8}

# Performing Set Operations
union_result = set1 | set2 | set3
intersection_result = set1 & set2 & set3
symmetric_difference_result = set1 ^ set2 ^ set3

print('Union of sets:', union_result)
print('Intersection of Sets:', intersection_result)
print('Symmetric Difference of Sets:', symmetric_difference_result)