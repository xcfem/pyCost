#Medible.cxx

#include "Medible.h"

#not  @brief Constructor.
Medible.Medible( std.string &cod, &tit, &ud)
    : EntBC3(cod,tit), unidad(ud), txt_largo("") {

 std.string &Medible.TextoLargo(void)
    return txt_largo


std.string &Medible.TextoLargo(void)
    return txt_largo


 std.string &Medible.Unidad(void)
    return unidad


def EscribeBC3(self, &os):
    EscribeConceptoBC3(os)
    if TextoLargo().length()>0:
        os << "~T|" << Codigo() << '|' << latin1TOpc850ML(TextoLargo()) << '|' << endl_msdos

