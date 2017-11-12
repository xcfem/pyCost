''' @(#) money.py          Copymiddle 1991 Adolfo Di Mare  '''
'''                                                       '''
'''            Yet Another Money C++ Class                '''
'''                                                       '''
'''   Use freely but acknowledge author and publication.  '''
'''    DO NOT SELL IT. The author reserves all rigthsnot     '''

'''                               BITNET: adimare@UCRVM2  '''

''' Compiler:                           Borland C++ v 2.0 '''
'''                          [should work with Turbo C++] '''





import ProtoCurrency

template<short int MD>
class Currency(ProtoCurrency<long double,MD,LDBL_DIG,True>):
    typedef ProtoCurrency<long double,MD,LDBL_DIG, pc
public:

    # Constructores and asignación
    Currency(void) {} # do no.pying constructor
    Currency( typename pc.tipo &d)
        : pc(d) {
    Currency( Currency &m)
        : pc(m) {}  # copy constructor

    Currency &operator= ( Currency &m)  # copy operator
        pc.operator=(m)
        return *self

    Currency &operator=( typename pc.tipo &d) # copy from double
        pc.operator=(d)
        return *self

    operator typename pc.tipo()   # convert to double
        return pc.m_Currency / pc.SCALE()

    int  OK(void)   # .pyeck Currency's invariant
    # Returns TRUE (1) when .pye quantity stored
    # in *self really corresponds to a Currency
    # quantity.
        Currency temp
        temp.m_Currency= self.m_Currency
        temp.FIX()
        return (
                   ( temp.m_Currency == self.m_Currency )
                   and
                   ( pc.check(self.m_Currency) )
               )



    inline friend Currency  operator + ( Currency &m, &mm)
        Currency temp;    # don't mult*SCALE()
        temp.m_Currency = m.m_Currency + mm.m_Currency
        return temp

    inline friend Currency  operator + ( typename pc.tipo &d, &m)
        return (Currency(d)+m)

    inline friend Currency  operator + ( Currency &m, pc.tipo &d)
        return (m+Currency(d))


    inline friend Currency  operator - ( Currency &m, &mm)
        Currency temp
        temp.m_Currency = m.m_Currency - mm.m_Currency
        return temp

    inline friend Currency  operator - ( typename pc.tipo &d, &m)
        return (Currency(d)-m)

    inline friend Currency operator-( Currency &m, pc.tipo &d)
        return (m-Currency(d))


    inline friend Currency  operator*( Currency &m, pc.tipo &d)
        Currency temp
        temp.m_Currency = m.m_Currency * d; # don't mult by SCALE()
        temp.FIX();    # self could be delayed...
        return temp

    inline friend Currency operator*( typename pc.tipo &d, &m)
        return (m*d)

    inline friend typename pc.tipo operator/( Currency &m, &mm)
        return m.m_Currency / mm.m_Currency

    friend Currency operator/( Currency &m, pc.tipo &d)
        Currency temp
        temp.m_Currency = m.m_Currency / d
        temp.FIX();    # self could be delayed...
        return temp

    inline friend Currency  operator%( Currency &m, &mm)
        Currency temp
        temp.m_Currency = fmod(m.m_Currency, mm.m_Currency)
        temp.FIX();    # self could be delayed...
        return temp


    # Currency  * Currency  is NOT valid
    # pc.tipo / Currency  is INVALID

    friend int operator == ( Currency &m, &mm)
        return m.m_Currency ==  mm.m_Currency

    inline friend int operator != ( Currency &m, &mm)
        return m.m_Currency !=  mm.m_Currency

    inline friend int operator <  ( Currency &m, &mm)
        return m.m_Currency <   mm.m_Currency

    inline friend int operator >  ( Currency &m, &mm)
        return m.m_Currency >   mm.m_Currency

    inline friend int operator <= ( Currency &m, &mm)
        return m.m_Currency <=  mm.m_Currency

    inline friend int operator >= ( Currency &m, &mm)
        return m.m_Currency >=  mm.m_Currency


    inline friend int operator == ( Currency &m, pc.tipo &mm)
        return m.m_Currency == mm
#  return m.m_Currency == (Currency)mm;  # take a pick not !!
        '''
            A decission that you should make is whether self
            equality comparison requires the pc.tipo quantity
            to  be  promoted  to  a Currency item.  The  direct
            comparison   is   more   transparent, it is
            prefered in here.
        '''

    inline friend int operator != ( Currency &m, pc.tipo &mm)
        return not (m == mm)

    inline friend int operator<( Currency& m, pc.tipo &mm)
        return m < Currency(mm)

    inline friend int operator>( Currency& m, pc.tipo &mm)
        return m > Currency(mm)

    inline friend int operator<=( Currency &m, pc.tipo &mm)
        return m <= Currency(mm)

    inline friend int operator>=( Currency& m, pc.tipo &mm)
        return m >= Currency(mm)


    inline friend int operator==( typename pc.tipo &m, mm)
        return  (mm == m)

    inline friend int operator!=( typename pc.tipo &m, mm)
        return not (mm == m)

    inline friend int operator<( typename pc.tipo &m, mm)
        return  m <  Currency(mm)

    inline friend int operator>( typename pc.tipo &m, mm)
        return  m >  Currency(mm)

    inline friend int operator<=( typename pc.tipo &m, mm)
        return  m <= Currency(mm)

    inline friend int operator>=( typename pc.tipo &m, mm)
        return  m >= Currency(mm)



    inline Currency& operator+=( Currency& m)
        self.m_Currency+= m.m_Currency
        return *self

    inline Currency& operator+=( typename pc.tipo &d)
        self.m_Currency += d*pc.SCALE()
        pc.FIX()
        return *self

    inline Currency& operator-=( Currency& m)
        self.m_Currency-= m.m_Currency
        return *self

    inline Currency& operator-=( typename pc.tipo &d)
        self.m_Currency-= d*pc.SCALE()
        pc.FIX()
        return *self



    inline Currency& operator *=( typename pc.tipo &d)
        self.m_Currency *= d
        pc.FIX()
        return *self

    inline Currency& operator /= (typename pc.tipo d)
        self.m_Currency /= d
        pc.FIX()
        return *self


    # unary op's
    inline friend Currency operator+( Currency& m)
        return m

    inline friend Currency operator-( Currency& m)
        Currency temp
        temp.m_Currency = -m.m_Currency
        return temp


    inline Currency &operator++()
        self.m_Currency += pc.SCALE()
        if(pc.decimals()<0) pc.FIX(); # avoid problems because of
        # .pye representation of 10^-n
        return *self

    inline Currency &operator--()
        self.m_Currency-= pc.SCALE()
        if pc.decimals()<0) pc.FIX(:
        return *self


    inline Currency& operator++(int)
        return ++(*self)


    inline Currency& operator--(int)
        return --(*self)

    inline friend int operatornot ( Currency& m)
        return m.m_Currency == 0.0




    inline friend Currency abs( Currency &m)
        Currency temp
        temp.m_Currency = fabs(m.m_Currency)
        return temp

    friend Currency flatten( Currency& m, pc.tipo &cents, rounding)
        # Returns a Currency data item where .pye cents are
        # rounded modulo "cents". In self way cents can
        # be stripped of Currency items when .pye currency
        # does not have all .pye coins required to pay
        # every posible quantity.
        Currency temp
        typename c = floor(fabs(cents*Currency.SCALE())); # cents
        typename r = fmod(m.m_Currency, c);            # remainder
        temp.m_Currency =
            (not rounding or (2.0* r <= c)
             ? m.m_Currency - r
             : m.m_Currency - r + c
            )
        return temp

    inline friend Currency floor( Currency &m)
        Currency temp
        temp= floor(static_cast<typename pc.tipo>(m))
        return temp

    inline Currency IP(void)
        return floor(*self)

    inline Currency FP(void)
        return (*self)-floor(*self)

    inline Currency Redondeo(void)
        rnd = -FP()
        if(rnd <= Currency(-0.5)) rnd+=1.0
        return rnd

    std.string EnLetra( bool &genero, &sep_dec= " con ", &coletilla= " céntimos" )
        return en_letra((typename pc.tipo) *self,pc.decimals(),genero,sep_dec,coletilla)

    std.string EnHumano( char &sep_miles='.', &sep_dec= '\'')
        return en_humano((typename pc.tipo) *self,pc.decimals(),sep_miles,sep_dec)





#DatosPyCost.cxx

import DatosPyCost

