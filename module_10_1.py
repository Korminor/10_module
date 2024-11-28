import time
import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.datetime.now()
result_funk = time_stop - time_start
print(f'Время работы функции {result_funk}')

time_start = datetime.datetime.now()

th1 = Thread(target = write_words(10, 'example5.txt'))
th2 = Thread(target = write_words(30, 'example6.txt'))
th3 = Thread(target = write_words(200, 'example7.txt'))
th4 = Thread(target = write_words(100, 'example8.txt'))

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

time_stop = datetime.datetime.now()
result_thread = time_stop - time_start
print(f'Работа потоков {result_thread}')

print(f'Разница во времени: потоки быстрее функции на {result_funk - result_thread}')