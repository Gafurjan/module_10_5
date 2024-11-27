
from multiprocessing import Pool
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            st = file.readline()
            if not st:
                break
            all_data.append(st)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    big_time = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.datetime.now() - big_time
    print(f'Время выполнение программы по линейному: {end_time}')

    big_time = datetime.datetime.now()
    with Pool(4) as p:
        p.map(read_info, filenames)
    end_time = datetime.datetime.now() - big_time
    print(f'Время выполнение программы: {end_time}')


