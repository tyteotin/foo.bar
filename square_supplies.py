import math
def answer(n):
    remain = n
    count = 0
    
    # Find nearest perfect square < n. If it's different by 1, subtract from n.
    # If the difference > 1, if n is odd, find next nearest perfect square that's odd, same for even.
    # Subtract perfect square from n until remain is 0
    while(remain > 0):
        base = math.floor(math.sqrt(remain))
        if(int(remain) & 1 == int(math.pow(base, 2)) & 1 or base == 1 or remain - math.pow(base, 2) == 1):
           gauge = math.pow(base, 2)
        else:
            gauge = math.pow(base-1, 2)
        remain = remain - gauge
        count+=1
    return count
