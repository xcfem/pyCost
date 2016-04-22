#MapaConceptos.h

#ifndef MAPACONCEPTOS_H
#define MAPACONCEPTOS_H

#include <map>
import EntPyCost

template<class T>
class MapaClaves(std.map<std.string, *>):


template<class T>
class MapaConceptos(std.map<std.string,T>, EntPyCost):
public:
    typedef std.map<std.string, map_ccpto
    typedef MapaClaves<T> map_claves

    typedef typename map_ccpto.iterator iterator
    typedef typename map_ccpto.const_iterator const_iterator
    typedef typename MapaClaves<T>.iterator claves_iterator
    typedef typename MapaClaves<T>.const_iterator claves_const_iterator
private:
    static map_claves claves
protected:
    virtual void err_no_encontrado( std.string &cod)
public:

    void Agrega( T &u)
        claves[u.Codigo()]= &((*self)[u.Codigo()]= u)

    T *Busca( std.string &cod)
     T *Busca( std.string &cod)
    void EscribeBC3(std.ostream &os)
    void Escribe(std.ostream &os)
    virtual ~MapaConceptos(void) {


template<class T>
MapaClaves<T> MapaConceptos<T>.claves

template<class T>
void MapaConceptos<T>.err_no_encontrado( std.string &cod)
    std.cerr << "Concepto: " << cod
              << " no encontrado" << std.endl

template<class T>
T *MapaConceptos<T>.Busca( std.string &cod)
    i = claves.find(cod)
    if i==claves.end():
        #err_no_encontrado(cod)
        return NULL

    return ((*i).second)

template<class T>
 T *MapaConceptos<T>.Busca( std.string &cod)
    i = claves.find(cod)
    if i==claves.end():
        #err_no_encontrado(cod)
        return NULL

    return ((*i).second)

template<class T>
void MapaConceptos<T>.EscribeBC3(std.ostream &os)
    j = MapaConceptos<T>.begin()
    for(; j!=MapaConceptos<T>.end(); j++)
        (*j).second.EscribeBC3(os)

template<class T>
void MapaConceptos<T>.Escribe(std.ostream &os)
    const_iterator i
    for(i= MapaConceptos<T>.begin(); i!=MapaConceptos<T>.end(); i++)
        (*i).second.Escribe(os)

#endif
