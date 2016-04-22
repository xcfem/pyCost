#Mediciones.h
#ifndef MEDICIONES_H
#define MEDICIONES_H

import RegMedicion

#not  @brief Mediciones de una unidad de obra
class Mediciones(std.deque<RegMedicion>, EntPyCost):
public:
    typedef std.deque<RegMedicion> dq_reg_med

    double TotalUnidades(void)
    double TotalLargo(void)
    double TotalAncho(void)
    double TotalAlto(void)
    long double Total(void)
    ppl_dimension TotalR(void)

    void LeeBC3( regBC3_lista_med &m)
    void EscribeBC3(std.ostream &os)
    void ImprCompLtx(std.ostream &os, &otra)
    void ImprCompLtx(std.ostream &os)
    void ImprLtx(std.ostream &os)
    void EscribeHCalc(std.ostream &os)


#endif
#Mediciones.cxx

import Mediciones

#not  @brief Devuelve el total de unidades de la medición.
def TotalUnidades(self, void):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades()
    return t


#not  @brief Devuelve el total del largo de la medición.
def TotalLargo(self, void):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades()*(*i).Largo()
    return t


#not  @brief Devuelve el total del ancho de la medición.
def TotalAncho(self, void):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades()*(*i).Ancho()
    return t


#not  @brief Devuelve el total del alto de la medición.
def TotalAlto(self, void):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).Unidades()*(*i).Ancho()
    return t


long double Mediciones.Total(void)
    long t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).Total()
    return t

def TotalR(self, void):
    t = 0.0
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        t+=(*i).TotalR()
    return t


#| @brief Lee la lista de mediciones.
def LeeBC3(self, &m):
    RegMedicion rm
    for(i = m.begin(); i!=m.end(); i++)
        rm.LeeBC3(*i)
        push_back(rm)



def EscribeBC3(self, &os):
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        (*i).EscribeBC3(os)

def ImprCompLtx(self, &os, &otra):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd
    dq_reg_med.const_iterator i=begin()
    dq_reg_med.const_iterator j=otra.begin()
    for(; ((i!=end()) and (j!=otra.end())); i++,j++)
        (*j).ImprLtx(os,"p{1.5cm}")
        os << ltx_ampsnd
        (*i).ImprLtx(os,"p{1.5cm}")
        os << ltx_fin_reg << std.endl

    if i!=end():
        for(; i!=end(); i++)
            os << media_linea_en_blanco
            os << ltx_ampsnd
            (*i).ImprLtx(os,"p{1.5cm}")
            os << ltx_fin_reg << std.endl

    elif j!=end():
        for(; j!=otra.end(); j++)
            (*j).ImprLtx(os,"p{1.5cm}")
            os << media_linea_en_blanco << ltx_fin_reg << std.endl

    os << linea_en_blanco << std.endl

def ImprCompLtx(self, &os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
                                       ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
     media_linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+
            ltx_ampsnd+ltx_ampsnd+ltx_ampsnd
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        os << media_linea_en_blanco
        (*i).ImprLtx(os,"p{1.5cm}")
        os << ltx_fin_reg << std.endl

    os << linea_en_blanco << std.endl

def ImprLtx(self, &os):
     linea_en_blanco = ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_ampsnd+ltx_fin_reg
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        (*i).ImprLtx(os,"p{3.5cm}")
        os << ltx_fin_reg << std.endl

    os << linea_en_blanco << std.endl

def EscribeHCalc(self, &os):
    dq_reg_med.const_iterator i
    for(i=begin(); i!=end(); i++)
        (*i).EscribeHCalc(os)
    os << ",,,,Suma ..." << tab << Total() << std.endl << std.endl

