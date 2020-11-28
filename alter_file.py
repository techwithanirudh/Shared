def alter_file(inputFile='input.py', outputFile='output.py', replace={'\t': '    '}):
    '''
    This function will alter a file.

    These are the parameters needed.

    1. InputFile is the file name of which you want to change. 

    2. OutputFile is the file name which is changed after replacing data. 

    3. Replace is the data to be replaced. 
    '''
    index = -1

    try:
        open(inputFile)
    except FileNotFoundError:
        fileName = list(inputFile.split('\\'))
        fileName = str(fileName[len(fileName) - 1])
        raise FileNotFoundError('There is no such file named as ' + fileName)

    for _ in range(len(replace)):
        index += 1
        with open(inputFile, 'r') as source:
            with open(outputFile, 'a+') as result:
                result.truncate(0)
                for line in source:
                    line = line.replace(list(replace.keys())[index], list(replace.values())[index])
                    result.write(line)

if __name__ == '__main__':
    import os

    alter_file(str(os.path.dirname(__file__)) + '\\' + 'alter_file.py', str(os.path.dirname(__file__)) + '\\' + 'alter_file.txt')