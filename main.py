from ast import IsNot
import datetime
import time
import git
from colorama import Fore, Back, Style


class AutoSave:
    def __init__(self):
        self.loop_task()

    def loop_task(self):
        path = self.input_path()

        while True:
            print(Fore.GREEN + 'start loop')
            try:
                result = self.save_code(path)
                if not result:
                    print(Fore.RED + 'path is error')
            except BaseException as e:
                pass
            time.sleep(10)

    def input_path(self):
        path = input(Fore.YELLOW + "Please input program path:")
        if not path:
            print(Fore.YELLOW + 'path is empty')
            return self.input_path()

        return path

    def save_code(self, path):

        try:
            repo = git.cmd.Git(path)

        except BaseException as e:
            print(Fore.RED + 'path error')
            return False
        try:
            repo.add('.')
        except BaseException as e:
            print(Fore.YELLOW + 'nothing to add')
            pass
        try:
            repo.commit('-m update')
        except BaseException as e:
            print(Fore.YELLOW + 'nothing to commit')
            pass
        repo.push()
        print(Fore.GREEN + 'push over')
        return True


if __name__ == '__main__':
    AutoSave()
