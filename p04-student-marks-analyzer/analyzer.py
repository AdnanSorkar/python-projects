def average(stdList):
    if not stdList:
        return None  # It will not divide by 0 (also has alt. method)
    avr = round(sum(stdList) / len(stdList), 2)
    return avr


def maximum(stdList):
    try:
        return max(stdList)
    except ValueError:
        return None  # 1st (simpler) method


def minimum(stdList):
    if not stdList:
        return None
    return min(stdList)  # 2nd (alternative) method


def stdGrade(num):
    if num >= 80:
        return "A"
    elif num >= 70:
        return "B"
    elif num >= 60:
        return "C"
    elif num >= 40:
        return "D"
    else:
        return "Fail"


def totalPassed(stdList):
    passed = 0
    for i in range(len(stdList)):
        if stdList[i] >= 40:
            passed = passed + 1
    return passed