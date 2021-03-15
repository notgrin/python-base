# O(N) столько памяти на кажды элемент

# g = range(10)
# print(g, type(g))
#
# for i in g:
#     print(i)
#
# # ------------------#
# def gen_odd_number(limit):
#     number = 1
#     while number < limit:
#         yield number    # генератор
#         # number += 2
#         number += number
#
#
# values = list(gen_odd_number(1000))
# print(values)

# -------------------------
# g1 = gen_odd_number()   # генераторы друг другу не мешают
# g2 = gen_odd_number()
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g2))
# print(next(g1))
# print(next(g2))

# g = gen_odd_number()

# values = []

# try:
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
#     values.append(next(g))
# except StopIteration:
#     pass
#
# print(values)


# for i in g:
#     print(i)

# values = []
# for i in range(5):
#     values.append(2 ** i)
#
# print(values)
# ---------------------------
#
# def gen_round(lst, limit=10):
#     counter = 0
#     while True:
#         for i in lst:
#             if counter >= limit:
#                 return
#             yield i
#             counter += 1
#
#
# for i in gen_round([1, 2, 3, 4, 5, 6], 100):
#     print(i)
# ---------------------------
# list comprehensions
#
# values = []
# for i in range(1, 21):
#     values.append(i*i)
#
# print(values)
#
# values = [i*i for i in range(1, 21) if (i+1) % 3 == 0]
# print(values)

# -------------------
# dict comprehensions
# names = ['Varkashia', 'Peter', 'Masha', 'Ann']
# values = {name: len(name) for name in names}
# print(values)
#
# values = {name[0]: name for name in names}
# print(values)

# -------------------
# множества (set comprehensions)
new_set = {1, 2, 3, 4, 5, 'A'}

names = ['Varvara', 'Peter', 'Mary', 'Ann']
new_set2 = {name[0] for name in names}
print(new_set2)

new_set3 = set([1, 2, 3, 4])    # {1, 2, 3, 4, 5}
print(new_set3)

lst = [1, 2, 3, 4, 1, 2, 4]
new_set4 = set(lst)
print(new_set4)
print(new_set - new_set4)
print(new_set2 - new_set4)
print(new_set2 | new_set)
print(new_set2 & new_set)