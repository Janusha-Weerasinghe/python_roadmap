#logical operators = evaluate multiple conditions (or, and not)
# or = at least on condition must be true
# and both conditions must be true
# not = inverts the condition (not false , not true)

temp = float(input ("Input the temp"))
is_raining = False

if temp > 35 or temp<0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")