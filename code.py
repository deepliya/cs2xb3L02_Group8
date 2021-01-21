def are_valid_groups(student, groups):

    for x in student:

        found = False

        for y in groups:

            if x in y:

                found = True

        if not found:

            return found

    return True
