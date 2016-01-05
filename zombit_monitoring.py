#Test.assert_equals(answerA([[1, 2],[2, 6],[8, 10]]), 7)
#Test.assert_equals(answer([[1, 2],[2, 6],[3, 10]]), 9)
#Test.assert_equals(answer([[1, 3],[3, 6]]), 5)
#Test.assert_equals(answer([[10, 14],[4, 18],[19, 20],[19, 20],[13, 20]]), 16)

def answer(intervals):
	# Remove duplicate pairs
    intervals = [tuple(k) for k in intervals]
    intervals = [list(k) for k in set(intervals)]
	
	# Run through intervals and group overlapping time
    for i in intervals:
        idx = 0
        if(i != []):
            while(idx < len(intervals)):
                if(intervals[idx] != []):
                    start = intervals[idx][0]
                    end = intervals[idx][1]

                    if(start > i[0] and start < i[1]):
                        if(end > i[1]):
                            i[1] = end
                            intervals[idx] = []
                            idx = 0
                        else:
                            intervals[idx] = []
                            idx = 0
                    else:
                        idx += 1
                else:
                    idx += 1
	
	# No overlapping time, sum all groups for total time
    sum = 0
    for i in intervals:
        if(i != []):
            diff = i[1] - i[0]
            sum = sum + diff
    return sum     
