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
            ownerCode= self.owner.Codigo()
            retval['owner_code']= ownerCode
        return retval
        
    def setFromDict(self, dct):
        ''' Read member values from a dictionary.

        :param dct: input dictionary.
        '''
        pendingLinks= list() # Links that cannot be set yet.
        self.owner= None
        if('owner_code' in dct):
            ownerCode= dct['owner_code']
            pendingLinks.append({'object':self, 'attr':'owner', 'key':ownerCode}) 
        return pendingLinks

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
    
        
