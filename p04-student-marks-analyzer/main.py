from analyzer import average, maximum, minimum, stdGrade

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

    stdList.append(stdNum)
    std += 1

if not stdList:
    print("\nNo student marks were entered.")
else:
    avg = average(stdList)
    high = maximum(stdList)
    low = minimum(stdList)

    print("\nAverage:", round(avg, 2))
    print("Highest:", high)
    print("Lowest:", low)

    print("\n--- Final Report ---")
    for i in range(len(stdList)):
        grade = stdGrade(stdList[i])
        print(f"Student #{i + 1}: {stdList[i]} -> Grade: {grade}")

print()