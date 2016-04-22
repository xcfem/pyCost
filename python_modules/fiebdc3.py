#fiebdc3.h

#ifndef FIEBDC3_H
#define FIEBDC3_H

#include <iostream>
import bibXCBasica/src/texto/StrTok
import bibXCBasica/src/texto/cadena_carac
#include <set>


def es_codigo_obra(self, &c):
    '''Returns true if c it's the code of a project.'''
    sz= len(c)
    if sz>1:
        return ((c[sz-2]=='#') and (c[sz-1]=='#'))
    else:
        return False


#not  @brief Devuelve verdadero si el código corresponde a un capítulo.
def es_codigo_capitulo(self, &c):
    retval = False
     sz = c.length()
    if es_codigo_capitulo_u_obra(c):
        if sz<2:
            retval= True; #Capítulo sin nombre.
        else:
            retval= (c[sz-2]!='#'); #Si no es obra, capítulo.

    return retval


def es_codigo_capitulo_u_obra(self, &c):
     sz = c.length()
    if sz>0:
        return (c[sz-1]=='#')
    else:
        return False


def limpia_str(self, &str):
    return q_car(q_car(str,char(10)),char(13))

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
#fiebdc3.cc

import fiebdc3
#include "boost/lexical_cast.hpp"



std.ostream &operator<<(std.ostream &os, &r)
    r.Escribe(os)
    return os


def decod_str_bc3(self, &str):
    if not str.empty():
        StrTok strtk(limpia_str(str))
        decod_bc3(strtk)



regBC3_desc.regBC3_desc( std.string &str)
    decod_str_bc3(limpia_str(str))


#not  @brief Decodifica la cadena str
StrTok &regBC3_desc.decod_bc3(StrTok &strtk)
    codigo= strtk.get_token('\\')
    tmp = strtk.get_token('\\')
    if not tmp.empty():
        factor= boost.lexical_cast<float>(tmp)
    if(factor==0.0) factor= 1.0; #Por defecto factor=1.0
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        rendimiento= boost.lexical_cast<float>(tmp)
    return strtk


regBC3_d.regBC3_d( std.string &str)
    decod_str_bc3(limpia_str(str))


StrTok &regBC3_d.decod_bc3(StrTok &strtk)
#La cadena que se pasa es la que queda a la derecha
#de ~D|
    strtk_lista_desc = strtk.get_token('|')
    regBC3_lista_desc.decod_bc3(strtk_lista_desc)
    return strtk


#not  @brief Devuelve verdadero si el registro corresponde a un capítulo.
def EsCapitulo(self, &r, &nombres_capitulo):
    retval = r.EsCapitulo()
    if not retval:
        retval= (nombres_capitulo.find(r.codigo+'#')!= nombres_capitulo.end())
    return retval


#not  @brief Devuelve los elementos de la descomposición que son capítulos.
def FiltraCapitulos(self, &nombres_capitulo):
    regBC3_d retval
    for(i = 0; i<size(); i++)
        if EsCapitulo((*self)[i],nombres_capitulo):
            retval.push_back((*self)[i])
    return retval

#not  @brief Devuelve los elementos de la descomposición que son precios elementales o descompuestos.
def FiltraPrecios(self, &nombres_capitulo):
    regBC3_d retval
    for(i = 0; i<size(); i++)
        if not EsCapitulo((*self)[i],nombres_capitulo):
            retval.push_back((*self)[i])
    return retval



#not  @brief Decodifica la cadena str
StrTok &regBC3_ruta.decod_bc3(StrTok &strtk)
    StrTok.dq_campos.operator=(strtk.campos('\\'))
    return strtk



def Escribe(self, &os):
    str = "Capitulo: "
    for(i = 0; i<Capitulos(); i++)
        os << str << (*self)[i] << std.endl
        str= "Sub" + str

    os << "Posición: " << Posicion()



StrTok &MedArq.decod_bc3(StrTok &strtk)
#Decodifica la cadena str
    unidades= 1
    largo= 1
    ancho= 1
    alto= 1
    comentario= strtk.get_token('\\')
    tmp = strtk.get_token('\\')
    if not tmp.empty():
        unidades= boost.lexical_cast<double>(tmp)
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        largo= boost.lexical_cast<double>(tmp)
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        ancho= boost.lexical_cast<double>(tmp)
    tmp= strtk.get_token('\\')
    if not tmp.empty():
        alto= boost.lexical_cast<double>(tmp)
    return strtk


def Escribe(self, &os):
    os << "Comentario: " << comentario << std.endl
       << "Unidades: " << unidades << std.endl
       << "Largo: " << largo << std.endl
       << "Ancho: " << ancho << std.endl
       << "Alto: " << alto << std.endl


regBC3_linea_med.regBC3_linea_med( std.string &str)
    decod_str_bc3(limpia_str(str))


#not  @brief Decodifica la cadena str
StrTok &regBC3_linea_med.decod_bc3(StrTok &strtk)
     tmp = strtk.get_token('\\')
    if not tmp.empty():
        tipo= boost.lexical_cast<short int>(tmp)
    return med.decod_bc3(strtk)


def Escribe(self, &os):
    os << "Tipo: " << tipo << std.endl
    med.Escribe(os)


regBC3_m.regBC3_m( std.string &str)
    decod_str_bc3(limpia_str(str))


#not  @brief Decodifica un registro de tipo medición (~M).
StrTok &regBC3_m.decod_bc3(StrTok &strtk)
#La cadena que se pasa es la que queda a la derecha
#de ~M|
    strtk_ruta = strtk.get_token('|')
    ruta.decod_bc3(strtk_ruta)
    tmp = strtk.get_token('|')
    if not tmp.empty():
        med_total= boost.lexical_cast<double>(tmp)
    strtk_lista_med = strtk.get_token('|')
    lista_med.decod_bc3(strtk_lista_med)
    return strtk


def Escribe(self, &os):
    os << "Ruta: "
    ruta.Escribe(os)
    os << std.endl << "Total: " << med_total << std.endl
    lista_med.Escribe(os)


regBC3_c.regBC3_c( std.string &str)
    decod_str_bc3(limpia_str(str))


StrTok &regBC3_c.decod_bc3(StrTok &strtk)
#Decodifica la cadena str
    unidad= strtk.get_token('|')
    resumen= strtk.get_token('|')
    tmp = strtk.get_token('|')
    if not tmp.empty():
        precio= boost.lexical_cast<double>(tmp)
    fecha= strtk.get_token('|')
    tmp= strtk.get_token('|')
    if not tmp.empty():
        tipo= boost.lexical_cast<short int>(tmp)
    return strtk


def Escribe(self, &os):
    os << "Unidad: " << unidad << std.endl
       << "Resumen: " << resumen << std.endl
       << "Precio: " << precio << std.endl
       << "Fecha: " << fecha << std.endl
       << "Tipo: " << tipo << std.endl



regBC3_t.regBC3_t( std.string &str)
    decod_str_bc3(limpia_str(str))


StrTok &regBC3_t.decod_bc3(StrTok &strtk)
#Decodifica la cadena str
    texto= strtk.get_token('|')
    return strtk


def Escribe(self, &os):
    os << "Texto: " << texto << std.endl


std.ostream &operator<<(std.ostream &os, &e)
    e.Escribe(os)
    return os


std.ostream &operator<<(std.ostream &os, &rm)
    rm.Escribe(os)
    return os


regBC3_capitulo.regBC3_capitulo( regBC3_c &c, &t, &d)
    : regBC3_udobra(c,t,d) {

def FiltraCapitulos(self, &nombres_capitulo):
    return desc.FiltraCapitulos(nombres_capitulo)

