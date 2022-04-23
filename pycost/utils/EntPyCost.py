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

