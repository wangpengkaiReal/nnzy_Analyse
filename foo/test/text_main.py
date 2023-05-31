from foo import Analyes
from tool import doris


def text_run():
    # todo
    name = 'abc'
    values = (1,2,3,4,5)
    print(f'INSERT INTO %s VALUES ({"%s," * (len(values)-2) + "%s"})' % (name,values))
    print()


if __name__ == '__main__':
    text_run()
