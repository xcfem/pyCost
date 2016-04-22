#include "Fiebdc.h"

BDCGLOLEE		pGloLee;
BDCGLOPARNUMERO	pGloParNumero;
BDCGLOOPCNUMERO	pGloOpcNumero;
BDCGLOPARROTULO	pGloParRotulo;
BDCGLOOPCROTULO	pGloOpcRotulo;
BDCGLOCIERRA	pGloCierra;

BDCLEE			pLee;
BDCPARNUMERO	pParNumero;
BDCOPCNUMERO	pOpcNumero;
BDCPARROTULO	pParRotulo;
BDCOPCROTULO	pOpcRotulo;
BDCOPCIONES		pOpciones;
BDCCALCULA		pCalcula;
BDCCIERRA		pCierra;
BDCDESNUMERO	pDesNumero;
BDCDESCODIGO	pDesCodigo;
BDCRENDIMIENTO	pRendimiento;
BDCPRECIO		pPrecio;
BDCCODIGO		pCodigo;
BDCRESUMEN		pResumen;
BDCTEXTO		pTexto;
BDCPLIEGO		pPliego;
BDCERROR		pError;

BOOL AbreDll (char *nDll, HINSTANCE *hDll, char	*Err);
BOOL CierraDll (HMODULE hDll, char *Err);
