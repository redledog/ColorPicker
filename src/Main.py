from src import ScreenController
from src import ScreenManager
from src import main_screen

if __name__ == '__main__':
    mainScreen = main_screen
    screenMng = ScreenManager
    screenCon = ScreenController

    screenMng.init_screen(mainScreen)
    screenCon.show(mainScreen)
