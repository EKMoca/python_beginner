falsy_values = [0, 0.0, 0j, {}, set(), (), [], False, None, list(range(0))]
for i in falsy_values:
    if i == False:
        print("This is a falsy value. ")
    else:
        print("This is truthy, my boy. ")