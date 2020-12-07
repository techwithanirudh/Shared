# Word {len('word')}
# num = f"{len('Always')}{len('Help')}{len('The')}{len('Needy')}"
num = f"{len('Hello')}{len('am')}{len('am')}{len('I')}"

try:
    if not int(num) > 1:
        raise ValueError()
except ValueError:
    raise ValueError()

print('\n', ' ' * 35, 'Enrichment Acitvity', '\n')
print('Number of letters in each word -', num)
digits = list(num)

def gen_permutations(outcomes, length):
        ans = set([()])
        index = 0

        for _ in range(length):
            temp = set()
            for seq in ans: 
                for item in outcomes:
                    new_seq = list(seq)
                    if len(outcomes) == 1 or item in new_seq:
                        continue
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
            ans = temp
            print(ans)

        if not temp:
            ans = '('

            for _ in range(len(outcomes) - 1):
                ans += outcomes[index] + ', '
                index += 1
        
            ans = set([ans + outcomes[index] + ')'])

        print(ans)
        return ans

values = list(gen_permutations(digits, len(num)))
print(values)
max = str(max(values)).replace('(', '').replace(')', '').replace(', ', '').replace('\'', '')
min = str(min(values)).replace('(', '').replace(')', '').replace(', ', '').replace('\'', '')
sum = str(int(min) + int(max))
print('Greatest number -', max)
print('Smallest number -', min)
print()

header = ['H', 'Th', 'O', 'T']
maxL = []
minL = []
sumL = []
index = 0

for number in max:
    maxL.append(number)

for number in min:
    minL.append(number)

for number in sum:
    sumL.append(number)

print('|', end='')

for _ in range(len(maxL)):
    print(header[index], end='|')
    index -= 1

index = 0
print(' ' * 50)
print('|', end='')

for _ in range(len(maxL)):
    print(maxL[index], end='|')
    index += 1

index = 0
print(' ' * 50)
print('|', end='')

for _ in range(len(minL)):
    print(minL[index], end='|')
    index += 1

print(' ' * 50)
print('-' * int(len(minL) + len(minL) + 1))
print('|', end='')
index = 0

for _ in range(len(minL)):
    print(sumL[index], end='|')
    index += 1

print()