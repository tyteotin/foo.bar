#Test.assert_equals(answer(10), 2)
#Test.assert_equals(answer(7), 4)
#Test.assert_equals(answer(24), 3)
#Test.assert_equals(answer(160), 2)
#Test.assert_equals(answer(133), 4)
#Test.assert_equals(answer(7215), 4)
#Test.assert_equals(answer(0), 0)
#Test.assert_equals(answer(1), 1)
#Test.assert_equals(answer(10000), 1)
#Test.assert_equals(answer(2), 2)
#Test.assert_equals(answer(3), 3)
#Test.assert_equals(answer(4), 1)
#Test.assert_equals(answer(5), 2)
#Test.assert_equals(answer(6), 3)
#Test.assert_equals(answer(8), 2)
#Test.assert_equals(answer(9), 1)

import math
# Find nearest perfect square < n. If it's different by 1, subtract from n.
# If the difference > 1, if n is odd, find next nearest perfect square that's odd, same for even.
# Subtract perfect square from n until remain is 0
def answer(n):
    remain = n
    count = 0
    while(remain > 0):
        base = math.floor(math.sqrt(remain))
        if(int(remain) & 1 == int(math.pow(base, 2)) & 1 or remain - math.pow(base, 2) == 1):
            gauge = math.pow(base, 2)
        else:
            gauge = math.pow(base-1, 2)
        remain = remain - gauge
        count+=1
    return count
