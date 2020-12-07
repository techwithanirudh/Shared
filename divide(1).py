type1 = False
dividend = 15
divisor = 3
howTo = True
ans = 0

if type1:
    minus = dividend
    while True:
        ans += 1
        if howTo:
            print(f'Sum: {minus} - {divisor} = {minus - divisor} Count: {ans}')
        minus = minus - divisor
        if minus < 1:
            break

    print('Answer:', ans)

if not type1:
    while True:
        ans += 1
        ansT = divisor * ans
        if howTo:
            print(f'Sum: {divisor} x {ans} = {ansT}')
        if ansT == dividend:
            break
    print('Answer:', ans)
