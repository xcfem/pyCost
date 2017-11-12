#Obra.h

#ifndef OBRA_H
#define OBRA_H

#include "Capitulo.h"
#include "Porcentajes.h"

class CodigoObra
class Codigos

class Obra: public Capitulo
private:
    Porcentajes porcentajes

    inline virtual std.string nombre_clase(void)
        return "Obra"

public:
    Obra( std.string &cod="ObraSinCod", &tit="ObraSinTit")
    virtual std.string CodigoBC3(void)

    void AgregaCapitulo( std.string &cap_padre, &cap)
    void AgregaPartida( std.string &cap_padre, &m)

    void LeeBC3DatosObra( Codigos &obra)
    void EscribeSpre(void)
        precios.EscribeSpre()
        std.cerr << "Exportación de capítulos no implementada." << std.endl

    void EscribeBC3(std.ostream &os, pos="")
    void LeeMedicSpre(std.istream &is)
    void LeeSpre(std.istream &is)
    Capitulo *BuscaCapituloMedicion(regBC3_ruta &ruta)
    void LeeBC3Mediciones( CodigosObra &co)
    void LeeBC3(std.istream &is)

    void ImprLtxPresEjecMat(std.ostream &os)
    void ImprLtxPresContrata(std.ostream &os)
    void ImprLtxPresGen(std.ostream &os)
    void ImprLtxMed(std.ostream &os)
    void ImprCompLtxMed( Obra &otra, &os)
    void ImprLtxCP1(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP(std.ostream &os)
    void ImprLtxPreParc(std.ostream &os)
    void ImprCompLtxPreParc( Obra &otra, &os)
    void ImprLtxResumen(std.ostream &os)
    void ImprCompLtx( Obra &otra, &os)
    void ImprLtx(std.ostream &os)
    void ImprLtxInformeObra(std.ostream &os)

    void EscribeHCalc(std.ostream &os)
    void SimulaDescomp( std.string &origen, &destino)

#endif
