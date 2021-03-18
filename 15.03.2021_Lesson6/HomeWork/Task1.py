"""
1. Не используя библиотеки для парсинга, распарсить
 (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
 — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
  Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""
a = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        remote_addr = line.split(' - - [')[0]
        # request_type = line.split('] "')[1].split(' /downloads/product_')[0]
        requested_resource = line.split(' +0000] "')[1].split(' HTTP/1.1" ')[0].split()
        b = (remote_addr, requested_resource[0], requested_resource[1])
        a.append(b)
    print(a)