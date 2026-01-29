start = int(input("Початок: "))
end = int(input("Кінець: "))

for i in range(start, end + 1):
    if i % 7 == 0:
        print(i)
