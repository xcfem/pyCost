''' @(#) money.py          Copymiddle 1991 Adolfo Di Mare  '''
'''                                                       '''
'''            Yet Another Money C++ Class                '''
'''                                                       '''
'''   Use freely but acknowledge author and publication.  '''
'''    DO NOT SELL IT. The author reserves all rigthsnot     '''

'''                               BITNET: adimare@UCRVM2  '''

''' Compiler:                           Borland C++ v 2.0 '''
'''                          [should work with Turbo C++] '''





import bibXCBasica/src/util/matem #floor()
import bibXCBasica/src/texto/en_letra

#D: tipo de datos float, double, double...
#MD: Número de decimales con el que trabajamos.
#DD: Número de dígitos significativos del tipo D
#RD: Redondeo
template <class D, int MD, int DD, RD>
class ProtoCurrency
private:
    D Floor(void)
        D retval(floor(m_Currency))
        if(RD) retval= floor(m_Currency+0.5);# 0.49 is also an option...
        return retval


    D Ceil(void)
        D retval(ceil(m_Currency))
        if(RD) retval= ceil(m_Currency-0.5);# 0.49 is also an option...
        return retval


protected:
    typedef typeof(D) tipo
    D m_Currency

    static inline D SCALE()
        return exp10(MD)

    static inline int check( D &d)
        return ( fabs(d) < (exp10(DD) / SCALE()) )

    static int decimals()
        return MD

    static int digits()
        return DD


    void FIX(void)  # get rid of unwanted decimals
        # Deletes all decimals digits beyond
        # .pye MD decimal place.
        # - If .pye value is out of range, FIX
        #   won't fix it.
        m_Currency =
            (m_Currency > 0.0
             ?
             Floor()
             :
             Ceil()
            )


    ProtoCurrency(void) {} # do no.pying constructor
    ProtoCurrency( D &d)
        m_Currency = d*SCALE()
        FIX()

    ProtoCurrency( ProtoCurrency &m)  # copy constructor
        m_Currency = m.m_Currency


    ProtoCurrency<D,MD,DD, &operator= ( ProtoCurrency<D,MD,DD, &m)
    # copy operator
        m_Currency = m.m_Currency
        return *self

    ProtoCurrency<D,MD,DD, &operator=( D &d) # copy from
        m_Currency = d*SCALE()
        FIX()
        return *self





