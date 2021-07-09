import os


class Reader:

    def __init__(self, path):
        self.path = path
        self.f = open(self.path, 'r+')

    def read(self):
        self.f = open(self.path, 'r+')
        return self.f.readlines()

    def write(self, string):
        self.f = open(self.path, 'w+')
        self.f.write(string)

    def __add__(self, other):
        a = self.read()
        b = other.read()
        self.write(a + b)

    def __str__(self):
        return f'{os.path.abspath(self.path)}'

    def __iter__(self):
        return self

    # def __next__(self):
    #     rez = self.f.readlines()[a]
    #
    #     return rez


file = Reader('out.txt')
file1 = Reader('out1.txt')




