def minimumNumber(n, password):

    special_characters = "!@#$%^&*()-+"
    res = 0

    if any(x.isupper() for x in password) == False:
        res += 1
    if any(x.islower() for x in password) == False:
        res += 1
    if any(x.isdigit() for x in password) == False:
        res += 1
    if any(x in special_characters for x in password) == False:
        res += 1

    return max(res,6 - n)