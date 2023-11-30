from datetime import datetime


# class Logger:
#     _instance = None
#     _file_name = 'logs.log'
#
#     def __init__(self):
#         self._file = None
#         raise RuntimeError('Call instance() instead')
#
#     @classmethod
#     def instance(cls):
#         """It returns instance of our Logger"""
#         if cls._instance is None:
#             cls._instance = cls.__new__(cls)
#
#             cls._instance._file = open(cls._file_name, 'w')
#         return cls._instance
#
#     def write_log(self, message):
#         self._file.writelines(message + datetime.now() + '\n')
#
# logger = Logger.instance()
# logger2 = Logger().instance()
# logger3 = Logger().instance()
#
# print(id(logger))
# print(id(logger2))
# print(id(logger3))
#
# logger.write_log('HelloWorldddddddddd')
# logger2.write_log('dup[a')


# class Logger:
#     _instance = None
#     _file_name = 'logs.log'
#
#     def __new__(cls):
#         """It returns instance of our Logger"""
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#
#             cls._instance._file = open(cls._file_name, 'w')
#         return cls._instance
#
#     def write_log(self, message):
#         self._file.writelines(message + '\n')
#
# logger = Logger()
# logger2 = Logger()
# logger3 = Logger()
#
# print(id(logger))
# print(id(logger2))
# print(id(logger3))
#
# logger.write_log('HelloWorldddddddddd')
# logger2.write_log('dup[a')

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def stub(self):
        print('elo')
