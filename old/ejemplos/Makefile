           SHELL = /bin/sh

               AR = ar rs
               CC = g++
           RANLIB = ranlib
               RM = rm -f
FLAGS = -Wall -D_GNU_SOURCE -Wno-sign-compare -fno-implicit-templates -L/home/luisc/fuentes/c/libreria/lib
FLAGS_MODULES = $(FLAGS) -frepo -c

HDRS = ../src/DatosPpl.hxx EntPpl.hxx CuaPre.hxx Descompuestos.hxx Medible.hxx CompBC3.hxx UdObra.hxx ComptesBC3.hxx Currency.hxx CodigosObra.hxx Codigos.hxx MedsCap.hxx ProtoPartida.hxx Partida.hxx Pieza.hxx fiebdc3.h Mediciones.hxx RegMedicion.hxx

OBJS = ../lib/Obra.o ../lib/Capitulo.o ../lib/Subcapitulos.o ../lib/DatosPpl.o ../lib/Descompuestos.o ../lib/CuaPre.o ../lib/Elemento.o ../lib/Elementos.o ../lib/EntFR.o ../lib/Medible.o ../lib/Mediciones.o ../lib/MedsCap.o ../lib/Partida.o ../lib/Pieza.o ../lib/Porcentajes.o ../lib/UdObra.o ../lib/Codigos.o ../lib/CodigosObra.o ../lib/CompBC3.o ../lib/ProtoPartida.o ../lib/EntBC3.o ../lib/RegMedicion.o ../lib/templates.o

all:: ../ppl2hcalc 

../ppl2hcalc: $(OBJS) ppl2hcalc.cxx
	$(CC) $(FLAGS) ppl2hcalc.cxx $(OBJS) -o ../ppl2hcalc -lAlgebra -lgeom -lCoin

clean:
	rm -f ../lib/*.o ../lib/*.rpo

