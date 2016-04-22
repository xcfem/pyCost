#fiebdc3.h

#ifndef FIEBDC3_H
#define FIEBDC3_H

#include <iostream>
#include "bibXCBasica/src/texto/StrTok.h"
#include "bibXCBasica/src/texto/cadena_carac.h"
#include <set>

def es_codigo_obra(self, &c):
def es_codigo_capitulo(self, &c):
def es_codigo_capitulo_u_obra(self, &c):

struct regBC3
    virtual StrTok &decod_bc3(StrTok &strtk)= 0
    void decod_str_bc3( std.string &str)
    virtual void Escribe(std.ostream &os)const= 0
    virtual ~regBC3(void) {
    static std.string limpia_str( std.string &)


std.ostream &operator<<(std.ostream &os, &r)

template<class T>
struct regBC3_lista_reg: public std.deque<T>, regBC3
    typedef typename std.deque<T>.const_iterator const_iterator

    regBC3_lista_reg(void) {
    regBC3_lista_reg( std.string &str)
    virtual StrTok &decod_bc3(StrTok &strtk)
    virtual void Escribe(std.ostream &os)


template<class T>
regBC3_lista_reg<T>.regBC3_lista_reg( std.string &str)
    decod_str_bc3(limpia_str(str))


template<class T>
StrTok &regBC3_lista_reg<T>.decod_bc3(StrTok &strtk)
    if(not strtk.size()) return strtk; #Nada a decodificar.
    T lt
    do
        lt.decod_bc3(strtk)
        self.push_back(lt)

    while(not strtk.final())
    return strtk

template<class T>
void regBC3_lista_reg<T>.Escribe(std.ostream &os)
    for(const_iterator i=self.begin(); i!=self.end(); i++)
        (*i).Escribe(os)


struct regBC3_desc: public regBC3
#Elemento de una descomposición
    std.string codigo; #Codigo de la entidad
    float factor
    float rendimiento
    regBC3_desc(void)
        : codigo(""),factor(.0),rendimiento(.0) {
    regBC3_desc( std.string &str)
    virtual StrTok &decod_bc3(StrTok &strtk)
    inline bool EsCapituloUObra(void)
        return (codigo.find("#")<codigo.length())

    inline bool EsCapitulo(void)
        return es_codigo_capitulo(codigo)

    inline bool EsObra(void)
        return es_codigo_obra(codigo)

    virtual void Escribe(std.ostream &os)
        os << "Código: " << codigo << std.endl
           << "Factor: " << factor << std.endl
           << "Rendimiento: " << rendimiento << std.endl



typedef regBC3_lista_reg<regBC3_desc> regBC3_lista_desc

struct regBC3_d: public regBC3_lista_desc
#Corresponde a un registro ~D de BC3.
    regBC3_d(void)
        : regBC3_lista_desc() {
    regBC3_d( std.string &str)
    virtual StrTok &decod_bc3(StrTok &strtk)
    bool EsCapitulo( regBC3_desc &r, &nombres_capitulo)
    regBC3_d FiltraCapitulos( std.set<std.string> &nombres_capitulo)
    regBC3_d FiltraPrecios( std.set<std.string> &nombres_capitulo)


struct MedArq: public regBC3
    std.string comentario
    double unidades
    double largo
    double ancho
    double alto

    virtual StrTok &decod_bc3(StrTok &strtk)
    virtual void Escribe(std.ostream &os)


struct regBC3_linea_med: public regBC3
    short int tipo
    # 0 (Vacio en el archivo)
    # 1 Subtotal parcial
    # 2 Subtotal acumulado.
    # 3 El comentario es una fórmula.
    MedArq med; #Medición
    regBC3_linea_med(void)
        : tipo(0),med() {
    regBC3_linea_med( std.string &str)
    virtual StrTok &decod_bc3(StrTok &strtk)
    virtual void Escribe(std.ostream &os)


typedef regBC3_lista_reg<regBC3_linea_med> regBC3_lista_med

struct regBC3_ruta: public StrTok.dq_campos, regBC3
    virtual StrTok &decod_bc3(StrTok &strtk)
    size_t Capitulos(void)
        return size()-1

    std.string Posicion(void)
        return *rbegin()

    virtual void Escribe(std.ostream &os)


struct regBC3_m: public regBC3
#Corresponde a un registro ~M de BC3.
    regBC3_ruta ruta; #Cap/subcap/subsubcap/.../posicion
    long double med_total
    regBC3_lista_med lista_med

    regBC3_m(void)
        : ruta(),med_total(0.0),lista_med() {
    regBC3_m( std.string &str)
    virtual StrTok &decod_bc3(StrTok &strtk)
    virtual void Escribe(std.ostream &os)


#not  @brief Corresponde a un registro ~C de BC3.
struct regBC3_c: public regBC3
    std.string unidad
    std.string resumen
    long double precio
    std.string fecha
    short int tipo
    regBC3_c(void)
        : unidad(""),resumen(""),precio(.0),fecha(""),tipo(0) {
    regBC3_c( std.string &str)
    virtual StrTok &decod_bc3(StrTok &strtk)
    virtual void Escribe(std.ostream &os)


#not  @brief Corresponde a un registro ~T de BC3.
struct regBC3_t: public regBC3
    std.string texto

    regBC3_t(void): texto("") {
    regBC3_t( std.string &str)
    virtual StrTok &decod_bc3(StrTok &strtk)
    virtual void Escribe(std.ostream &os)


struct regBC3_elemento
    regBC3_c ccpto; #Concepto.
    regBC3_t txt; #Texto.

    regBC3_elemento( regBC3_c &c, &t)
        : ccpto(c),txt(t) {
     std.string &Titulo(void)
        return ccpto.resumen

     std.string &Unidad(void)
        return ccpto.unidad

     long double &Precio(void)
        return ccpto.precio

    short int Tipo(void)
        return ccpto.tipo

     std.string &Texto(void)
        return txt.texto

    virtual void Escribe(std.ostream &os)
        ccpto.Escribe(os)
        txt.Escribe(os)

    virtual ~regBC3_elemento(void) {


std.ostream &operator<<(std.ostream &os, &e)

struct regBC3_udobra : public regBC3_elemento
    regBC3_d desc; #Descomposicion.

    regBC3_udobra( regBC3_c &c, &t, &d)
        : regBC3_elemento(c,t),desc(d) {
    virtual void Escribe(std.ostream &os)
        regBC3_elemento.Escribe(os)
        desc.Escribe(os)

    virtual ~regBC3_udobra(void) {


struct regBC3_medicion : public regBC3_elemento
    regBC3_m med; #Medicion.

    regBC3_medicion( regBC3_c &c, &t, &m)
        : regBC3_elemento(c,t),med(m) {
    regBC3_ruta Ruta(void)
        return med.ruta

    virtual void Escribe(std.ostream &os)
        regBC3_elemento.Escribe(os)
        med.Escribe(os)



std.ostream &operator<<(std.ostream &, &)

struct regBC3_capitulo: public regBC3_udobra
    regBC3_capitulo( regBC3_c &c, &t, &d)
    regBC3_d FiltraCapitulos( std.set<std.string> &nombres_capitulo)


#endif
