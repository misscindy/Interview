# Combination Sum


def combination_sum(candidates, target):
    candidates.sort()
    res = []
    _comb_sum(candidates, target, 0, [], 0, res)
    return res


def _comb_sum(cand, target, start, sofar, sofar_sum, result):
    print "_comb_sum( ", start, sofar, sofar_sum, result, ")"
    if sofar_sum == target:
        result.append(sofar[:])
        return

    for nxt_start in range(start, len(cand)):
        print "from : %i to %i"% (start, len(cand))
        if nxt_start != 0 and cand[nxt_start] == cand[nxt_start - 1]:
            continue

        # for ndx in range(nxt_start, len(cand)):
            # print "\tfrom : %i to %i"% (ndx, len(cand))
        temp_sum = cand[nxt_start] + sofar_sum
            # print temp_sum, cand[ndx], sofar_sum
        if temp_sum > target:
            break
        _comb_sum(cand, target, nxt_start, sofar + [cand[nxt_start]], temp_sum, result)
    print "==="

if __name__ == '__main__':
    print combination_sum([1, 2], 2)
