#include <windows.h>
#include <stdio.h>
#include <stdarg.h>

#include "Base.h"

short ABPH_1 (Cfiebdc &par, short operacion) {

	INI (operacion);
	COD ("ABPH.1$");

	if (operacion == LEE) {
		PAR ("RESISTENCIA", "H-50", "H-100", "H-125", "H-150", "H-175", "");
		PAR ("CONSISTENCIA", "plástica", "blanda", "");
		PAR ("Tmax", "18", "38", "78", "");
		return TRUE;
	}

	else if (operacion == CALCULA) {

		// plástica				H50		H100	H125	H150	H175
		double T[2][3][5] ={	.180,	.255,	.290,	.330,	.365,	//18
								.160,	.225,	.260,	.290,	.325,	//38
								.140,	.200,	.225,	.255,	.285,	//78
		// blanda
								.210,	.290,	.330,	.375,	.000,
								.185,	.260,	.300,	.335,	.375,
								.165,	.235,	.265,	.300,	.335 };
   	
		if (!T[B][C][A]) return ERR ("Combinación no permitida");
   	
		double U[2][3]= {		.180,	.160,	.140,
								.205,	.185,	.165 };
   	
		double V[2][3][5]= {	.695,	.675,	.665,	.650,	.640,
								.720,	.700,	.690,	.680,	.670,
								.740,	.725,	.720,	.710,	.700,
								.665,	.640,	.630,	.615,	.0,
								.690,	.670,	.665,	.645,	.635,
								.715,	.695,	.685,	.775,	.665 };
   	
		DES (T[B][C][A],	"SBAC.5ccaa");		// Cemento
		DES (U[B][C],		"SBAA.1a");			// Agua
		DES (V[B][C][A],	"SBRA.5ab");		// Arena
		DES (V[B][C][A]*2,	"SBRG.1%c", 'a'+C);	// Grava
		DES (1,				"MAMA19a");			// Hormigonera
		DES (2,				"MOOC13a");			// Peón ordinario
   	
		RES ("%s C/%s Tmax=%s mm", ROTA, ROTB, ROTC);
   	
		int G[5]= { 50, 100, 125, 150, 175 };
   	
		TEX (	"Hormigón %s, resistencia característica %d Kg/cm2, "
				"consistencia %s, cemento tipo II-Z/35-A, arena silícea "
				"(0/6) y grava silícea rodada, tamaño máximo %s mm, "
				"confeccionado en obra con hormigonera de 300 l de capacidad. "
				"Según RC-93 y EH-91.", ROTA, G[A], ROTB, ROTC );

		return TRUE;
	}

	return TRUE;
}


short SBRG_1 (Cfiebdc &par, short operacion) {
	
	INI (operacion);
	COD ("SBRG.1$");

	if (operacion == LEE) {
		PAR ("Tmax", "18", "38", "78", "");
		SIN ("a", "_18");
		SIN ("b", "_38");
		SIN ("c", "_78");
		return TRUE;
	}

	else if (operacion == CALCULA) {

		PRE (125.5+0.25*A);
		RES ("Grava de Tmáx. %s", ROTA);

		return TRUE;
	}

	return TRUE;
}

short FIN (Cfiebdc &par, short operacion) {
	return FALSE;
}

PRECIO precios[] = {ABPH_1, SBRG_1, FIN};
