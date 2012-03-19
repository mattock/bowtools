#! /usr/bin/python
# -*- coding: utf-8 -*-

class LaminateBow():

    def __init__(self, maxlength, layers, *args, **kwargs):
        self.maxlength = maxlength
        self.layers = layers
        self.laminate_length = [] 

        decrement = self.maxlength / self.layers
        length = self.maxlength
        layer = 1

        while layer <= self.layers:
            self.laminate_length.append(length)
            length = length - decrement
            layer = layer + 1

    def __str__(self):

        output = ""
        layer = 1

        while layer <= len(self.laminate_length):
            output = output + str(layer) + ": " + str(self.laminate_length[layer-1]) + "\n"
            layer = layer + 1
        return output
