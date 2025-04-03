import subprocess
import os


def run_1_lab_tests():
    "Функция для запуска тестов 4 лабы"
    tasks = ['3', '5', '6']
    for i in tasks:
        print(' ')
        print('######## lab_4', f'task{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests', f'task{i}.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_1_lab_tests()
