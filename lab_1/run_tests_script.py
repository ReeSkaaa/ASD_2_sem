import subprocess
import os


def run_1_lab_tests():
    "Функция для запуска тестов 1 лабы"
    tasks = ['1', '3', '4', '5', '6', '8', '9']
    for i in tasks:
        print(' ')
        print('######## Lab_1', f'Task_{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'tests', 'test.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_1_lab_tests()