type1 = True
dividend = 56
divisor = 9
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
