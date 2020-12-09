from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(receiver, response):
    while True:
        msg = receiver.recv()
        print(f'Process {getpid()} got message : {msg}')
        sleep(2)
        receiver.send(response)


if __name__ == "__main__":
    ping, pong = Pipe()
    Process(target=ponger, args=(ping, 'Pong')).start()
    Process(target=ponger, args=(pong, 'Ping')).start()
    pong.send('Ping')
