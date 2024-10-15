import random
import time
from threading import Thread


class MyThread(Thread):

    def __init__(self, name):
        #Инициализация потока
        Thread.__init__(self)
        self.name = name

    def run(self):
        #Запуск потока
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)


def create_threads():
    #Создаем группу потоков
    for i in range(5):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name)
        my_thread.start()

create_threads()