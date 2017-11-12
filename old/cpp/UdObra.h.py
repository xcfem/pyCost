#UdObra.h
#ifndef UD_OBRA_H
#define UD_OBRA_H

#include "Elementos.h"
#include "ComptesBC3.h"

class UdObra: public Medible
private:
    ComptesBC3 lista
    static ComptesBC3 ObtienePunteros( regBC3_d &descBC3, &bp, &error)
    ComptesBC3 GetSindesco( double &rendimiento, &bp)
public:
    UdObra( std.string &cod="", &tit="", &ud="")
        : Medible(cod,tit,ud) {
    virtual tipo_concepto Tipo(void)
        return mat;    #XXX provisional.

    virtual long double Precio(void)
        return lista.Precio()

    void AsignaFactor( float &f)
        lista.AsignaFactor(f)

    void Agrega( Elemento &e, &f, &r)
        lista.push_back(CompBC3(e,f,r))

    #not  @brief Lee la unidad a falta de la descomposición
    void LeeBC3Fase1( Codigos.reg_udobra &r)
        Medible.LeeBC3(r)

    bool LeeBC3Fase2( Codigos.reg_udobra &r, &bp)
    void EscribeSpre(std.ostream &os)
    void EscribeBC3(std.ostream &os)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP1(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)
    void EscribeHCalc(std.ostream &os)
    long double SimulaDescomp( UdObra &otra)


#endif
