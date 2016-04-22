//Tipos.h
//Tipos de datos básicos.

#ifndef TIPOS_H
#define TIPOS_H

#include "Currency.h"

typedef Currency<3> ppl_dimension;
typedef Currency<2> ppl_precio; //Para euros dos decimales.
typedef Currency<2> ppl_precio2; //precio con dos decimales.
typedef Currency<3> ppl_precio3; //precio con tres decimales.
typedef Currency<4> ppl_precio4; //precio con cuatro decimales.
typedef Currency<3> ppl_porcentaje;

#endif
