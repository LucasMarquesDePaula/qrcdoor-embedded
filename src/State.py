'''
Created on 13 de set de 2017

@author: Lucas
'''
 
from enum import IntFlag

class State(IntFlag):
    DONE = 0
    TRYING = 1
    ERROR = 2