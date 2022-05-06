# -*- coding: utf-8 -*-
#EntPyCost.py
import logging

class EntPyCost(object):
    ''' Root PyCost class.

    :ivar owner: object to which this object belongs.
    '''
    
    def __init__(self, owner= None):
        ''' Constructor.

        :param owner: object to which this object belongs.
        '''
        self.owner= owner
        
    def getDict(self):
        ''' Return a dictionary containing the object data.'''
        retval= dict()
        if(not self.owner is None):
            logging.error("Can't store pointer to owner.")
        return retval
        
    def setFromDict(self,dct):
        ''' Read member values from a dictionary.'''
        # Does nothing.

    @staticmethod
    def peek(inputFile, length=1):
        ''' Take a look to the following length bytes.

        :param inputFile: file to read from.
        :param length: number of bytes to read.
        '''
        pos = inputFile.tell()
        data = inputFile.read(length) # Might try/except this line, and finally: inputFile.seek(pos)
        inputFile.seek(pos)
        return data
    
        
