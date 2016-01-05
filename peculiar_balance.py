import math
def answer(x):
    pwr3List = [math.pow(3, i) for i in range(0, 20, 1)]
    powNum = math.floor(math.log(x, 3))
    right_scale = math.pow(3, powNum)
    idx = [i for i in range(0, 20, 1) if pwr3List[i] == right_scale]
    ix = idx[0]
	
	# If the sum of all previous power of 3 including the current power of 3 
	# is less than input, then the next power of 3 should be used
    if(x > sum(pwr3List[:(ix+1)])):
        right_scale = pwr3List[(ix+1)]
        ix +=1
        sliceIdx = ix
    
	# End index for resulting list
    ans = ["-" for i in range(0, ix+1, 1)]
    ans[ix] = "R"
    left_scale = x
	
	# Immediate matched
    if(left_scale == right_scale):
            ans[ix] = "R"
    else:
        while(left_scale != right_scale):
            # Difference of 1 can be balanced quickly
			if(left_scale - right_scale == 1):
                right_scale += pwr3List[0]
                ans[0] = "R"
            elif(right_scale - left_scale == 1):
                left_scale += pwr3List[0]
                ans[0] = "L"
        
            else:
		# If the difference between 2 scales is bigger than the sum of
		# all previous power of 3 including the current "weight" below, add the 
		# next power of 3 to the lighter scale. Keep overadding the 
		# lighter scale until difference is 1 or exact match
                diff = math.fabs(left_scale - right_scale)
                weight = math.pow(3, math.floor(math.log(diff, 3)))
                wIdx = [i for i in range(0, 20, 1) if pwr3List[i] == weight]
                wx = wIdx[0]

                if(diff > sum(pwr3List[:(wx+1)])):
                    weight = pwr3List[(wx+1)]
                    wx += 1
                
                if(left_scale > right_scale):
                    right_scale = right_scale + weight
                    ans[wx] = "R"
                elif(left_scale < right_scale):
                    left_scale = left_scale + weight
                    ans[wx] = "L"

    return ans    
