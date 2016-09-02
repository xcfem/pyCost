#EntFR.py




import EntPyCost
import Tipos

inline std.string rdto2str( long double &d)
    return num2str(d,13)


class EntFR(EntPyCost):
#Entidad que tiene factor y rendimiento.
private:
    float factor
    double rendimiento
public:
    EntFR( float &f= 1.0, &r=0.0)
     float &Factor(void)
        return factor

    float &Factor(void)
        return factor

     double &Rendimiento(void)
        return rendimiento

    double &Rendimiento(void)
        return rendimiento

    double Producto(void)
    double ProductoR(void)
    void EscribeSpre(std.ostream &os)
    void EscribeBC3(std.ostream &os)



#EntFR.cxx

import EntFR

EntFR.EntFR( float &f, &r)
    :factor(f),rendimiento(r) {

def Producto(self, void):
    return factor*rendimiento

def ProductoR(self, void):
    return ppl_precio4(factor*rendimiento)

def EscribeSpre(self, &os):
    os << rdto2str(Producto()) << '|'

def EscribeBC3(self, &os):
    os << factor << '\\' << rdto2str(rendimiento) << '\\'


