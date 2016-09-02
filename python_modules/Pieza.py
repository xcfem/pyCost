#Pieza.py
#Figura geométrica llena de una unidad de obra.




import ProtoPartida
import matemat/geom-2.0/src/listas/GmGrupo

#Metodo de medida
typedef enum {unidad,longitud,area,volumen,peso_l,peso_a,peso_v} forma_medicion
#peso_l: Peso obtenido multiplicando densidad por longitud.
#peso_a: Peso obtenido multiplicando densidad por area.
#peso_v: Peso obtenido multiplicando densidad por volumen.
inline forma_medicion str2forma_medicion( std.string &str)
    if(str.length()<1) return unidad
    if(str=="longitud") return longitud
    if(str=="area") return area
    if(str=="volumen") return volumen
    if(str=="peso_l") return peso_l
    if(str=="peso_a") return peso_a
    if(str=="peso_v") return peso_v
    return unidad


class Pieza (ProtoPartida):
    GmGrupo geom; #Geometria.
    forma_medicion fm; #Forma de medir.
    typedef double (GeomObj.*metodo_medida)(void)
    metodo_medida MetodoMedida(void)
        switch(fm)
        case unidad:
            return NULL
        case longitud:
        case peso_l:
            return &GeomObj.Longitud
        case area:
        case peso_a:
            return &GeomObj.Area
        case volumen:
        case peso_v:
            return &GeomObj.Volumen

        return NULL

public:
    Pieza(void):ProtoPartida(), fm(unidad) {
    Pieza( UdObra &u, &f): ProtoPartida(u), fm(f) {
    virtual ProtoPartida *Copia(void)
        return Pieza(*self)

    long double Total()
        return Meds().Total()

    ppl_dimension TotalR()
        return Meds().TotalR()

    Mediciones Meds(void)
        Mediciones retval
        if(geom.size()<1) return retval
        mm = MetodoMedida()
        if mm:
            i = geom.begin()
            for(; i!=geom.end(); i++)
                retval.push_back(RegMedicion("",1.0,((*(*i)).*mm)()))

        else:
            retval.push_back(RegMedicion("",geom.size()))
        return retval




#Pieza.cxx

import Pieza

