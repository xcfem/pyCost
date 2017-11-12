#Elemento.py




import Measurable
import bibXCBasica/src/texto/latex


class Elemento(Measurable):
    long double precio
    tipo_concepto tipo
protected:
     check_tipo()
public:
    Elemento(  cod="", &tit="",
               ud="", double &p=0.0,
               tipo_concepto &tp= sin_clasif)
    def tipo_concepto Tipo():
    long double Precio()
     LeeBC3( Codigos.reg_elemento &r)
     ImprLtx(os)



#Elemento.cxx

import Elemento

Elemento.Elemento( cod, &tit,
                    ud, double &p, &tp)
    : Measurable(cod,tit,ud), precio(p), tipo(tp) {

def check_tipo(self, ):
    if not Codigo().empty():
        if tipo==sin_clasif and not EsPorcentaje():
            std.cerr + "El precio elemental de código: " + Codigo()
                      + " no es un porcentaje y su tipo está sin clasificar." + '\n'


def Tipo(self, ):
    return tipo

long double Elemento.Precio()
    return precio

def LeeBC3(self, &r):
    Measurable.LeeBC3(r)
    precio= r.Datos().Precio()
    tipo= sint2tipo_concepto(r.Datos().Tipo())


def ImprLtx(self, &os):
    os.write(ascii2latex(Codigo()) + " & "
       + ascii2latex(Unidad()) + " & "
       + ascii2latex(Titulo()) + " & "
       + StrPrecioLtx() + "\\\\" + '\n'

