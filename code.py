def are_valid_groups(student, groups):

    for x in groups:

        if len(x) != 2 and len(x) != 3:

            return False

    for y in student:

        counter = 0

        for x in groups:

            if y in x:

                counter += 1

        if counter != 1:

            return False

    return True
