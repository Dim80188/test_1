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

