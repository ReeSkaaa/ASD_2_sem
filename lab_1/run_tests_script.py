import subprocess
import os


def run_1_lab_tests():
    "Функция для запуска тестов 1 лабы"
    tasks = ['1']
    for i in tasks:
        print(' ')
        print('######## lab_1', f'task{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', 'task1.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_1_lab_tests()
