#!/usr/bin/env python
"""For this problem, you are given N days of upvote count data, and a
fixed window size K. For each window of K days, from left to right,
find the number of non-decreasing subranges within the window minus
the number of non-increasing subranges within the window.
"""

(ndays, window_size) = map(int, raw_input().split())
upvotes = map(int, raw_input().split())

def diff_subranges(window):
    """By keeping track of the number of consecutive decreasing/increasing
    values and adding nconsec to the number of increasing/decreasing
    subranges, it's possible to loop through window only once.

    Returns ndec - ninc
    """
    ninc = 0
    ndec = 0
    ninc_consec = 0
    ndec_consec = 0
    for idx, curr in enumerate(window):
        if idx == 0:
            continue
        prev = window[idx-1]

        if curr > prev:
            if ndec_consec == 0:
                ndec_consec = 1
            else:
                ndec_consec += 1

            ninc_consec = 0
            ndec += ndec_consec
        elif curr < prev:
            if ninc_consec == 0:
                ninc_consec = 1
            else:
                ninc_consec += 1

            ndec_consec = 0
            ninc += ninc_consec
        else:
            if ninc_consec == 0:
                ninc_consec = 1
                ndec_consec += 1
            if ndec_consec == 0:
                ndec_consec = 1
                ninc_consec += 1
            ninc += ninc_consec
            ndec += ndec_consec

    return ndec - ninc


for day in range(ndays-window_size+1):
    print diff_subranges(upvotes[day:day+window_size])
