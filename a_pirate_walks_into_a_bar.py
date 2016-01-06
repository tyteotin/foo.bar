def answer(numbers):
    count = 0
    min_count = 0
    parley = False
	
	# Find a number that is less than its index, referring to earlier
	# number to its left. Mr.Gibbs will have the 'backward' referral
	# and will find the pirate that referred him. Mr.Gibbs then takes
	# that pirate's place and keeps doing so until Mr.Gibbs is his
	# 'backward' referral
    for i in range(0, len(numbers), 1):
        if(numbers[i] < i):
            count = 0
            mrGibbsRefer = numbers[i]
            mrGibbs = i
            j = i
			# Keep looking while the 'backward' referral is not Mr.Gibbs
			# and there's no guy that referred to Mr.Gibbs. If there is,
			# then parley between pirates is true, and Mr.Gibbs will take
			# that pirate's place
            while(j > 0 and numbers[j] != mrGibbs and j != mrGibbsRefer):
                parley = False
                j-= 1
                if(numbers[j] == mrGibbs):                   
                    mrGibbs = j
                    count+=1
                    parley = True
			
            if(j == mrGibbsRefer):
                if(numbers[j] == i):
                    return 2
				# Account for first loop encountered
                elif(min_count == 0 and parley == True):               
                    min_count = count + 1   
				# Account for subsequence smaller loop encountered
                elif(min_count > count and parley == True):
                    min_count = count + 1
    return min_count
