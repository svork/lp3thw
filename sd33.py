# function write_stuff
def write_stuff(start, stop, step):
    numbers = []

    while start < stop:
        print(f"At the top i is {start}")
        numbers.append(start)

        start = start + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {start}")

    print("The numbers: ")

    for num in numbers:
        print(num)

write_stuff(0, 100, 10)
