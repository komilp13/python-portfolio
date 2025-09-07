'''
Lambda: small, one line anonymous function with input that returns an output
- typically used with higher order functions, which take other functions as arguments
'''

from functools import reduce

# define a anonymous function
add10 = lambda x: x + 10
print(f'output of add10: {add10(5)}')

# define additional parameters
multiply_func = lambda x, y: x * y
print(f'output of multiply_func: {multiply_func(2, 3)}')

# Sorted() - sorts a collection
points_2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_2d_sorted_def = sorted(points_2d)    # default sort is by first element
points_2d_sorted_by_y = sorted(points_2d, key=lambda p: p[1])   # sort by second element

print(f'        output of points_2d: {points_2d}')
print(f'     output of default sort: {points_2d_sorted_def}')
print(f'output of default sort by Y: {points_2d_sorted_by_y}')

# we can also sort the list by the total of the values
points_2d_sorted_sum = sorted(points_2d, key=lambda p: p[0] + p[1])
print(f'output of points_2d_sorted_sum: {points_2d_sorted_sum}')



# Map() - transforms each element using a function
# usage: map(func, seq)
list1 = [1, 2, 3, 4, 5]
list2 = map(lambda x: x ** 2, list1)
print(f'output of map(): {list(list2)}')



# Filter() - returns all elements where the func returns to True
# usage: filter(func, seq)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = filter(lambda x: x % 2 == 0, list1)
print(f'output of filter(): {list(evens)}')



# Reduce() - applies the function to all the elements & returns a single value
# usage: reduce(func, seq)
list1 = [1, 2, 3, 4, 5]
product_a = reduce(lambda x, y: x * y, list1)
print(f'output of reduce(): {product_a}')
