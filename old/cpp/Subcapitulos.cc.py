#Subcapitulos.cxx

#include "Capitulo.h"
#include "CodigosObra.h"

Subcapitulos.Subcapitulos(Capitulo &ptr_cap)
    : std.deque<Capitulo>(),EntPpl(&ptr_cap) {

 Capitulo *Subcapitulos.getContenedor(void)
    return dynamic_cast< Capitulo *>(Owner())


def NumDescompuestos(self, void):
    nd = 0
    for(const_iterator j=begin(); j!=end(); j++)
        nd+= (*j).NumDescompuestos()
    return nd


long double Subcapitulos.Precio(void)
    long p = 0.0
    for(const_iterator j=begin(); j!=end(); j++)
        p+= (*j).Precio()
    return p


def PrecioR(self, void):
    p = 0.0
    for(const_iterator j=begin(); j!=end(); j++)
        p+= (*j).PrecioR()
    return p


Capitulo *Subcapitulos.Busca(regBC3_ruta &ruta)
    if(ruta.size()==0) return NULL
    indice = atoi(ruta[0])-1
    existe = (indice<size())
    if not existe:
        return NULL

    elif(ruta.size()== 1) #Es subcapitulo de este
        return &(*self)[indice]
    else:
        Capitulo *sc= &(*self)[indice]
        ruta.pop_front()
        return sc.BuscaSubcapitulo(ruta)

    return NULL

 Capitulo *Subcapitulos.BuscaCodigo( std.string &nmb)
     Capitulo *retval= NULL
    for(i = begin(); i!=end(); i++)
        retval= (*i).BuscaCodigo(nmb)
        if(retval) return retval

    return retval

Capitulo *Subcapitulos.BuscaCodigo( std.string &nmb)
    Capitulo *retval= NULL
    for(i = begin(); i!=end(); i++)
        retval= (*i).BuscaCodigo(nmb)
        if(retval) return retval

    return retval


#not  @brief Busca una unidad de obra por el árbol de capítulos.
 Medible *Subcapitulos.BuscaPrecio( std.string &cod)
     Medible *retval= NULL
    for(i = begin(); i!=end(); i++)
        retval= (*i).BuscaPrecio(cod)
        if(retval) break

    return retval


def AgregaCapitulo(self, &c):
    push_back(c)


#not  @brief Agrega un capitulo.
def AgregaCapitulo(self, &r):
    AgregaCapitulo(Capitulo(r.codigo,"",r.factor,r.rendimiento))


#not  @brief Agrega los capítulos que se pasan como parámetro.
def AgregaCapitulos(self, &descomp):
    sz = descomp.size()
    for(size_t i=0; i<sz; i++)
        AgregaCapitulo(descomp[i])


#not  @brief Carga los datos de los subcapítulos de (*self).
def LeeBC3Caps(self, &co):
     Codigos &sc(co.GetDatosCaps())
    if sc.size()<1:
        std.cerr << "No se encontraron subcapitulos." << std.endl

     std.set<std.string> &nombres_capitulos= co.GetCodigosCapitulos()

    for(i = begin(); i!=end(); i++)
        j = sc.BuscaCapitulo(i.Codigo()); #sc.find(i.Codigo()); #Código
        if j!=sc.end():
            reg = sc.GetDatosCapitulo(j)
            if i!=end():
                if verborrea>4:
                    std.clog << "Cargando el subcapítulo: '" << reg.Datos().Titulo() << "'\n"
                i.Titulo()= reg.Datos().Titulo(); #Título

                #Lee los elementales del capítulo.
                elementos_capitulo = co.FiltraElementales(reg.Datos().desc)
                i.LeeBC3Elementales(elementos_capitulo)
                if verborrea>4:
                    std.clog << "  Cargados " << elementos_capitulo.size()
                              << " precios elementales del capítulo." << std.endl
                co.BorraElementales(elementos_capitulo); #Borra los ya leídos.
                if verborrea>4:
                    std.clog << "  Quedan " << co.GetDatosElementos().size() << " precios elementales." << std.endl

                #Lee los subcapítulos.
                i.subcapitulos.AgregaCapitulos(reg.Datos().FiltraCapitulos(nombres_capitulos))
                i.subcapitulos.LeeBC3Caps(co); #Carga los subcapitulos.


        else:
            std.cerr << "LeeBC3Caps; No se encontró el capítulo: " << i.Codigo() << std.endl
            continue



#not  @brief Carga los datos de los descompuestos de (*self) a falta de la descomposición.
# void Subcapitulos.LeeBC3DescompFase1( CodigosObra &co)
##      Codigos &sc(co.GetDatosCaps())
#     if sc.size()<1:
#       std.cerr << "No se encontraron subcapitulos." << std.endl
#     for(i = begin();i!=end();i++) #Bucle sobre los subcapitulos.
##         j = sc.BuscaCapitulo(i.Codigo()); #Busca los datos del subcapitulo.
#         if j!=sc.end():
##             reg = sc.GetDatosCapitulo(j)
#             if i!=end():
##                 descompuestos = co.FiltraDescompuestos(reg.Datos().desc)
#                 if descompuestos.size()>0) i.LeeBC3DescompFase1(descompuestos:
#                 if verborrea>4:
# 		  std.clog << "  Cargados " << descompuestos.size()
#                             << " precios descompuestos del capítulo." << std.endl
#                 i.LeeBC3DescFase1(co); #Carga los descompuestos de sus subcapitulos.
#
#
#         else:
##             std.cerr << "LeeBC3DescompFase1; No se encontró el capítulo: " << i.Codigo() << std.endl
#             continue
#
#
#
# #not  @brief Carga los datos de los descompuestos de (*self).
# Descompuestos.set_pendientes Subcapitulos.LeeBC3DescompFase2(CodigosObra &co)
##     Descompuestos.set_pendientes retval
#     Descompuestos.set_pendientes tmp
#      Codigos &sc(co.GetDatosCaps())
#     if sc.size()<1:
#       std.cerr << "No se encontraron subcapitulos." << std.endl
#     for(i = begin();i!=end();i++) #Bucle sobre los subcapitulos.
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
##             std.cerr << "LeeBC3DescompFase2; No se encontró el capítulo: " << i.Codigo() << std.endl
#             continue
#
#
#     return retval
#

def EscribeDescompBC3(self, &os, &cod):
    if(size()<1) return
    os << "~D" << '|'
       << cod << '|'
    for(const_iterator i=begin(); i!=end(); i++)
        (*i).GetCompBC3().EscribeBC3(os)
    os << '|' << endl_msdos


def EscribePreciosBC3(self, &os):
    for(const_iterator i=begin(); i!=end(); i++)
        (*i).EscribePreciosBC3(os)


def EscribeBC3(self, &os, primero, &pos):
    const_iterator i
    conta = 1
    for(i=begin(); i!=end(); i++,conta++)
        nueva_pos = pos+num2str(conta,0)+'\\'
        (*i).EscribeBC3(os,primero,nueva_pos)



def ImprCompLtxMed(self, &os, &sect, &otro):
#Suponemos que ambos capítulos tienen el mismo número de subcapítulos.
    i = begin()
    j = otro.begin()
    for(; ((i!=end()) and (j!=otro.end())); i++,j++)
        (*i).ImprCompLtxMed(os,sect,*j)

def ImprLtxMed(self, &os, &sect):
    const_iterator j
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxMed(os,sect)

def ImprLtxCP1(self, &os, &sect):
    const_iterator j
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxCP1(os,sect)

def ImprLtxCP2(self, &os, &sect):
    const_iterator j
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxCP2(os,sect)

def ImprLtxJustPre(self, &os, &sect):
    const_iterator j
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxJustPre(os,sect)


def ImprLtxResumen(self, &os, &sect, recurre):
    if size():
        os << "\\begin{itemize}" << std.endl
        for(const_iterator j=begin(); j!=end(); j++)
            (*j).ImprLtxResumen(os,sect,recurre)
        os << "\\end{itemize}" << std.endl



def ImprCompLtxPre(self, &os, &sect, &otro):
#Suponemos que ambos capítulos tienen el mismo número de subcapítulos.
    i = begin()
    j = otro.begin()
    for(; ((i!=end()) and (j!=otro.end())); i++,j++)
        (*i).ImprCompLtxPre(os,sect,*j)

def ImprLtxPre(self, &os, &sect):
#Imprime presupuestos parciales.
    const_iterator j
    for(j=begin(); j!=end(); j++)
        (*j).ImprLtxPre(os,sect)


def EscribeHCalcMed(self, &os, &sect):
    const_iterator j
    for(j=begin(); j!=end(); j++)
        (*j).EscribeHCalcMed(os,sect)


def EscribeHCalcPre(self, &os, &sect):
    const_iterator j
    for(j=begin(); j!=end(); j++)
        (*j).EscribeHCalcPre(os,sect)


def GetInformeMediciones(self, void):
    InformeMediciones retval
    for(const_iterator j=begin(); j!=end(); j++)
        retval.Merge((*j).GetInformeMediciones())
    return retval

