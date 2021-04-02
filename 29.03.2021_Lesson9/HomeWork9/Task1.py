"""
1. Создать класс TrafficLight (светофор).
определить у него один приватный атрибут color (цвет) и метод get_current_signal()
 (получить текущий цвет);
после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью:
 красный (3 сек), жёлтый (1 сек), зелёный (3 сек);
переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора
 с интервалом 0.5 секунды, используя метод get_current_signal().
"""
import time
from time import perf_counter


class TrafficLight:
    _color = ['красный', 'желтый', 'зеленый']

    def __str__(self):
        return self.get_current_signal()

    def get_current_signal(self):
        i = 0
        perf_counter()
        while True:
            print(f'цвет:')
            time.sleep(0.5)
            print(f'{TrafficLight._color[i % 3]}, {perf_counter()}')
            if i % 3 == 0:
                time.sleep(3)
            elif i % 3 == 1:
                time.sleep(1)
            elif i % 3 == 2:
                time.sleep(3)
            i += 1


k = TrafficLight()
k.get_current_signal()