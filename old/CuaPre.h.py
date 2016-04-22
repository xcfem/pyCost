#CuaPre.h

#ifndef CUAPRE_H
#define CUAPRE_H

#include "Elementos.h"
#include "Descompuestos.h"

class CuaPre: public EntPpl
private:
    Elementos elementos; #Precios elementales.
    Descompuestos unidades; #Unidades de obra.

public:
     Elementos &Elementales(void)
        return elementos

    Elementos &Elementales(void)
        return elementos

     Descompuestos &UdsObra(void)
        return unidades

    inline bool TieneElementales(void)
        return (elementos.size()>0)

    inline size_t NumDescompuestos(void)
        return unidades.size()

    inline bool TieneDescompuestos(void)
        return (unidades.size()>0)

    inline BuscadorDescompuestos GetBuscadorDescompuestos(void)
        return unidades.GetBuscador()

     UdObra *BuscaUdObra( std.string &cod)
     Elemento *BuscaElemento( std.string &cod)
     Medible *BuscaPrecio( std.string &cod)
    void AgregaComponente( std.string &cod_ud, &cod_el, &r, &f= 1.0)
        unidades.AgregaComponente(elementos,cod_ud,cod_el,r,f)


    void EscribeSpre(void)
    void EscribeBC3(std.ostream &os)
    void LeeSpre(std.istream &is)
    inline void LeeBC3Elementales( Codigos &elem)
        elementos.LeeBC3(elem)

    inline void LeeBC3DescompFase1( Codigos &descomp)
        unidades.LeeBC3Fase1(descomp)

    Descompuestos.set_pendientes LeeBC3DescompFase2( Codigos &descomp)
#     inline void LeeBC3Fase1( CodigosObra &c)
##         LeeBC3Elementales(c.GetDatosElementos())
#         LeeBC3DescompFase1(c.GetDatosUnidades())
#
#     inline void LeeBC3Fase2( CodigosObra &c)
#       { LeeBC3DescompFase2(c.GetDatosUnidades());
    void ImprLtxElementales(std.ostream &os)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP1(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)
    void ImprLtxCP(std.ostream &os)
    void EscribeHCalc(std.ostream &os)
    void SimulaDescomp( std.string &origen, &destino)


#endif
