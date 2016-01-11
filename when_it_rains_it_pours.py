import itertools
def answer(heights):

    peak = max(heights)
    water = [peak - i for i in heights]
    left, right = peak - heights[0], peak - heights[-1]    
    water = [list(g) for k,g in itertools.groupby(water, lambda x:x in [0]) if not k]
    if(right == 0):
        water.append([0])
    total, index, last_col_min = 0, 0, 0
    first_col_min = min(water[0])

    for i in water:        
        min_val = min(i)
        if(len(water) > 2 and index > 0 and index < len(water)-1):
            total = total + sum(i)
        else:
            i = [v - min_val for v in i ]
            total = total + sum(i)
        index+=1
    last_col_min = min_val    
    left = left - first_col_min if left - first_col_min > 0 else 0
    right = right - last_col_min if right - last_col_min > 0 else 0
    total = total - left - right

    return total
