# # import module
# from module import a as m_a
# from package import a as p_a
#
# # import package.module
# # from package.module import * #module_function, module_function1
#
# # print(module.calc_sum(1, 2, 3, 4, 5))
# # print(package.package_function())
# # print(package.module.module_function())
# # print(module_function())
# # print(package.module.module_function1())
# # print(package.module_function1())
#
# m_a()
# p_a()

# import requests
# # r = requests.get('https://www.python.org')
# r = requests.get('https://www.geekbrains.ru')
# # print(r.status_code, type(r), dir(r))
# print(r.status_code, r.content.decode('utf-8'))
# 200 - все хорошо
# 400+ - ошибка с запросом
# 500... - у сервера проблема, не может обработать

# import sys
#
# print('hello', sys.argv)

import time

start = time.perf_counter()
j = 0
for i in range(10000000):
    j += i
end = time.perf_counter()
print(end-start, start, end)

