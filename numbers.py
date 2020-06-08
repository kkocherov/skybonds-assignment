import fileinput

_, *numbers = fileinput.input()
fileinput.close()

numbers = list(map(float, numbers))
total = sum(numbers)

for number in numbers:
    print('{:.3f}'.format(float(number) / total))
