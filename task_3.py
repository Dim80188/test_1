def appearance(intervals):
    lesson_1 = intervals[0]['data']['lesson']
    pupil_1 = intervals[0]['data']['pupil']
    tutor_1 = intervals[0]['data']['tutor']
    pupil_2 = get_many_list(pupil_1)
    tutor_2 = get_many_list(tutor_1)
    start = lesson_1[0]
    finish = lesson_1[1]
    m = 0
    st_list = []

    while start <= finish:
        for i in pupil_2:
            if i[0] != i[1]:
                if i[0] < start <= i[1]:
                    for j in tutor_2:
                        if j[0] != j[1]:
                            if j[0] < start <= j[1]:
                                if start not in st_list:

                                    m += 1
                                    st_list.append(start)

        start += 1


    return m

def get_many_list(list_1):
    list_2 =[]
    n = 0
    while n < len(list_1):
        a = [list_1[n], list_1[n + 1]]
        list_2.append(a)
        n += 2
    return list_2

print(appearance([
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]


},
     }
]))