def are_valid_groups(student_nums, groups_lst):
    counter = 0
    for i in groups_lst:
        for j in range(len(student_nums)):
            if student_nums[j] in i:
                counter += 1
    if counter != len(student_nums):
        return False
    return True
