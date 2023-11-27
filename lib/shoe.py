#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    
    def get_size(self):
        print(self._size)
        return self._size
    
    def set_size(self, new_size):
        if (type(new_size) == int):
            self._size = new_size
            print("size set to", new_size)
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)