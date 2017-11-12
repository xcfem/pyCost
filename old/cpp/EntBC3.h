//EntBC3.h
//Precio elemental.

#ifndef ENTBC3_H
#define ENTBC3_H

#include <string>
#include <iostream>
#include "bibXCBasica/src/texto/en_letra.h"
#include "Codigos.h"
#include "EntPpl.h"
#include "Tipos.h"

const char tab= char(9);

inline std::string precio2str(const long double &d)
{
    return num2str(d,13);
}


/* TIPO: Tipo de concepto, Inicialmente se reservan los siguientes tipos: */

/* 0 (Sin clasificar) 1 (Mano de obra), 2 (Maquinaria y medios aux.), 3 (Materiales). */

typedef enum {sin_clasif=0,mdo=1,maq=2,mat=3} tipo_concepto;

tipo_concepto str2tipo_concepto(const std::string &str);
tipo_concepto sint2tipo_concepto(const short int &si);
std::string tipo_concepto2str(const tipo_concepto &);

class EntBC3: public EntPpl
{
private:
    std::string codigo;
    std::string titulo;
    static const std::string txtud;
    static const std::string txtl;
public:
    EntBC3(const std::string &cod,const std::string &tit);

    virtual const std::string &Codigo(void) const;
    std::string &Codigo(void);
    virtual std::string CodigoBC3(void) const;

    virtual const std::string &Unidad(void) const;
    const std::string &Titulo(void) const;
    std::string &Titulo(void);

    virtual std::string StrPrecio(void) const;
    std::string StrPrecioLtx(void) const;
    std::string StrPrecioEnLetra(const bool &genero) const;
    virtual long double Precio(void) const;
    virtual ppl_precio PrecioR(void) const;

    virtual std::string Fecha(void) const;
    virtual tipo_concepto Tipo(void) const;
    virtual const std::string &TextoLargo(void) const;
    virtual char ChrTipo(void) const;
    bool EsPorcentaje(void) const;

    template<class T>
    void LeeBC3(const T &r);
    void EscribeSpre(std::ostream &os) const;
    void EscribeConceptoBC3(std::ostream &os,const bool &primero= false) const;
    void Escribe(std::ostream &os) const;
    virtual ~EntBC3(void) {}
};

template<class T>
void EntBC3::LeeBC3(const T &r)
{
    if(verborrea>4)
        std::clog << "Cargando concepto: '" << r.Codigo() << "'\n";
    codigo= r.Codigo();
    titulo= protege_signos(r.Datos().Titulo());
}

std::ostream &operator<<(std::ostream &os,const EntBC3 &e);

#endif
