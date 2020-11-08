from abc import ABC, abstractmethod


class SqlDataClass(ABC):
    @abstractmethod
    def generate_instance(self):
        pass

    @abstractmethod
    def generate_sql(self):
        pass

    @staticmethod
    @abstractmethod
    def generate_all():
        pass
