//Medible.h

#ifndef MEDIBLE_H
#define MEDIBLE_H

#include <string>
#include "EntBC3.h"
#include "Codigos.h"

//! @brief Cosa que se mide (en m,kg,h,m2,m3,...)
class Medible: public EntBC3
{
    std::string unidad;
    std::string txt_largo;
public:
    Medible(const std::string &cod,const std::string &tit,const std::string &ud);
    virtual const std::string &TextoLargo(void) const;
    std::string &TextoLargo(void);
    virtual const std::string &Unidad(void) const;
    template<class T>
    void LeeBC3(const T &r);
    void EscribeBC3(std::ostream &os) const;
};

template<class T>
void Medible::LeeBC3(const T &r)
{
    EntBC3::LeeBC3(r);
    unidad= r.Datos().Unidad();
    txt_largo= protege_signos(r.Datos().Texto());
}

#endif
