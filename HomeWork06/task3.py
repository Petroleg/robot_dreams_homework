# використати built-in функцію

collection = [i for i in range(1, 999999)]
the_greatest_number = max(collection)


# створити свою функцію
def maximum(numbers):
    biggest_number = 0
    for number in numbers:
        if number > biggest_number:
            biggest_number = number
    return biggest_number


# використати лямбда функцію

# Need your comments on the details of this task as far as I'm not sure whether my solution is correct, and I've got the
#  general point of this task. First thought about using a for loop in a lambda function to iterate over each element in
#  collection and further to compare it with some variable (same as in the above-shown "maximum" function), but in one
# line lambda function, but discovered that we can't use "for" statement in lambda, so the only way I see here to solve
# this task is to use my "maximum" function or built-in "max" function. Please let me know if there is more true python
# solution to this exercise. The point is that we are trying to figure out the greater value inside a collection, so we
# have to iterate. I can't see the possibility to reproduce lambda a, b: a if a > b else b over the iterable.

maximum_lambda = lambda some_collection, some_function: some_function(some_collection)

max_lambda = lambda some_collection: max(some_collection)

# later on I have found such a lambda function, but it uses recursion, so it just blows my mind...
# moreover it takes a lot of time to run this code, so it won't execute for long collections, but it works ok with
# short one

f = lambda l: l[0] if len(l) == 1 else l[0] if l[0] > f(l[1:]) else f(l[1:])
