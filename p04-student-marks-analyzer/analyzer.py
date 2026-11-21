def average(stdList):
    if not stdList:
        return None # It will not divide by 0
    avr = round(sum(stdList) / len(stdList), 2)
    return avr

def stdInfo(stdNum, std, highest, lowest):
    if (max < stdNum):
        max = stdNum
    print(f"Highest mark of #{std + 1} student: {max}")
    
    if (min > stdNum):
            min = stdNum
    print(f"Lowest mark of #{std + 1} student: {min}")
    
    
    
def stdGrade(stdNum):
    if stdNum >= 80:
        print("A")