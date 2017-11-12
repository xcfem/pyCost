#InformeUdObra.cxx

#include "InformeUdObra.h"
#include "bibXCBasica/src/texto/latex.h"

def ImprLtx(self, &os):
    if ud:
        os << ud.Codigo() << " & "
           << ascii2latex(ud.TextoLargo()) << " & "
           << en_humano(med_total,0) << " & "
           << en_humano(med_total*ud.Precio(),0)


