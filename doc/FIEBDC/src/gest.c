#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include "Gest.h"

int main (void) {

	HANDLE		Precio=(HANDLE)0, PrecioGlobal=(HANDLE)0;
	HINSTANCE	hLib=(HINSTANCE)0;
	FILE		*fSalida;
	char		*err, codigo[20];
	char		*Precios [] = {"ABPH.1$", "SBRG.1$", "NoExiste"};
	int			nPrecios = 3;
	int			i,j,k;
	long		nParGlobales=0,ListaOpcGlobales[20];
	long		nPar,nOpc[20],ListaOpc[20],ListaOpc2[20];

	printf ("\nEJEMPLO DE PROGRAMA QUE ACCEDE A LA BASE \"BASE.DLL\"\n");
	printf ("LOS RESULTADOS SE ESCRIBEN EN EL ARCHIVO \"SALIDA.TXT\"\n");

	if ( !(fSalida = fopen ("SALIDA.TXT", "wt")) ) {
		printf ("\nERROR: Imposible crear el archivo de salida\n");
		return FALSE;
	}
	fprintf (fSalida,"\nEJEMPLO DE PROGRAMA QUE ACCEDE A LA BASE \"BASE.DLL\"\n");

	if (!AbreDll("BASE.DLL", &hLib, err)) {
		fprintf (fSalida,"\nERROR: %s\n", err);
		return FALSE;
	}

	// Lectura del Paramétrico Global
	if ( (PrecioGlobal = pGloLee ()) == (HANDLE) 0 ) {
		fprintf (fSalida,"\nATENCIÓN: No existe Paramétrico Global en la Base\n");
	} else {
		nParGlobales = pGloParNumero(PrecioGlobal);
		fprintf (fSalida,"\nPrecio Global: Número de parámetros: %ld\n", nParGlobales);
		for (j=0; j<nParGlobales; j++) {
			ListaOpcGlobales[j]=0;
			fprintf (fSalida,"\nParámetro %d: Rótulo: %s\n", j, pGloParRotulo(PrecioGlobal,j));
			for (k=0; k<pGloOpcNumero(PrecioGlobal,j); k++) {
				fprintf (fSalida,"\tOpción %d: Rótulo: %s\n", k, pGloOpcRotulo(PrecioGlobal,j,k));
			}
		}

		pGloCierra (PrecioGlobal);
	}
	
	// Lectura de los precios
	for (i=0; i<nPrecios; i++) {
		if ( (Precio = pLee (Precios[i])) == (HANDLE) 0 ) {
			fprintf (fSalida,"\nERROR: El precio \"%s\" no existe\n", Precios[i]);
			continue;
		}

		// Rótulos de Parámetros y Opciones
		nPar = pParNumero(Precio);
		fprintf (fSalida,"\nPrecio \"%s\": Número de parámetros: %ld\n", Precios[i], nPar);
		for (j=0; j<nPar; j++) {
			fprintf (fSalida,"\nParámetro %d: Rótulo: %s\n", j, pParRotulo(Precio,j));
			nOpc[j]=pOpcNumero(Precio,j);
			ListaOpc[j]=0;
			for (k=0; k<nOpc[j]; k++) {
				fprintf (fSalida,"\tOpción %d: Rótulo: %s\n", k, pOpcRotulo(Precio,j,k));
			}
		}

		//Listado de todas las combinaciones paramétricas
		do {
			if (!pCalcula (Precio, ListaOpc, nParGlobales, ListaOpcGlobales)) {
				fprintf (fSalida,"\nCODIGO : %s\n", pCodigo(Precio));
				fprintf (fSalida,"ERROR: %s\n", pError(Precio));
				goto siguiente;
			}
			strcpy (codigo, pCodigo(Precio));
			pOpciones (Precio, codigo+6, ListaOpc2);
			fprintf (fSalida,"\nCODIGO: %s\n", codigo);
			fprintf (fSalida,"OPCIONES: ");
			for (j=0; j<nPar; j++)
				fprintf (fSalida,"%d ",ListaOpc2[j]);

			fprintf (fSalida,"\nRESUMEN:%s\n", pResumen(Precio));
			fprintf (fSalida,"TEXTO:%s\n", pTexto(Precio));
			fprintf (fSalida,"PLIEGO:%s\n", pPliego(Precio));

			if (pDesNumero(Precio)) {
				fprintf (fSalida,"DESCOMPOSICIÓN:\n");
				for (j=0; j<pDesNumero(Precio); j++) {
					fprintf (fSalida,"\t%2d %s \t%.3lf\n", j+1, pDesCodigo(Precio,j), pRendimiento(Precio,j));
				}
			} else {
				fprintf (fSalida,"PRECIO:%.2lf\n", pPrecio(Precio));
			}

siguiente:			
			for (j=nPar-1; j>=0; j--) {
				if (ListaOpc[j]<nOpc[j]-1) {
					ListaOpc[j]++;
					break;
				} else {
					ListaOpc[j]=0;
				}
			}
			if (j<0) break;
		} while (TRUE);

		pCierra (Precio);
	}

	fcloseall();
	printf ("\nPROGRAMA FINALIZADO\nPulse una tecla\n");
	getch();

	if (!CierraDll ((HMODULE)hLib, err) ) {
		fprintf (fSalida,"\nERROR: %s\n", err);
		return FALSE;
	}

	return TRUE;
}
