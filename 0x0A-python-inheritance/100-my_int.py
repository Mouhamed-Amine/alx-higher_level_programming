#!/usr/bin/python3

class MyInt(int):
    

    def __new__(cls, *args, **kwargs):
	return super(MyInt,cls).__new__(cls, *args, **kwargs)

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return int(self) != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return int(self) == value
