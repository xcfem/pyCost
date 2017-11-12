#CodigosObra.h

#ifndef CODIGOSOBRA_H
#define CODIGOSOBRA_H

#include "Codigos.h"

class CodigosObra
    Codigos caps; #capitulos.
    Codigos elementos
    Codigos mediciones
    Codigos udsobr
    Codigos resto
    static std.set<std.string> codigos_capitulos
    void Trocea( int &verborrea)
public:
    CodigosObra(void) {
    bool ExisteConcepto( std.string &cod)
    std.string StrTablaConcepto( std.string &cod)
    Codigos.const_iterator BuscaConcepto( std.string &cod)

     Codigos &GetDatosElementos(void)
     Codigos &GetDatosUnidades(void)
     Codigos GetDatosObra(void)
     Codigos &GetDatosCaps(void)
     std.set<std.string> &GetCodigosCapitulos(void)

    Codigos.reg_capitulo GetDatosCapitulo( Codigos.mapa.const_iterator &i)
    Codigos FiltraPrecios( regBC3_d &descomp, &precios)
    Codigos FiltraElementales( regBC3_d &descomp)
    Codigos FiltraDescompuestos( regBC3_d &descomp)

     Codigos &GetDatosMeds(void)
    void BorraElementales( Codigos &els)
    void BorraDescompuestos( Codigos &uds)
    void LeeBC3(std.istream &is, &verborrea= 0)

    friend std.ostream &operator<<(std.ostream &os, &co)


#endif
