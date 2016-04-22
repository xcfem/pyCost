#Capitulo.h

#ifndef CAPITULO_H
#define CAPITULO_H

#include "MedsCap.h"
#include "EntFR.h"
#include "Subcapitulos.h"
#include "CuaPre.h"


class Capitulo: public EntBC3
private:
    EntFR fr
    MedsCap mediciones
protected:
    CuaPre precios; #Para precios elementales y descompuestos clasificados por capítulos.
    Subcapitulos subcapitulos

    friend class Subcapitulos
    void LeeBC3Elementales( Codigos &elementos)
    void LeeBC3DescompFase1( Codigos &descompuestos)
    Descompuestos.set_pendientes LeeBC3DescompFase2( Codigos &descompuestos)

public:
    Capitulo( std.string &cod= "CapSinCod", &tit= "CapSinTit",
              float &factor= 1.0, &rendimiento= 1.0)
    Capitulo( Capitulo &otro)
    Capitulo &operator=( Capitulo &otro)

    virtual std.string CodigoBC3(void)
     CuaPre &CuadroPrecios(void)
    CuaPre &CuadroPrecios(void)

    void AgregaPartida( Partida &m)
    CompBC3 GetCompBC3(void)

    Capitulo *BuscaSubcapitulo(regBC3_ruta &ruta)
    Capitulo *BuscaSubcapitulo( std.string &lst)
     Capitulo *BuscaCodigo( std.string &mnb)
    Capitulo *BuscaCodigo( std.string &mnb)
    inline bool TieneElementales(void)
        return precios.TieneElementales()

    size_t NumDescompuestos(void)
        return precios.NumDescompuestos()+subcapitulos.NumDescompuestos()

    inline bool TieneDescompuestos(void)
        return NumDescompuestos()> 0

    inline BuscadorDescompuestos GetBuscadorDescompuestos(void)
        return precios.GetBuscadorDescompuestos()

     Medible *BuscaPrecio( std.string &cod)

     Subcapitulos &getSubcapitulos(void)
        return subcapitulos

    Subcapitulos &getSubcapitulos(void)
        return subcapitulos

     MedsCap &getMediciones(void)
        return mediciones

    MedsCap &getMediciones(void)
        return mediciones


    virtual long double Precio(void)
    virtual ppl_precio PrecioR(void)

    void EscribeMediciones(std.ostream &os, &pos="")
        mediciones.Escribe(os,CodigoBC3(),pos)

    void EscribeSubCapitulos(std.ostream &os, primero= "False", &pos="")
        subcapitulos.EscribeBC3(os,primero,pos)

    void EscribePreciosBC3(std.ostream &os)
    void EscribeDescompBC3(std.ostream &os)
    void EscribeBC3(std.ostream &os, primero=False, pos="")

    static std.string SectionLtx( std.string &sect)
    void ImprCompLtxMed(std.ostream &os, &sect, &otro)
    void ImprLtxMed(std.ostream &os, &sect)
    void ImprLtxCP1(std.ostream &os, &sect)
    void ImprLtxCP2(std.ostream &os, &sect)
    void ImprLtxJustPre(std.ostream &os, &sect)
    void ImprLtxResumen(std.ostream &os, &sect, recurre= True)
    void ImprCompLtxPre(std.ostream &os, &sect, &otro)
    void ImprLtxPre(std.ostream &os, &sect)
    void EscribeHCalcMed(std.ostream &os, &sect)
    void EscribeHCalcPre(std.ostream &os, &sect)
    InformeMediciones GetInformeMediciones(void)


#endif
