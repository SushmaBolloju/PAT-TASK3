def distributing_mangoes(mangoes, ns):
    mangoes.sort()
    l = len(mangoes)
    start = 0
    end = start + ns - 1
    diff = mangoes[end] - mangoes[start]
    i = 1
    while i + ns - 1 < l:
        if mangoes[i + ns - 1] - mangoes[i] < diff:
            end = i + ns - 1
            start = i
            diff = mangoes[end] - mangoes[start]
        i = i + 1
    j = start
    while j <= end:
        print(mangoes[j])
        j += 1
    return diff


mangoes = [5, 7, 8, 3, 2, 6, 1, 9, 11, 10, 12]
number_students = 5
print("Least diff :", distributing_mangoes(mangoes, number_students))

