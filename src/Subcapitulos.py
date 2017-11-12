#Subcapitulos.py




import Descompuestos

class Capitulo
class CodigosObra

class Subcapitulos(std.deque<Capitulo>, EntPyCost):
public:
    typedef std.deque<Capitulo> dq_cap
    Subcapitulos(Capitulo &ptr_cap)
    long double Precio()
    ppl_precio PrecioR()
    Capitulo *Busca(regBC3_ruta &ruta)
     Capitulo *BuscaCodigo( nmb)
    Capitulo *BuscaCodigo( nmb)
    size_t NumDescompuestos()
     Measurable *BuscaPrecio( cod)

     Capitulo *getContenedor()

     AgregaCapitulo( Capitulo &c)
     AgregaCapitulo( regBC3_desc &r)
     AgregaCapitulos( regBC3_d &descomp)

     LeeBC3Caps(CodigosObra &co)
     WritePreciosBC3(os)
     WriteDescompBC3(os, cod)
     WriteBC3(os, primero= "False", pos="")

     ImprCompLtxMed(os, sect, otro)
     ImprLtxMed(os, sect)
     ImprLtxCP1(os, sect)
     ImprLtxCP2(os, sect)
     ImprLtxJustPre(os, sect)
     ImprLtxResumen(os, sect, recurre= True)
     ImprCompLtxPre(os, sect, otro)
     ImprLtxPre(os, sect)
     WriteHCalcMed(os, sect)
     WriteHCalcPre(os, sect)
    InformeMediciones GetInformeMediciones()



#Subcapitulos.cxx

import Capitulo
import CodigosObra

Subcapitulos.Subcapitulos(Capitulo &ptr_cap)
    : std.deque<Capitulo>(),EntPyCost(&ptr_cap) {

 Capitulo *Subcapitulos.getContenedor()
    return dynamic_cast< Capitulo *>(Owner())


def NumDescompuestos(self):
    nd = 0
    for(const_iterator j=begin(); j!=end(); j+= 1)
        nd+= (j).NumDescompuestos()
    return nd


long double Subcapitulos.Precio()
    long p = 0.0
    for(const_iterator j=begin(); j!=end(); j+= 1)
        p+= (j).Precio()
    return p


def PrecioR(self):
    p = 0.0
    for(const_iterator j=begin(); j!=end(); j+= 1)
        p+= (j).PrecioR()
    return p


Capitulo *Subcapitulos.Busca(regBC3_ruta &ruta)
    if(ruta.size()==0) return None
    indice = atoi(ruta[0])-1
    existe = (indice<size())
    if not existe:
        return None

    elif(ruta.size()== 1) #Es subcapitulo de este
        return &(self)[indice]
    else:
        Capitulo *sc= &(self)[indice]
        ruta.pop_front()
        return sc.BuscaSubcapitulo(ruta)

    return None

 Capitulo *Subcapitulos.BuscaCodigo( nmb)
     Capitulo *retval= None
    for(i = begin(); i!=end(); i+= 1)
        retval= (i).BuscaCodigo(nmb)
        if(retval) return retval

    return retval

Capitulo *Subcapitulos.BuscaCodigo( nmb)
    Capitulo *retval= None
    for(i = begin(); i!=end(); i+= 1)
        retval= (i).BuscaCodigo(nmb)
        if(retval) return retval

    return retval


#not  @brief Busca una unidad de obra por el árbol de capítulos.
 Measurable *Subcapitulos.BuscaPrecio( cod)
     Measurable *retval= None
    for(i = begin(); i!=end(); i+= 1)
        retval= (i).BuscaPrecio(cod)
        if(retval) break

    return retval


def AgregaCapitulo(self, c):
    append(c)


#not  @brief Agrega un capitulo.
def AgregaCapitulo(self, r):
    AgregaCapitulo(Capitulo(r.codigo,"",r.factor,r.rendimiento))


#not  @brief Agrega los capítulos que se pasan como parámetro.
def AgregaCapitulos(self, descomp):
    sz = descomp.size()
    for(size_t i=0; i<sz; i+= 1)
        AgregaCapitulo(descomp[i])


#not  @brief Carga los datos de los subcapítulos de (self).
def LeeBC3Caps(self, co):
     Codigos &sc(co.GetDatosCaps())
    if sc.size()<1:
        lmsg.error("No se encontraron subcapitulos." + '\n')

     std.set<std.string> &nombres_capitulos= co.GetCodigosCapitulos()

    for(i = begin(); i!=end(); i+= 1)
        j = sc.BuscaCapitulo(i.Codigo()); #sc.find(i.Codigo()); #Código
        if j!=sc.end():
            reg = sc.GetDatosCapitulo(j)
            if i!=end():
                if verborrea>4:
                    logging.info("Cargando el subcapítulo: '" + reg.Datos().Titulo() + "'\n")
                i.Titulo()= reg.Datos().Titulo(); #Título

                #Lee los elementales del capítulo.
                elementos_capitulo = co.FiltraElementales(reg.Datos().desc)
                i.LeeBC3Elementales(elementos_capitulo)
                if verborrea>4:
                    logging.info("  Cargados " + elementos_capitulo.size())
                              + " precios elementales del capítulo." + '\n'
                co.BorraElementales(elementos_capitulo); #Borra los ya leídos.
                if verborrea>4:
                    logging.info("  Quedan " + co.GetDatosElementos().size() + " precios elementales." + '\n')

                #Lee los subcapítulos.
                i.subcapitulos.AgregaCapitulos(reg.Datos().FiltraCapitulos(nombres_capitulos))
                i.subcapitulos.LeeBC3Caps(co); #Carga los subcapitulos.


        else:
            lmsg.error("LeeBC3Caps; No se encontró el capítulo: " + i.Codigo() + '\n')
            continue



#not  @brief Carga los datos de los descompuestos de (self) a falta de la descomposición.
#  Subcapitulos.LeeBC3DescompFase1( CodigosObra &co)
##      Codigos &sc(co.GetDatosCaps())
#     if sc.size()<1:
#       lmsg.error("No se encontraron subcapitulos." + '\n')
#     for(i = begin();i!=end();i+= 1) #Bucle sobre los subcapitulos.
##         j = sc.BuscaCapitulo(i.Codigo()); #Busca los datos del subcapitulo.
#         if j!=sc.end():
##             reg = sc.GetDatosCapitulo(j)
#             if i!=end():
##                 descompuestos = co.FiltraDescompuestos(reg.Datos().desc)
#                 if descompuestos.size()>0) i.LeeBC3DescompFase1(descompuestos:
#                 if verborrea>4:
# 		  logging.info("  Cargados " + descompuestos.size())
#                             + " precios descompuestos del capítulo." + '\n'
#                 i.LeeBC3DescFase1(co); #Carga los descompuestos de sus subcapitulos.
#
#
#         else:
##             lmsg.error("LeeBC3DescompFase1; No se encontró el capítulo: " + i.Codigo() + '\n')
#             continue
#
#
#
# #not  @brief Carga los datos de los descompuestos de (self).
# Descompuestos.set_pendientes Subcapitulos.LeeBC3DescompFase2(CodigosObra &co)
##     Descompuestos.set_pendientes retval
#     Descompuestos.set_pendientes tmp
#      Codigos &sc(co.GetDatosCaps())
#     if sc.size()<1:
#       lmsg.error("No se encontraron subcapitulos." + '\n')
#     for(i = begin();i!=end();i+= 1) #Bucle sobre los subcapitulos.
##         j = sc.BuscaCapitulo(i.Codigo())
#         if j!=sc.end():
##             reg = sc.GetDatosCapitulo(j); #Busca los datos del subcapitulo.
#             if i!=end():
##                 descompuestos = co.FiltraDescompuestos(reg.Datos().desc)
#                 if descompuestos.size()>0:
##                     tmp= i.LeeBC3DescompFase2(descompuestos)
#                     retval.insert(tmp.begin(),tmp.end())
#
#                 co.BorraDescompuestos(descompuestos); #Borra los ya leídos.
#                 tmp= i.LeeBC3DescFase2(co); #Carga los descompuestos de sus subcapitulos.
#                 retval.insert(tmp.begin(),tmp.end())
#
#
#         else:
##             lmsg.error("LeeBC3DescompFase2; No se encontró el capítulo: " + i.Codigo() + '\n')
#             continue
#
#
#     return retval
#

def WriteDescompBC3(self, os, cod):
    if(size()<1) return
    os.write("~D" + '|'
       + cod + '|'
    for(const_iterator i=begin(); i!=end(); i+= 1)
        (i).GetCompBC3().WriteBC3(os)
    os.write('|' + endl_msdos


def WritePreciosBC3(self, os):
    for(const_iterator i=begin(); i!=end(); i+= 1)
        (i).WritePreciosBC3(os)


def WriteBC3(self, os, primero, pos):
    const_iterator i
    conta = 1
    for(i=begin(); i!=end(); i+= 1,conta+= 1)
        nueva_pos = pos+num2str(conta,0)+'\\'
        (i).WriteBC3(os,primero,nueva_pos)



def ImprCompLtxMed(self, os, sect, otro):
#Suponemos que ambos capítulos tienen el mismo número de subcapítulos.
    i = begin()
    j = otro.begin()
    for(; ((i!=end()) and (j!=otro.end())); i+= 1,j+= 1)
        (i).ImprCompLtxMed(os,sect,*j)

def ImprLtxMed(self, os, sect):
    const_iterator j
    for(j=begin(); j!=end(); j+= 1)
        (j).ImprLtxMed(os,sect)

def ImprLtxCP1(self, os, sect):
    const_iterator j
    for(j=begin(); j!=end(); j+= 1)
        (j).ImprLtxCP1(os,sect)

def ImprLtxCP2(self, os, sect):
    const_iterator j
    for(j=begin(); j!=end(); j+= 1)
        (j).ImprLtxCP2(os,sect)

def ImprLtxJustPre(self, os, sect):
    const_iterator j
    for(j=begin(); j!=end(); j+= 1)
        (j).ImprLtxJustPre(os,sect)


def ImprLtxResumen(self, os, sect, recurre):
    if size():
        os.write("\\begin{itemize}" + '\n'
        for(const_iterator j=begin(); j!=end(); j+= 1)
            (j).ImprLtxResumen(os,sect,recurre)
        os.write("\\end{itemize}" + '\n'



def ImprCompLtxPre(self, os, sect, otro):
#Suponemos que ambos capítulos tienen el mismo número de subcapítulos.
    i = begin()
    j = otro.begin()
    for(; ((i!=end()) and (j!=otro.end())); i+= 1,j+= 1)
        (i).ImprCompLtxPre(os,sect,*j)

def ImprLtxPre(self, os, sect):
#Imprime presupuestos parciales.
    const_iterator j
    for(j=begin(); j!=end(); j+= 1)
        (j).ImprLtxPre(os,sect)


def WriteHCalcMed(self, os, sect):
    const_iterator j
    for(j=begin(); j!=end(); j+= 1)
        (j).WriteHCalcMed(os,sect)


def WriteHCalcPre(self, os, sect):
    const_iterator j
    for(j=begin(); j!=end(); j+= 1)
        (j).WriteHCalcPre(os,sect)


def GetInformeMediciones(self):
    InformeMediciones retval
    for(const_iterator j=begin(); j!=end(); j+= 1)
        retval.Merge((j).GetInformeMediciones())
    return retval

