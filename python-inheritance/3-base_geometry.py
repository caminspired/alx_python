#!/usr/bin/python3
""" this module contains class BaseGeometry """


class BaseGeometry:
    """ defines the class BaseGeometry """
    pass


    def dir(cls):
        """ removes __init__subclass from dir() """
        return [attribute for  attribute in super().dir() if attribute != "init_subclass"] 
