/* @(#) money.h          Copymiddle 1991 Adolfo Di Mare  */
/*                                                       */
/*            Yet Another Money C++ Class                */
/*                                                       */
/*   Use freely but acknowledge author and publication.  */
/*    DO NOT SELL IT. The author reserves all rigths!    */

/*                               BITNET: adimare@UCRVM2  */

/* Compiler:                           Borland C++ v 2.0 */
/*                          [should work with Turbo C++] */


#ifndef CURRENCY_H
#define CURRENCY_H

#include "ProtoCurrency.h"

template<short int MD>
class Currency: public ProtoCurrency<long double,MD,LDBL_DIG,true>
{
    typedef ProtoCurrency<long double,MD,LDBL_DIG,true> pc;
public:

    // Constructores && asignación
    Currency(void) {} // do nothing constructor
    Currency(const typename pc::tipo &d)
        : pc(d) {}
    Currency(const Currency &m)
        : pc(m) {}  // copy constructor

    Currency &operator= (const Currency &m)  // copy operator
    {
        pc::operator=(m);
        return *this;
    }
    Currency &operator=(const typename pc::tipo &d) // copy from double
    {
        pc::operator=(d);
        return *this;
    }
    operator typename pc::tipo() const  // convert to double
    {
        return pc::m_Currency / pc::SCALE();
    }
    int  OK(void) const  // check Currency's invariant
    // Returns TRUE (1) when the quantity stored
    // in *this really corresponds to a Currency
    // quantity.
    {
        Currency temp;
        temp.m_Currency= this->m_Currency;
        temp.FIX();
        return (
                   ( temp.m_Currency == this->m_Currency )
                   &&
                   ( pc::check(this->m_Currency) )
               );
    }


    inline friend Currency  operator + (const Currency &m, const Currency &mm)
    {
        Currency temp;    // don't mult*SCALE()
        temp.m_Currency = m.m_Currency + mm.m_Currency;
        return temp;
    }
    inline friend Currency  operator + (const typename pc::tipo &d, const Currency &m)
    {
        return (Currency(d)+m);
    }
    inline friend Currency  operator + (const Currency &m,const typename pc::tipo &d)
    {
        return (m+Currency(d));
    }

    inline friend Currency  operator - (const Currency &m, const Currency &mm)
    {
        Currency temp;
        temp.m_Currency = m.m_Currency - mm.m_Currency;
        return temp;
    }
    inline friend Currency  operator - (const typename pc::tipo &d,const Currency &m)
    {
        return (Currency(d)-m);
    }
    inline friend Currency operator-(const Currency &m,const typename pc::tipo &d)
    {
        return (m-Currency(d));
    }

    inline friend Currency  operator*(const Currency &m,const typename pc::tipo &d)
    {
        Currency temp;
        temp.m_Currency = m.m_Currency * d; // don't mult by SCALE()
        temp.FIX();    // this could be delayed...
        return temp;
    }
    inline friend Currency operator*(const typename pc::tipo &d, const Currency &m)
    {
        return (m*d);
    }
    inline friend typename pc::tipo operator/(const Currency &m, const Currency &mm)
    {
        return m.m_Currency / mm.m_Currency;
    }
    friend Currency operator/(const Currency &m,const typename pc::tipo &d)
    {
        Currency temp;
        temp.m_Currency = m.m_Currency / d;
        temp.FIX();    // this could be delayed...
        return temp;
    }
    inline friend Currency  operator%(const Currency &m, const Currency &mm)
    {
        Currency temp;
        temp.m_Currency = fmod(m.m_Currency, mm.m_Currency);
        temp.FIX();    // this could be delayed...
        return temp;
    }

    // Currency  * Currency  is NOT valid
    // pc::tipo / Currency  is INVALID

    friend int operator == (const Currency &m, const Currency &mm)
    {
        return m.m_Currency ==  mm.m_Currency;
    }
    inline friend int operator != (const Currency &m, const Currency &mm)
    {
        return m.m_Currency !=  mm.m_Currency;
    }
    inline friend int operator <  (const Currency &m, const Currency &mm)
    {
        return m.m_Currency <   mm.m_Currency;
    }
    inline friend int operator >  (const Currency &m, const Currency &mm)
    {
        return m.m_Currency >   mm.m_Currency;
    }
    inline friend int operator <= (const Currency &m, const Currency &mm)
    {
        return m.m_Currency <=  mm.m_Currency;
    }
    inline friend int operator >= (const Currency &m, const Currency &mm)
    {
        return m.m_Currency >=  mm.m_Currency;
    }

    inline friend int operator == (const Currency &m,const typename pc::tipo &mm)
    {
        return m.m_Currency == mm;
//  return m.m_Currency == (Currency)mm;  // take a pick !!!
        /*
            A decission that you should make is whether this
            equality comparison requires the pc::tipo quantity
            to  be  promoted  to  a Currency item.  The  direct
            comparison   is   more   transparent,   so it is
            prefered in here.
        */
    }
    inline friend int operator != (const Currency &m,const typename pc::tipo &mm)
    {
        return !(m == mm);
    }
    inline friend int operator<(const Currency& m,const typename pc::tipo &mm)
    {
        return m < Currency(mm);
    }
    inline friend int operator>(const Currency& m,const typename pc::tipo &mm)
    {
        return m > Currency(mm);
    }
    inline friend int operator<=(const Currency &m,const typename pc::tipo &mm)
    {
        return m <= Currency(mm);
    }
    inline friend int operator>=(const Currency& m,const typename pc::tipo &mm)
    {
        return m >= Currency(mm);
    }

    inline friend int operator==(const typename pc::tipo &m,const Currency& mm)
    {
        return  (mm == m);
    }
    inline friend int operator!=(const typename pc::tipo &m,const Currency& mm)
    {
        return !(mm == m);
    }
    inline friend int operator<(const typename pc::tipo &m, const Currency& mm)
    {
        return  m <  Currency(mm);
    }
    inline friend int operator>(const typename pc::tipo &m, const Currency& mm)
    {
        return  m >  Currency(mm);
    }
    inline friend int operator<=(const typename pc::tipo &m, const Currency& mm)
    {
        return  m <= Currency(mm);
    }
    inline friend int operator>=(const typename pc::tipo &m, const Currency& mm)
    {
        return  m >= Currency(mm);
    }


    inline Currency& operator+=(const Currency& m)
    {
        this->m_Currency+= m.m_Currency;
        return *this;
    }
    inline Currency& operator+=(const typename pc::tipo &d)
    {
        this->m_Currency += d*pc::SCALE();
        pc::FIX();
        return *this;
    }
    inline Currency& operator-=(const Currency& m)
    {
        this->m_Currency-= m.m_Currency;
        return *this;
    }
    inline Currency& operator-=(const typename pc::tipo &d)
    {
        this->m_Currency-= d*pc::SCALE();
        pc::FIX();
        return *this;
    }


    inline Currency& operator *=(const typename pc::tipo &d)
    {
        this->m_Currency *= d;
        pc::FIX();
        return *this;
    }
    inline Currency& operator /= (typename pc::tipo d)
    {
        this->m_Currency /= d;
        pc::FIX();
        return *this;
    }

    // unary op's
    inline friend Currency operator+(const Currency& m)
    {
        return m;
    }
    inline friend Currency operator-(const Currency& m)
    {
        Currency temp;
        temp.m_Currency = -m.m_Currency;
        return temp;
    }

    inline Currency &operator++()
    {
        this->m_Currency += pc::SCALE();
        if(pc::decimals()<0) pc::FIX(); // avoid problems because of
        // the representation of 10^-n
        return *this;
    }
    inline Currency &operator--()
    {
        this->m_Currency-= pc::SCALE();
        if(pc::decimals()<0) pc::FIX();
        return *this;
    }

    inline Currency& operator++(int)
    {
        return ++(*this);
    }

    inline Currency& operator--(int)
    {
        return --(*this);
    }
    inline friend int operator!(const Currency& m)
    {
        return m.m_Currency == 0.0;
    }



    inline friend Currency abs(const Currency &m)
    {
        Currency temp;
        temp.m_Currency = fabs(m.m_Currency);
        return temp;
    }
    friend Currency flatten(const Currency& m,const typename pc::tipo &cents, int rounding)
    {
        // Returns a Currency data item where the cents are
        // rounded modulo "cents". In this way cents can
        // be stripped of Currency items when the currency
        // does not have all the coins required to pay
        // every posible quantity.
        Currency temp;
        typename pc::tipo c = floor(fabs(cents*Currency::SCALE())); // cents
        typename pc::tipo r = fmod(m.m_Currency, c);            // remainder
        temp.m_Currency =
            (!rounding || (2.0* r <= c)
             ? m.m_Currency - r
             : m.m_Currency - r + c
            );
        return temp;
    }
    inline friend Currency floor(const Currency &m)
    {
        Currency temp;
        temp= floor(static_cast<typename pc::tipo>(m));
        return temp;
    }
    inline Currency IP(void) const
    {
        return floor(*this);
    }
    inline Currency FP(void) const
    {
        return (*this)-floor(*this);
    }
    inline Currency Redondeo(void) const
    {
        Currency rnd= -FP();
        if(rnd <= Currency(-0.5)) rnd+=1.0;
        return rnd;
    }
    std::string EnLetra(const bool &genero,const std::string &sep_dec= " con ", const std::string &coletilla= " céntimos" ) const
    {
        return en_letra((typename pc::tipo) *this,pc::decimals(),genero,sep_dec,coletilla);
    }
    std::string EnHumano(const char &sep_miles='.',const char &sep_dec= '\'') const
    {
        return en_humano((typename pc::tipo) *this,pc::decimals(),sep_miles,sep_dec);
    }
};


#endif
