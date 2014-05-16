import sys
import copy

change_units = (1,5,10,25,50)
# change_units = (50,25,10,5,1)

def sum_change(change_list):
    sum = 0
    for idx, n_coins in enumerate(change_list):
        sum += change_units[idx] * n_coins
    return sum

cache = {}
def break_change_wrapper(n_cents):
    change = set([])
    def break_change(n_cents,
                     curr_change = [0]*len(change_units)):
        if n_cents < 0:
            return

        if n_cents == 0:
            change.add(tuple(curr_change))
            return

        curr_change_sum = sum_change(curr_change)
        if not cache.has_key(curr_change_sum):
            cache[curr_change_sum]= break_change_wrapper(curr_change_sum)

        remainder = abs(n_cents - curr_change_sum)
        if remainder < n_cents and (not cache.has_key(remainder)):
            cache[remainder]= break_change_wrapper(remainder)

        if cache.has_key(n_cents):
            remainder_change = cache[n_cents]
            for a_remainder in remainder_change:
                change.add(tuple(sum(x) for x in zip(a_remainder, curr_change)))
            return


        for idx, coin in enumerate(change_units):
            this_curr = copy.copy(curr_change)
            this_curr[idx] += 1
            break_change(n_cents - coin,
                         curr_change = this_curr)

    break_change(n_cents)
    return change

if __name__=='__main__':
    print 'Number of ways to break', sys.argv[1], 'cents:', len(break_change_wrapper(int(sys.argv[1])))
