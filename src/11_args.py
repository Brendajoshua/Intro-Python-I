# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(n1, n2):
    return n1 + n2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*args):
  total = 0
  for n in args:
    if isinstance(n, (list, tuple)):
      for v in n:
        total += v
    else:
      total += n
  return total

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
'''
We may use tuple(a) to convert the list to tuples, while the leading * spills the contents as arguments into the function
like so: f2(*tuple(a))
https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/
However, we can also easily use f2(*a)
'''

print(f2(a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(n1, n2=1):
  return f2(n1, n2)

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(l = [], **kwargs):
  if len(l) > 0:
    kwargs['__list__'] = l
  for k, v in kwargs.items():
    if isinstance(v, dict):
      print(f"key: {k}, value: dict(")
      for k1, v1 in v.items():
        print(f"  key: {k1}, value: {v1}")
      print(")")
    else:
      print(f"key: {k}, value: {v}")

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
'''
change it to a keyword argument by adding two asteriks before the variable like so **d
'''
f4(**d)
