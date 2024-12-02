import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        people = 100
        day = 0
        while people > 0:
            people -= self.power
            day += 1
            if people < self.power:
                people = 0
            print(f'{self.name}, сражается {day} день(дня)..., осталось {people} воинов.')
            time.sleep(1)
        print(f'{self.name}, одержал победу спустя {day} дней(дня)!')
        print(f'Все битвы закончились!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()


