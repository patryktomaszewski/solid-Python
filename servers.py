#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Optional
import re


class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class TooManyProductsFoundError(Exception):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass

class Server(ABC):
    def __init__(self,list_prod: List[Product]):
        self.list_prod = list_prod

    def to_dict(self):
        slownik = {}
        for elem in self.list_prod:
            slownik[elem.name] = elem
        return slownik

    n_max_returned_entries = 5


    @abstractmethod
    def get_entries(self, n_letters:int = 1):
        pass

# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#  (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#  (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#  (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania

class ListServer(Server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_entries(self, n_letters:int )->List[Product]:
        getted_prod = []
        for elem in self.list_prod:




class MapServer:
    pass


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()



def main():
    print("ttt")
    lista = ['ab123', 'cd45', 'tp789']
    for elem in lista:
        z = re.match("(str\w+)\W(int\w+)",elem)
        if z:
            print((z.groups()))



