import math

def bytesToSize(_bytes):
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    if _bytes == 0:
        return '0 Byte';
    i = int(math.floor(math.log(_bytes) / math.log(1024)));
    if i > 8:
        while True:
            inp = input('Enter your own ?B: ').upper()
            conditions = [len(inp) == 2, inp.endswith('B'), inp != sizes[0], inp != sizes[1], inp != sizes[2], inp != sizes[3], inp != sizes[4], inp != sizes[5], inp != sizes[6], inp != sizes[7], inp != sizes[8]]
            print(conditions)
            if all(conditions):
                sizes.append(inp)
                i = 9
                break
    return str(round(_bytes / math.pow(1024, i), 2)) + ' ' + sizes[i];

print(bytesToSize(int(input('Bytes: '))))
