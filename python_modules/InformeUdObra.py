#InformeUdObra.h

#ifndef INFORMEUDOBRA_H
#define INFORMEUDOBRA_H

import Medible

class InformeUdObra
    Medible  *ud
    long double med_total
public:
    InformeUdObra(Medible  *u, double &mt)
        : ud(u), med_total(mt) {
    Medible  *Unidad(void)
        return ud

     long double &Medicion(void)
        return med_total

    void ImprLtx(std.ostream &os)


#endif
#InformeUdObra.cxx

import InformeUdObra
import bibXCBasica/src/texto/latex

def ImprLtx(self, &os):
    if ud:
        os << ud.Codigo() << " & "
           << ascii2latex(ud.TextoLargo()) << " & "
           << en_humano(med_total,0) << " & "
           << en_humano(med_total*ud.Precio(),0)


