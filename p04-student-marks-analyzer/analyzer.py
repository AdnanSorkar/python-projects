def average(stdList):
    if not stdList:
        return None  # It will not divide by 0 (also has alt. method)
    return round(sum(stdList) / len(stdList), 2)

def maximum(stdList):
    try:
        return max(stdList)
    except ValueError:
        return None  # 1st (simpler) method

def minimum(stdList):
    if not stdList:
        return None
    return min(stdList)  # 2nd (alternative) method

def stdGrade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "Fail"