#MapaConceptos.py




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
    def err_no_encontrado( cod):
public:

     Agrega( T &u)
        claves[u.Codigo()]= &((*self)[u.Codigo()]= u)

    T *Busca( cod)
     T *Busca( cod)
     WriteBC3(os)
     Write(os)
    virtual ~MapaConceptos() {


template<class T>
MapaClaves<T> MapaConceptos<T>.claves

template<class T>
 MapaConceptos<T>.err_no_encontrado( cod)
    std.cerr + "Concepto: " + cod
              + " no encontrado" + '\n'

template<class T>
T *MapaConceptos<T>.Busca( cod)
    i = claves.find(cod)
    if i==claves.end():
        #err_no_encontrado(cod)
        return NULL

    return ((*i).second)

template<class T>
 T *MapaConceptos<T>.Busca( cod)
    i = claves.find(cod)
    if i==claves.end():
        #err_no_encontrado(cod)
        return NULL

    return ((*i).second)

template<class T>
 MapaConceptos<T>.WriteBC3(os)
    j = MapaConceptos<T>.begin()
    for(; j!=MapaConceptos<T>.end(); j++)
        (*j).second.WriteBC3(os)

template<class T>
 MapaConceptos<T>.Write(os)
    const_iterator i
    for(i= MapaConceptos<T>.begin(); i!=MapaConceptos<T>.end(); i++)
        (*i).second.Write(os)


