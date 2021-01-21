def are_valid_groups(stdno, groups):
    counter = 0
    for i in groups:
        for j in range (len(stdno)):
            if stdno[j] in i:
                counter = counter + 1
    if counter != len(stdno):
        return False
    return True
