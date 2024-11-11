import random
import sortires # наш модуль
import time # модуль для замера времени
def times_for_N(N):

    Massiv = [random.randint(1,100000) for i in range(N)]
    start = time.time()
    # print(start)
    sortires.insertion_sort(Massiv)
    finish = time.time()
    # print(finish)

    Res_msec_ins = (finish - start)*1000*100//1/100

    Massiv = [random.randint(1,100000) for i in range(N)]
    start = time.time()
    sortires.bubble_sort(Massiv)
    finish = time.time()
    Res_msec_bub = (finish - start)*1000*100//1/100

    Massiv = [random.randint(1,100000) for i in range(N)]
    start = time.time()
    sortires.merge_sort(Massiv)
    finish = time.time()
    Res_msec_mer = (finish - start)*1000*100//1/100

    Massiv = [random.randint(1,100000) for i in range(N)]
    start = time.time()
    sortires.selection_sort(Massiv)
    finish = time.time()
    Res_msec_sel = (finish - start)*1000*100//1/100

    Massiv = [random.randint(1,100000) for i in range(N)]
    start = time.time()
    sortires.quick_sort(Massiv)
    finish = time.time()
    Res_msec_qui = (finish - start)*1000*100//1/100
    print(Res_msec_ins, Res_msec_bub, Res_msec_mer, Res_msec_sel, Res_msec_qui)
    return Res_msec_ins, Res_msec_bub, Res_msec_mer, Res_msec_sel, Res_msec_qui
for N in [10, 100, 1000, 10000, 100000]:
    print(N)
    times_for_N(N)
