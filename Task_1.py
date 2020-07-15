from time import sleep


class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


class TrafficLight(Colors):
    def __init__(self, color):
        self.__color = color

    def running(self):
        colors = ['red', 'yellow', 'green']
        if type(self.__color) is str:
            if self.__color in colors:
                while True:
                    for color in range(len(colors)):

                        try:
                            self.__color = colors[color + 1]
                            color = self.__color

                            if color == 'red':
                                print(f'{Colors.RED}{color}')
                                sleep(2)
                                continue
                            elif color == 'yellow':
                                print(f'{Colors.YELLOW}{color}')
                                sleep(2)
                                continue
                            elif color == 'green':
                                print(f'{Colors.GREEN}{color}')
                                sleep(2)
                                continue
                        except IndexError:
                            colors.reverse()
                            continue
            else:
                print('There is no color...')

        else:
            print('Wrong argument')


a = TrafficLight('red')
a.running()
