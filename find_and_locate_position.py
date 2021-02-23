numbers = list(map(int, input().split()))
number = int(input())

positions = []
count = 0
for n in numbers:
    if n == number:
        positions.append(count)
        count += 1
    else:
        count += 1
if len(positions) == 0:
    print("Отсутствует")
else:
    print(*positions)
