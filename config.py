import os

basedir = os.path.abspath(os.path.dirname(__file__)) # в переменной __file__  дежит имя файла

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '.', 'cows.db')
# если в (basedir, '.', 'cows.db') проставить две точки, то
#база данных будет создана на директорию выше и вероятно и запись данный тоже
# будет производится в базу выше