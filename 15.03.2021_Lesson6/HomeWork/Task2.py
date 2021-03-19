"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных
 им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов;
 код должен работать даже с файлами, размер которых превышает
  объем ОЗУ компьютера.
"""
lst = []
f = open('nginx_logs.txt', 'r', encoding='utf-8')
for line in f:
    line = line.strip()
    remote_addr = line.split(' - - [')[0]
    requested_resource = line.split(' +0000] "')[1].split(' HTTP/1.1" ')[0].split()
    b = (remote_addr, requested_resource[0], requested_resource[1])
    lst.append(b)
f.close()

clients_requests = {}
counter = 0
for i in lst:
    remote_address = i[0]
    clients_requests.setdefault(remote_address, []).append(counter)

spammer = max(clients_requests.items(), key=lambda k_v: k_v[1])
# не пойму почему key=lambda k_v: k_v[1] подобное выражение работает
print(f'IP спаммера: {spammer[0]}, кол-во запросов: {len(spammer[1])}')