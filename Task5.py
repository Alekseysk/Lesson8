"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""


class Equipment:
    price: float
    weight: float
    color: str = 'white'
    paper_size: str = 'A4'


class Printer(Equipment):
    def __init__(self, price: float, weight: float, speed_ppm: int, color: str = 'white',
                 paper_size: str = 'A4', prn_type: str = 'Laser', color_print: bool = False):
        self.price = price
        self.weight = weight
        self.color = color
        self.paper_size = paper_size
        self.prn_type = prn_type
        self.speed_ppm = speed_ppm
        self.color_print = color_print
    
    def __str__(self):
        return f'{self.prn_type} {self.paper_size} printer of {self.color} color'


class Scanner(Equipment):
    def __init__(self, price: float, weight: float, color: str = 'white', paper_size: str = 'A4',
                 resolution: int = 1200, bpp: int = 32, doc_feed: bool = False):
        self.price = price
        self.weight = weight
        self.color = color
        self.paper_size = paper_size
        self.resolution = resolution
        self.bpp = bpp
        self.doc_feed = doc_feed
    
    def __str__(self):
        return f'{self.paper_size} scanner with resolution of {self.resolution} dpi'


class Xerox(Equipment):
    def __init__(self, price: float, weight: float, speed_ppm: int, color: str = 'white',
                 paper_size: str = 'A4', resource: int = 10000):
        self.price = price
        self.weight = weight
        self.color = color
        self.paper_size = paper_size
        self.speed_ppm = speed_ppm
        self.resource = resource
    
    def __str__(self):
        return f'{self.paper_size} scanner with resource of {self.resource} pages'


class Warehouse:
    nomenclature = {Printer: [], Scanner: [], Xerox: []}
    
    def put_equipment(self, equipment):
        if isinstance(equipment, tuple(self.nomenclature.keys())):
            print(f'Нашёл, поклал {equipment}')
            self.nomenclature[equipment.__class__].append(equipment)
        else:
            print('Чего подсовываете???')
    
    def get_equipment(self, equipment):
        if isinstance(equipment, tuple(self.nomenclature.keys())) and \
                (equipment in self.nomenclature[equipment.__class__]):
            print(f'Имеется такое: {equipment}')
            place = self.nomenclature[equipment.__class__].index(equipment)
            self.nomenclature[equipment.__class__].pop(place)
        else:
            print(f'Нет такого на складе: {equipment}')


my_printer = Printer(price=12578.12, weight=8.4, speed_ppm=100, color_print=True)
my_scanner = Scanner(price=5864.65, weight=1.6, bpp= 48)
my_xerox = Xerox(price=23456.84, weight=23.4, speed_ppm=50, color = 'yellow')
my_warehouse = Warehouse()
my_warehouse.put_equipment(my_printer)
my_warehouse.put_equipment(my_scanner)
my_warehouse.put_equipment(my_printer)
my_warehouse.put_equipment(my_xerox)
my_warehouse.get_equipment(my_scanner)
my_warehouse.get_equipment(my_printer)
my_warehouse.get_equipment(my_scanner)