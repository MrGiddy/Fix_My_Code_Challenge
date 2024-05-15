#!/usr/bin/python3
""" Defines class Square. """


class Square():
    """ Represents a Square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize a Square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of a Square """
        return self.width * self.height

    def PerimiterOfMySquare(self):
        """ Perimeter of a Square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of a Square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Driver code """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimiterOfMySquare())
