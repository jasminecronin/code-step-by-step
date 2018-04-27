def is_magic_square(lst):

    sum1 = 0
    if len(lst) == 0:
        return True
    for row in lst:
        if len(row) != len(lst):
            return False
			
    # Get initial sum
    for item in lst[0]:
        sum1 += item
		
	# Check sums of the rows
    for row in lst:
        sum2 = 0
        for item in row:
            sum2 += item
        if sum2 != sum1:
            return False
			
	# Check sums of the columns
    for i in range(len(lst)):
        sum2 = 0
        for row in lst:
            sum2 += row[i]
        if sum2 != sum1:
            return False
		
	# Check sum of first diagonal
    sum2 = 0	
    for i in range(len(lst)):
        sum2 += lst[i][i]
    if sum2 != sum1 :
        return False
			
	# Check sum of second diagonal
    sum2 = 0
    for i in range(len(lst)):
        sum2 += lst[i][-(i+1)]
    if sum2 != sum1:
        return False
			
    return True