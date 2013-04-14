from math import sqrt, floor, ceil
import itertools


def fair_pals_up_to_digit(digit_num):
    pals = [1, 2, 3]
    for d in range(2, digit_num + 1):
        pals = pals + fair_pals_start_with_one(d) + fair_pals_start_with_two(d)
    return pals


def fair_pals_start_with_one(k):
    def fair_filter(num):
        sq = num * num
        return str(sq) == str(sq)[::-1]

    x = 1
    pals = [sum([n*(10**i) for i, n in enumerate(([x] + list(ys) + [z] + list(ys)[::-1]+[x]) if k % 2
            else ([x] + list(ys) + list(ys)[::-1] + [x]))])
            for ys in itertools.product(range(2), repeat=k/2-1)
            for z in (range(3) if k % 2 else (None,))]
    return filter(fair_filter, pals)


def fair_pals_start_with_two(digit_num):
    pals = []
    pal = int("2%s2" % ('0'*(digit_num-2)))
    pals.append(pal)
    if digit_num % 2 != 0:
        pal = int("2%s1%s2" % ('0'*(digit_num/2-1), '0'*(digit_num/2-1)))
        pals.append(pal)
    return pals


if __name__ == "__main__":
    f = open('3.in', 'r')
    o = open('3.out', 'w')

    #  first generate all fair square numbers up to 20 digits
    all_fair_pals = fair_pals_up_to_digit(20)

    T = int(f.readline().strip())

    for t in xrange(T):
        (A, B) = map(int, f.readline().strip().split(' '))
        fair_count = 0
        a = int(ceil(sqrt(A)))
        b = int(floor(sqrt(B)))
        fair_count = len([num for num in all_fair_pals if num >= a and num <= b])

        s = "Case #%s: %s\n" % (t + 1, fair_count)
        o.write(s)
