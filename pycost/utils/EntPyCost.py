# -*- coding: utf-8 -*-
#EntPyCost.py

class EntPyCost(object):
    ''' Root PyCost class.

    :ivar owner: object to which this object belongs.
    '''
    
    def __init__(self, owner= None):
        ''' Constructor.

        :param owner: object to which this object belongs.
        '''
        self.owner= owner

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
    
        
