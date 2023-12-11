#!/usr/bin/python3
"""My module for creating a class Base"""
import json
import csv


class Base:
    """the base class for all the classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """assign public instance atttribute id with this argument value"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts dict representation into json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns python version of json string"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates instance of rectangle and square off the dictionary"""
        if "size" in dictionary:
            dummy = cls(1)
        else:
            dummy = cls(1, 1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """loads list objects into dicts and sends them to a function that
        turns them into json"""
        filename = "{}.csv".format(cls.__name__)
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list += [obj.to_dictionary()]

        json_list = Base.to_json_string(obj_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)

    @classmethod
    def load_from_file(cls):
        """returns instances in lists"""

        from_filename = "{}.json".format(cls.__name__)
        instance_list = []

        try:
            with open(from_filename, mode="r+", encoding="UTF-8") as f:
                raw_json = f.read()
            list_dicts = cls.from_json_string(raw_json)
            for d in list_dicts:
                instance_list += [cls.create(**d)]
        except FileNotFoundError:
            pass
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialization in CSV"""
        filename = "{}.csv".format(cls.__name__)
        data = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                data.append(dictionary)
        rectangle_header = ['id', 'width', 'height', 'x', 'y']
        square_header = ['id', 'size', 'x', 'y']
        with open(filename, mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    result = csv.DictWriter(f, fieldnames=rectangle_header)
                elif cls.__name__ == 'Square':
                    result = csv.DictWriter(f, fieldnames=square_header)
                result.writeheader()
                result.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """deserialization into CSV"""
        filename = "{}.csv".format(cls.__name__)
        instance_list = []
        try:
            with open(filename) as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list
