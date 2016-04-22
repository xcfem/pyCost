#include <windows.h>
#include "Gest.h"

BOOL
AbreDll (
char		*nDll,
HINSTANCE	*hDll,
char		*Err )
{
	*hDll = LoadLibrary (nDll);
	if ( ! (*hDll) ) {
		Err = "Imposible abrir la librería de la Base";
		return FALSE;
	}
	if(	(pGloLee =			(BDCGLOLEE)			GetProcAddress (*hDll, "BdcGloLee")) &&
		(pGloParNumero =	(BDCGLOPARNUMERO)	GetProcAddress (*hDll, "BdcGloParNumero")) &&
		(pGloOpcNumero =	(BDCGLOOPCNUMERO)	GetProcAddress (*hDll, "BdcGloOpcNumero")) &&
		(pGloParRotulo =	(BDCGLOPARROTULO)	GetProcAddress (*hDll, "BdcGloParRotulo")) &&
		(pGloOpcRotulo =	(BDCGLOOPCROTULO)	GetProcAddress (*hDll, "BdcGloOpcRotulo")) &&
		(pGloCierra =		(BDCGLOCIERRA)		GetProcAddress (*hDll, "BdcGloCierra")) &&
		(pLee =				(BDCLEE)			GetProcAddress (*hDll, "BdcLee")) &&
		(pParNumero =		(BDCPARNUMERO)		GetProcAddress (*hDll, "BdcParNumero")) &&
		(pOpcNumero =		(BDCOPCNUMERO)		GetProcAddress (*hDll, "BdcOpcNumero")) &&
		(pParRotulo =		(BDCPARROTULO)		GetProcAddress (*hDll, "BdcParRotulo")) &&
		(pOpcRotulo =		(BDCOPCROTULO)		GetProcAddress (*hDll, "BdcOpcRotulo")) &&
		(pOpciones =		(BDCOPCIONES)		GetProcAddress (*hDll, "BdcOpciones")) &&
		(pCalcula =			(BDCCALCULA)		GetProcAddress (*hDll, "BdcCalcula")) &&
		(pCierra = 			(BDCCIERRA)			GetProcAddress (*hDll, "BdcCierra")) &&
		(pDesNumero =		(BDCDESNUMERO)		GetProcAddress (*hDll, "BdcDesNumero")) &&
		(pDesCodigo =		(BDCDESCODIGO)		GetProcAddress (*hDll, "BdcDesCodigo")) &&
		(pRendimiento =		(BDCRENDIMIENTO)	GetProcAddress (*hDll, "BdcRendimiento")) &&
		(pPrecio =			(BDCPRECIO)			GetProcAddress (*hDll, "BdcPrecio")) &&
		(pCodigo =			(BDCCODIGO)			GetProcAddress (*hDll, "BdcCodigo")) &&
		(pResumen =			(BDCRESUMEN)		GetProcAddress (*hDll, "BdcResumen")) &&
		(pTexto =			(BDCTEXTO)			GetProcAddress (*hDll, "BdcTexto")) &&
		(pPliego =			(BDCPLIEGO)			GetProcAddress (*hDll, "BdcPliego")) &&
		(pError =			(BDCERROR)			GetProcAddress (*hDll, "BdcError")) ) {

		Err = "";
		return TRUE;
	
	} else {
		Err = "Función inexistente en la librería";
		return FALSE;
	}
}

BOOL
CierraDll (
HMODULE	hDll,
char	*Err )
{
	if (hDll) {
		if ( !FreeLibrary (hDll) ) {
			Err = "Error al cerrar la librería";
			return FALSE;
		} else {
			Err = "";
			return TRUE;
		}
	} else {
		Err = "No hay librería que cerrar";
		return FALSE;
	}
}
