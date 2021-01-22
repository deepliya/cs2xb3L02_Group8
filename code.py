def are_valid_groups(stdno, groups):
    for i in groups:
        if len(i) != 2 and len(i) != 3:
	    return False
    for j in student:
	counter = 0 
        for i in groups:
            if j in i:
                counter = counter + 1
    	if counter != len(stdno):
            return False
    return True
