def calc_persentage(count):
    total = int(0)
    percentage = []
    for number in range(len(count)):
        total += int(count[number])
    for number in range(len(count)):
        calc = int(count[number]) / total
        percentage.append(round(calc * 100, 2))
    return percentage

