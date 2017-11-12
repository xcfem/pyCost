#Elementos.h

#ifndef ELEMENTOS_H
#define ELEMENTOS_H

#include "Elemento.h"
#include "bibXCBasica/src/texto/cadena_carac.h"
#include <fstream>
#include "MapaConceptos.h"
#include "ComptesBC3.h"
#include "Codigos.h"
#include "bibXCLcmd/src/base/Buscadores.hxx"

class BuscadorElementos

#not  @brief Tabla de precios elementales.
class Elementos: public MapaConceptos<Elemento>
protected:
    static void ImprLtxCabecera( tipo_concepto &tipo, &os)
public:
    Elementos(void)

    BuscadorElementos GetBuscador(void)

    void LeeMdoSpre(std.istream &is)
    void LeeMaqSpre(std.istream &is)
    void LeeMatSpre(std.istream &is)
    void EscribeSpre(void)
    void LeeSpre(std.istream &is)
    void LeeBC3( Codigos &els)
    void ImprLtxTipo( tipo_concepto &tipo, &os)
    void ImprLtx(std.ostream &os)
    void EscribeHCalc(std.ostream &os)
        std.cerr << "Elementos.EscribeHCalc no implementada." << std.endl



class BuscadorElementos: public BuscadorPtros
    Elementos *contenedor; #Contenedor donde se buscan los punteros.
public:
    BuscadorElementos(Elementos *c)
        : contenedor(c) {
    virtual void  *Busca( std.string &clave)
        return contenedor.Busca(clave)

    virtual void *Busca( std.string &clave)
        return contenedor.Busca(clave)



#endif
