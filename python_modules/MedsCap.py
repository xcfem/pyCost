#MedsCap.h
#Mediciones de un capítulo.

#ifndef MEDSCAP_H
#define MEDSCAP_H

import Partida
import InformeMediciones
import bibXCBasica/src/stl/poli_deque
#import Pieza


class MedsCap(poli_deque<ProtoPartida>, EntPyCost):
    typedef poli_deque<ProtoPartida> dq_med
public:
    long double Precio(void)
    ppl_precio PrecioR(void)
    std.string StrPrecioLtx(void)
        return PrecioR().EnHumano()

    void Escribe(std.ostream &os, &cod, &pos="")
    void EscribeDescompBC3(std.ostream &os, &cod)
    void ImprCompLtxMed(std.ostream &os, &otra)
    void ImprLtxMed(std.ostream &os)
    void ImprCompLtxPre(std.ostream &os, &tit, &otra, &tit_otra)
    void ImprLtxPre(std.ostream &os, &tit)
    #Imprime presupuestos parciales.
    void EscribeHCalcMed(std.ostream &os)
    void EscribeHCalcPre(std.ostream &os)
    InformeMediciones GetInformeMediciones(void)


#endif
#MedsCap.cxx

import MedsCap


long double MedsCap.Precio(void)
    long t = 0.0
    const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).Precio()
    return t

def PrecioR(self, void):
    ppl_precio t(0.0)
    const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).PrecioR()
    return t

def Escribe(self, &os, &cod, &pos):
    const_iterator i
    contador = 1
    for(i=begin(); i!=end(); i++,contador++)
        pos_med = pos + num2str(contador,0) + '\\'
        (*i).EscribeBC3(os,cod,pos_med)


def EscribeDescompBC3(self, &os, &cod):
    if(size()<1) return
    os << "~D" << '|' #Antes estaba con ~Y (daba problemas)
       << cod << '|'
    for(i = begin(); i!=end(); i++)
        os << (*i).CodigoUdObra() << "\\1\\" #factor 1
           << (*i).Total() << '\\'
    os << '|' << endl_msdos

def ImprCompLtxMed(self, &os, &otra):
    if size():
        os << ltx_tiny << std.endl
        os << ltx_begin("longtable}{lrrrrr|lrrrrr") << std.endl
           << "\\multicolumn{6}{c|}{\\normalsize\\textbf{Proyecto de construcción}\\tiny} &"
           << "\\multicolumn{6}{c}{\\normalsize\\textbf{Proyecto modificado}\\tiny} \\\\"
           << std.endl << ltx_hline << std.endl
           << ltx_endhead << std.endl
           << "\\multicolumn{12}{r}{../..}\\\\" << std.endl
           << ltx_endfoot << std.endl
           << ltx_endlastfoot << std.endl
        const_iterator i
        for(i=begin(); i!=end(); i++)
             cod = (*i).CodigoUdObra()
            const_iterator j
            for(j=otra.begin(); j!=otra.end(); j++)
                if(cod == (*j).CodigoUdObra()) break
            if(j!=otra.end()) #La encotró
                (*i).ImprCompLtxMed(os,*(*j))
            else:
                (*i).ImprCompLtxMed(os)

        os << "\\end{longtable}" << std.endl
        os << ltx_normalsize << std.endl


def ImprLtxMed(self, &os):
    if size():
        os << ltx_small << std.endl
        os << "\\begin{longtable}{lrrrrr}" << std.endl
           << "\\multicolumn{6}{r}{../..}\\\\" << std.endl
           << "\\endfoot" << std.endl
           << "\\endlastfoot" << std.endl
        const_iterator i
        for(i=begin(); i!=end(); i++)
            (*i).ImprLtxMed(os)
        os << "\\end{longtable}" << std.endl
        os << ltx_normalsize << std.endl


def ImprCompLtxPre(self, &os, &tit, &otra, &tit_otra):
    if size():
        os << ltx_tiny << std.endl
        os << ltx_begin("longtable}{lrlrr|lrlrr") << std.endl
           << "\\multicolumn{5}{c|}{\\normalsize\\textbf{Proyecto de construcción}\\tiny} &"
           << "\\multicolumn{5}{c}{\\normalsize\\textbf{Proyecto modificado}\\tiny} \\\\"
           << std.endl << ltx_hline << std.endl
           << "Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{P. unitario} & Importe & Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{P. unitario} & Importe \\\\" << std.endl
           << ltx_hline << std.endl
           << ltx_endhead << std.endl
           << "\\multicolumn{10}{r}{../..}\\\\" << std.endl
           << ltx_endfoot << std.endl
           << ltx_endlastfoot << std.endl
        const_iterator i
        for(i=begin(); i!=end(); i++)
             cod = (*i).CodigoUdObra()
            const_iterator j
            for(j=otra.begin(); j!=otra.end(); j++)
                if(cod == (*j).CodigoUdObra()) break
            if(j!=otra.end()) #La encotró
                (*i).ImprCompLtxPre(os,*(*j))
            else:
                (*i).ImprCompLtxPre(os)

        os << "\\multicolumn{4}{p{8cm}}{\\textbf{Total: "
           << tit_otra << "}} & \\textbf{" << otra.StrPrecioLtx() << "} & " << std.endl
        os << "\\multicolumn{4}{p{8cm}}{\\textbf{Total: "
           << tit << "}} & \\textbf{" << StrPrecioLtx() << "}\\\\" << std.endl
        os << "\\end{longtable}" << std.endl
        os << ltx_normalsize << std.endl


def ImprLtxPre(self, &os, &tit):
#Imprime presupuestos parciales.
    if size():
        os << ltx_small << std.endl
        os << "\\begin{longtable}{lrlrr}" << std.endl
           << "Partida & Cantidad & Descripción & \\multicolumn{1}{p{1.5cm}}{Precio unitario} & Importe \\\\" << std.endl
           << "\\hline" << std.endl
           << "\\endhead" << std.endl
           << "\\multicolumn{5}{r}{../..}\\\\" << std.endl
           << "\\endfoot" << std.endl
           << "\\endlastfoot" << std.endl
        for(const_iterator i=begin(); i!=end(); i++)
            (*i).ImprLtxPre(os)
        os << "\\multicolumn{4}{p{8cm}}{\\textbf{Total: " << tit << "}} & \\textbf{" << StrPrecioLtx() << "}\\\\" << std.endl
        os << "\\end{longtable}" << std.endl
        os << ltx_normalsize << std.endl


def EscribeHCalcMed(self, &os):
    if size():
        const_iterator i
        for(i=begin(); i!=end(); i++)
            (*i).EscribeHCalcMed(os)


def EscribeHCalcPre(self, &os):
    if size():
        const_iterator i
        for(i=begin(); i!=end(); i++)
            (*i).EscribeHCalcPre(os)



def GetInformeMediciones(self, void):
    InformeMediciones retval
    for(i = begin(); i!=end(); i++)
        retval.Inserta((*i).Informe())
    return retval

