import sys

if len(sys.argv) != 2:
    print('перезадайте сумму продаж')
    exit(1)

with open('sales.txt', 'a', encoding='utf8') as f:
    print(f'{sys.argv[1]:10}', file=f)