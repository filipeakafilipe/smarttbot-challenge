from abc import ABC, abstractmethod

class CurrencyRepositoryInterface(ABC):
    ''' Interface to Pet Repository '''

    @abstractmethod
    def insert_currency(self, currency) -> None:
        raise Exception("Method not implemented")
