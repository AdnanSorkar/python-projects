from analyzer import average, maximum, minimum, stdGrade, totalPassed

stdList = []
std = 0

while True:
    print("Enter students' numbers / type 'exit' : ")
    stdNum = input(f"Enter #{std + 1} student's number: ").strip()

    if stdNum.lower() == "exit":
        break

    if not stdNum:
        print("Empty input. Try again.")
        continue

    try:
        stdNum = float(stdNum)
    except ValueError:
        print("Give a number. Try again.")
        continue

    if stdNum < 0 or stdNum > 100:
        print("Mark must be between 0 and 100. Try again.")
        continue

    stdList.append(stdNum)
    std += 1

if not stdList:
    print("\nNo student marks were entered.")
else:
    avr = average(stdList)
    highest = maximum(stdList)
    lowest = minimum(stdList)
    passed = totalPassed(stdList)
    passedPer = round((passed / len(stdList)) * 100, 2)

    print("\nAverage:", avr)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Total passed:", passed)
    print("Passed percentage:", passedPer, "%")

    print(f"\nFinal Report of {len(stdList)} student(s):")
    for i in range(len(stdList)):
        grade = stdGrade(stdList[i])
        print(f"Student #{i + 1}: {stdList[i]} -> Grade: {grade}")

print()