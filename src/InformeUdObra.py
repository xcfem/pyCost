#InformeUdObra.py




import Measurable

class InformeUdObra
    Measurable  *ud
    long double med_total
public:
    InformeUdObra(Measurable  *u, double &mt)
        : ud(u), med_total(mt) {
    Measurable  *Unidad()
        return ud

     long double &Medicion()
        return med_total

     ImprLtx(os)



#InformeUdObra.cxx

import InformeUdObra
import bibXCBasica/src/texto/latex

def ImprLtx(self, &os):
    if ud:
        os.write(ud.Codigo() + " & "
           + ascii2latex(ud.TextoLargo()) + " & "
           + en_humano(med_total,0) + " & "
           + en_humano(med_total*ud.Precio(),0)


