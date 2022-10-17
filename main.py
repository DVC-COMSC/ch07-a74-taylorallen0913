

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))

if delval not in numbers:
    numbers.clear()
else:
    while True:
        try:
            numbers.remove(delval)
        except:
            break

print(numbers)
