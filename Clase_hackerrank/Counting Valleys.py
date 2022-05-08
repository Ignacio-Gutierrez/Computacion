def countingValleys(steps, path):

    valley = 0
    actual_level = 0
    
    for step in path:
        if step == 'D':
            actual_level -= 1
        else:
            actual_level += 1
            if actual_level == 0:
                valley += 1
    return valley