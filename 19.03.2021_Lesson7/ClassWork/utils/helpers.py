import os


def print_current_work_dir():
    print(os.path.curdir)
    print(os.path.abspath(os.path.curdir))


if __name__ == '__main__':
    print_current_work_dir()