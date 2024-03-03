calculating = True
starting_val = 999

while calculating:
    goal = 1
    for digit in str(starting_val):
        goal *= int(digit)

    if goal > 9:
        starting_val = goal
    else:
        calculating = False
        print(goal)


# while calculating:
#     goal = 1
#     digit_list = [int(digit) for digit in str(starting_val)]
#     result_tuple = tuple(digit_list)
#
#     for i in range(len(result_tuple)):
#         goal = result_tuple[i] * goal
#     if goal > 9:
#         starting_val = goal
#     else:
#         calculating = False
#         print(goal)
