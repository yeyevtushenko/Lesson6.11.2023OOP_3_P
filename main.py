class Computer:
    def __init__(self, processor, ram, graphics_card):
        self.__processor = processor
        self.__ram = ram
        self.__graphics_card = graphics_card

    def get_processor(self):
        return self.__processor

    def get_ram(self):
        return self.__ram

    def get_graphics_card(self):
        return self.__graphics_card

    def display_info(self):
        print(f"Інформація про комп'ютер:")
        print(f"Процесор: {self.__processor}")
        print(f"ОЗУ: {self.__ram}")
        print(f"Відеокарта: {self.__graphics_card}")


computer = Computer(processor="Intel i7", ram="16 ГБ", graphics_card="NVIDIA GeForce RTX 3070")
computer.display_info()