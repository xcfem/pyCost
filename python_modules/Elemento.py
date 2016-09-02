#Elemento.py




import Measurable
import bibXCBasica/src/texto/latex


class Elemento(Measurable):
    long double precio
    tipo_concepto tipo
protected:
    void check_tipo(void)
public:
    Elemento(  std.string &cod="", &tit="",
               std.string &ud="", double &p=0.0,
               tipo_concepto &tp= sin_clasif)
    virtual tipo_concepto Tipo(void)
    long double Precio(void)
    void LeeBC3( Codigos.reg_elemento &r)
    void ImprLtx(std.ostream &os)



#Elemento.cxx

import Elemento

Elemento.Elemento( std.string &cod, &tit,
                    std.string &ud, double &p, &tp)
    : Measurable(cod,tit,ud), precio(p), tipo(tp) {

def check_tipo(self, void):
    if not Codigo().empty():
        if tipo==sin_clasif and not EsPorcentaje():
            std.cerr << "El precio elemental de código: " << Codigo()
                      << " no es un porcentaje y su tipo está sin clasificar." << std.endl


def Tipo(self, void):
    return tipo

long double Elemento.Precio(void)
    return precio

def LeeBC3(self, &r):
    Measurable.LeeBC3(r)
    precio= r.Datos().Precio()
    tipo= sint2tipo_concepto(r.Datos().Tipo())


def ImprLtx(self, &os):
    os << ascii2latex(Codigo()) << " & "
       << ascii2latex(Unidad()) << " & "
       << ascii2latex(Titulo()) << " & "
       << StrPrecioLtx() << "\\\\" << std.endl

