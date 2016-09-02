#Measurable.py




#include <string>
import EntBC3
import Codigos

# Thing that you can measure (en m,kg.py,m2,m3,...)
class Measurable(EntBC3):
    std.string unidad
    std.string txt_largo
public:
    Measurable( std.string &cod, &tit, &ud)
    virtual  std.string &TextoLargo(void)
    std.string &TextoLargo(void)
    virtual  std.string &Unidad(void)
    template<class T>
    void LeeBC3( T &r)
    void EscribeBC3(std.ostream &os)


template<class T>
def LeeBC3(self, &r):
    EntBC3.LeeBC3(r)
    unidad= r.Datos().Unidad()
    txt_largo= protege_signos(r.Datos().Texto())



#Measurable.cxx


#not  @brief Constructor.
Measurable.Measurable( std.string &cod, &tit, &ud)
    : EntBC3(cod,tit), unidad(ud), txt_largo("") {

 std.string &Measurable.TextoLargo(void)
    return txt_largo


std.string &Measurable.TextoLargo(void)
    return txt_largo


 std.string &Measurable.Unidad(void)
    return unidad


def EscribeBC3(self, &os):
    EscribeConceptoBC3(os)
    if TextoLargo().length()>0:
        os << "~T|" << Codigo() << '|' << latin1TOpc850ML(TextoLargo()) << '|' << endl_msdos

