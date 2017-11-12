# -*- coding: utf-8 -*-
#EntFR.py

import EntPyCost
import basic_types

def std.string rdto2str(d):
    return num2str(d,13)


class EntFR(EntPyCost):
#Entidad que tiene factor y rendimiento.
private:
    float factor
    double rendimiento
public:
    EntFR( float &f= 1.0, &r=0.0)
     float &Factor()
        return factor

    float &Factor()
        return factor

     double &Rendimiento()
        return rendimiento

    double &Rendimiento()
        return rendimiento

    double Producto()
    double ProductoR()
     WriteSpre(os)
     WriteBC3(os)



#EntFR.cxx

import EntFR

EntFR.EntFR( float &f, &r)
    :factor(f),rendimiento(r) {

def Producto(self, ):
    return factor*rendimiento

def ProductoR(self, ):
    return ppl_precio4(factor*rendimiento)

def WriteSpre(self, &os):
    os.write(rdto2str(Producto()) + '|'

def WriteBC3(self, &os):
    os.write(factor + '\\' + rdto2str(rendimiento) + '\\'


