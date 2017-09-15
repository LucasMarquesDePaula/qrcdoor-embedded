'''
Created on 13 de set de 2017

@author: Lucas
'''

class Obj(dict):
    def __getattr__(self, name):
        return self[name]
