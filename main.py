import csv


class CarBase:
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        pass


class Car(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, body_whl='0x0x0'):
        super().__init__(car_type, photo_file_name, brand, carrying)
        try:
            self.body_width = float(body_whl[0:(body_whl.find('x'))])
            self.body_height = float(body_whl[(body_whl.find('x') + 1):(body_whl.rfind('x'))])
            self.body_length = float(body_whl[(body_whl.rfind('x') + 1):])
        except ValueError:
            print('Вы ввели неверные значения')
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):

    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.extra = extra





def get_car_list(csv_filename):
    list = []
    list1 = []
    with open('file.csv') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            for i in row:
                if i != '':
                    list1.append(i)
            list.append(list1)
            # print(row)
            list1 = []

    for i in list:
        if len(i) > 0:
            list1.append(i)

    car_list = []
    for i in list1:
        if i[0] == 'car':
            obj = Car(*i)
            car_list.append(obj)
        elif i[0] == 'truck':
            obj = Truck(*i)
            car_list.append(obj)
        else:
            obj = SpecMachine(*i)
            car_list.append(obj)
    return car_list

print(get_car_list('file.csv'))
