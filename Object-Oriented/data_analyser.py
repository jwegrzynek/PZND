# Metoda wytwórcza (factory method)
from abc import ABC, abstractmethod


class Reader(ABC):

    @abstractmethod
    def read_raw_data(self):
        pass

    @abstractmethod
    def get_structured_data(self):
        pass


class FileReader(Reader):

    def read_raw_data(self):
        print('Read from file')

    def get_structured_data(self):
        self.read_raw_data()
        print('Processimg')


class DatabaseReader(Reader):

    def read_raw_data(self):
        print('Read from database')

    def get_structured_data(self):
        self.read_raw_data()
        print('Processimg')


class DataAnalyser(ABC):
    @abstractmethod
    def create_reader(self):
        pass

    def analyse_data(self):
        reader = self.create_reader()
        df = reader.get_structured_data()


class FileDataAnalyser(DataAnalyser):
    def create_reader(self):
        return FileReader()


class DatabaseDataAnalyser(DataAnalyser):
    def create_reader(self):
        return DatabaseReader()


file_data_analyser = FileDataAnalyser()
database_data_analyser = DatabaseDataAnalyser()


