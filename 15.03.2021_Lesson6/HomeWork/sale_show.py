import sys

if len(sys.argv) > 3:
    print('больше 2х параметров')
    exit(1)

try:
    start = int(sys.argv[1])-1 if len(sys.argv) > 1 else 0
    end = int(sys.argv[2])-1 if len(sys.argv) > 2 else None
    with open('sales.txt', 'r', encoding='utf8') as f:
        f.seek(11 * start)
        curline = start
        for line in f:
            if end is None or curline <= end:
                print(line, end='')
                curline += 1
            else:
                break

except ValueError:
    print('число должно быть целым и больше 1')


