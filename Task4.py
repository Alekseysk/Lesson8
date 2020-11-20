"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""


class Warehouse:
    pass


class Equipment:
    price: float
    weight: float
    color: str = 'White'
    paper_size: str = 'A4'


class Printer(Equipment):
    def __init__(self, price: float, weight: float, speed_ppm: int, color: str = 'White',
                 paper_size: str = 'A4', prn_type: str = 'Laser', color_print: bool = False):
        self.price = price
        self.weight = weight
        self.color = color
        self.paper_size = paper_size
        self.prn_type = prn_type
        self.speed_ppm = speed_ppm
        self.color_print = color_print


class Scanner(Equipment):
    def __init__(self, price: float, weight: float, color: str = 'White', paper_size: str = 'A4',
                 resolution: int = 1200, bpp: int = 32, doc_feed: bool = False):
        self.price = price
        self.weight = weight
        self.color = color
        self.paper_size = paper_size
        self.resolution = resolution
        self.bpp = bpp
        self.doc_feed = doc_feed


class Xerox(Equipment):
    def __init__(self, price: float, weight: float, speed_ppm: int, color: str = 'White',
                 paper_size: str = 'A4', resource: int = 10000):
        self.price = price
        self.weight = weight
        self.color = color
        self.paper_size = paper_size
        self.speed_ppm = speed_ppm
        self.resource = resource


my_printer = Printer(price=12578.12, weight=8.4, speed_ppm=100, color_print=True)
