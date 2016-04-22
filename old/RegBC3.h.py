#RegBC3.h

#ifndef RegBC3_H
#define RegBC3_H

#include <string>
#include "fiebdc3.h"

enum TipoConcepto {elemento, descompuesto, medicion, obra, capitulo, sin_tipo

struct RegBC3
    std.string c; #not  <Concepto
    std.string d; #not  <Descomposición.
    std.string m; #not  <Medicion
    std.string t; #not  <Texto
    std.string y; #not  <Descomposición.

    struct campos_reg
        StrTok.dq_campos campos_c
        StrTok.dq_campos campos_d
        StrTok.dq_campos campos_m
        StrTok.dq_campos campos_t

    regBC3_c GetConcepto(void)
    regBC3_t GetTexto(void)
    regBC3_d GetDesc(void)
    regBC3_m GetMed(void)
    bool EsElemento(void)
    bool EsMedicion(void)
    bool EsObra(void)
    bool EsCapitulo(void)
    regBC3_elemento GetDatosElemento(void)
        return regBC3_elemento(GetConcepto(),GetTexto())

    regBC3_udobra GetDatosUdObra(void)
        return regBC3_udobra(GetConcepto(),GetTexto(),GetDesc())

    regBC3_capitulo GetDatosCapitulo(void)
    regBC3_medicion GetDatosMedicion(void)
        return regBC3_medicion(GetConcepto(),GetTexto(),GetMed())

    friend std.ostream &operator<<(std.ostream &os, &r)


std.ostream &operator<<(std.ostream &os, &r)

#endif
