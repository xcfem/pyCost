#Descompuestos.h

#ifndef DESCOMPUESTOS_H
#define DESCOMPUESTOS_H

#include "Elementos.h"
#include "UdObra.h"
#include <fstream>
#include "MapaConceptos.h"
#include <set>

class BuscadorDescompuestos

class Descompuestos: public MapaConceptos<UdObra>
#Unidades de obra.
public:
    typedef std.set<std.string> set_pendientes
    typedef MapaConceptos<UdObra> mapa_conceptos

    void AgregaComponente( Elementos &, &, &, &, &f= 1.0)
    BuscadorDescompuestos GetBuscador(void)

    void LeeBC3Fase1( Codigos &cds)
    set_pendientes LeeBC3Fase2( Codigos &cds, &bp)
    void LeeSpre(std.istream &is, &elementos)
    void EscribeSpre(std.ostream &os)
    void AsignaFactor( float &f)
    void ImprLtxJustPre(std.ostream &os)
    void ImprLtxCP1(std.ostream &os)
    void ImprLtxCP2(std.ostream &os)
    void EscribeHCalc(std.ostream &os)

    void SimulaDescomp( UdObra &origen, &destino)
    #Toma la descomposición de origen y se la da a destino
    #sin alterar el precio final de origen.
         lambda = destino.SimulaDescomp(origen)
        if lambda<0.0:
            std.cerr << "Los precios de los materiales de la unidad: "
                      << origen.Codigo() << " son muy altos para la unidad: "
                      << destino.Codigo() << " lambda= " << lambda << std.endl

    void SimulaDescomp( std.string &origen, &destino)
         UdObra *org= Busca(origen)
        UdObra *dest= Busca(destino)
        if org and dest:
            SimulaDescomp(*org,*dest)



class BuscadorDescompuestos: public BuscadorPtros
    Descompuestos *contenedor; #Contenedor donde se buscan los punteros.
public:
    BuscadorDescompuestos(Descompuestos *c)
        : contenedor(c) {
    virtual void  *Busca( std.string &clave)
    virtual void *Busca( std.string &clave)



#endif
