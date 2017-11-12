#Pieza.py
#Figura geométrica llena de una unidad de obra.




import ProtoPartida
import matemat/geom-2.0/src/listas/GmGrupo

#Metodo de medida
typedef enum {unidad,longitud,area,volumen,peso_l,peso_a,peso_v} forma_medicion
#peso_l: Peso obtenido multiplicando densidad por longitud.
#peso_a: Peso obtenido multiplicando densidad por area.
#peso_v: Peso obtenido multiplicando densidad por volumen.
def forma_medicion str2forma_medicion( Str):
    if(len(Str)<1) return unidad
    if(Str=="longitud") return longitud
    if(Str=="area") return area
    if(Str=="volumen") return volumen
    if(Str=="peso_l") return peso_l
    if(Str=="peso_a") return peso_a
    if(Str=="peso_v") return peso_v
    return unidad


class Pieza (ProtoPartida):
    GmGrupo geom; #Geometria.
    forma_medicion fm; #Forma de medir.
    typedef double (GeomObj.*metodo_medida)()
    metodo_medida MetodoMedida()
        switch(fm)
        case unidad:
            return None
        case longitud:
        case peso_l:
            return GeomObj.Longitud
        case area:
        case peso_a:
            return GeomObj.Area
        case volumen:
        case peso_v:
            return GeomObj.Volumen

        return None

public:
    Pieza():ProtoPartida(), fm(unidad) {
    Pieza( UdObra &u, f): ProtoPartida(u), fm(f) {
    def ProtoPartida *Copia():
        return Pieza(self)

    long double Total()
        return Meds().Total()

    ppl_dimension TotalR()
        return Meds().TotalR()

    Mediciones Meds()
        Mediciones retval
        if(geom.size()<1) return retval
        mm = MetodoMedida()
        if mm:
            i = geom.begin()
            for(; i!=geom.end(); i+= 1)
                retval.append(RegMedicion("",1.0,((*(i)).*mm)()))

        else:
            retval.append(RegMedicion("",geom.size()))
        return retval




#Pieza.cxx

import Pieza

