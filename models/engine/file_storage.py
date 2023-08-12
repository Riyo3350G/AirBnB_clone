#!/usr/bin/python3
'''
  model thats contain a FileStorage class that
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import json
import os


class FileStorage:
    ''' represent FileStorage class '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' function thats returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the new obj '''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file '''
        filename = self.__file_path
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(filename, 'w') as file:
            json.dump(data, file)

    def reload(self):
        ''' deserializes the JSON file to __objects '''
        filename = self.__file_path
        self.__objects = {}
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception as e:
            return
        for key, value in data.items():
            self.__objects[key] = base_model.BaseModel(**value)
