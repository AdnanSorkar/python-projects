from analyzer import average, stdInfo, lowest, passedStd

stdList = []
std = 0
max = stdList[0]
min = stdList[0]
passed = 0
passRate = 1

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

print("Collected:", stdList)

print()