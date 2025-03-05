import subprocess
import os


def run_1_lab_tasks():
    "Функция для запуска заданий 1 лабы"
    tasks = ['1', '2', '5', '6', '15']
    for i in tasks:
        print(' ')
        print('######## Lab_1', f'Task_{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tasks', f'task{i}', f'task_{i}.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_1_lab_tasks()
