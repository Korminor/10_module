import multiprocessing
from datetime import datetime
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as file:
        date = file.readline()
        while date:
            date = file.readline()
            all_data.append(date[0:-1])
filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
start = datetime.now()
read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])
finish = datetime.now()
print(f' Линейный {finish - start}')
# Многопроцессный
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    finish = datetime.now()
    print(f' Многопроцессный {finish - start}')
