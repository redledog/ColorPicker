import os


class Information:
    MAIN_SCREEN_WIDTH = 0
    MAIN_SCREEN_HEIGHT = 512
    MAIN_SCREEN_SIZE = [MAIN_SCREEN_WIDTH, MAIN_SCREEN_HEIGHT]
    ROOT_DIR = os.path.dirname(os.path.abspath('main.py'))
    IMG_PATH = os.path.join(ROOT_DIR, 'img')
