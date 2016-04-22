/*	FORMATO DE INTERCAMBIO ESTÁNDAR DE PARAMÉTRICOS EN DLL	*/

#ifdef BASE

/****************************************************************************/
/*	PARTE DEL ARCHIVO NECESARIA PARA LOS DESARROLLADORES DE BASE DE PRECIOS	*/
/****************************************************************************/

/*	FUNCIONES REFERENTES AL PARAMÉTRICO GLOBAL	*****************************/
/*	Accesibles en cualquier momento	*/
/*	Lectura del paramétrico global */
HANDLE	APIENTRY BdcGloLee			(VOID);

/*	Accesibles después de BdcGloLee	*/
/*	Obtención de sus parámetros */
LONG	APIENTRY BdcGloParNumero 	(HANDLE h);
LONG	APIENTRY BdcGloOpcNumero 	(HANDLE h, LONG par);
LPCSTR	APIENTRY BdcGloParRotulo 	(HANDLE h, LONG par);
LPCSTR	APIENTRY BdcGloOpcRotulo 	(HANDLE h, LONG par, LONG opc);
/*	Cerrar y liberar memoria */
BOOL	APIENTRY BdcGloCierra		(HANDLE h);

/*	FUNCIONES REFERENTES AL RESTO DE PARAMÉTRICOS	*************************/
/*	Accesibles en cualquier momento	*/
/*	Lectura de una familia */
HANDLE	APIENTRY BdcLee				(LPCSTR cod);

/*	Accesibles después de BdcLee	*/
/*	Obtención de sus parámetros */
LONG	APIENTRY BdcParNumero 		(HANDLE h);
LONG	APIENTRY BdcOpcNumero 		(HANDLE h, LONG par);
LPCSTR	APIENTRY BdcParRotulo 		(HANDLE h, LONG par);
LPCSTR	APIENTRY BdcOpcRotulo 		(HANDLE h, LONG par, LONG opc);
/*	Obtención de las opciones en función del código */
BOOL	APIENTRY BdcOpciones		(HANDLE h, LPCSTR sub, LPLONG opcl);
/*	Asignación de opciones de los parámetros y cálculo del derivado */
BOOL	APIENTRY BdcCalcula			(HANDLE h, LPLONG opcl, LONG gloparnum, LPLONG gloopcl);
/*	Liberación de memoria */
BOOL	APIENTRY BdcCierra			(HANDLE h);

/*	Accesibles después de BdcCalcula	*/
/*	Obtención del derivado paramétrico */
LONG	APIENTRY BdcDesNumero		(HANDLE h);
LPCSTR	APIENTRY BdcDesCodigo		(HANDLE h, LONG des);
double	APIENTRY BdcRendimiento		(HANDLE h, LONG des);
double	APIENTRY BdcPrecio			(HANDLE h);
LPCSTR	APIENTRY BdcCodigo			(HANDLE h);
LPCSTR	APIENTRY BdcResumen			(HANDLE h);
LPCSTR	APIENTRY BdcTexto			(HANDLE h);
LPCSTR	APIENTRY BdcPliego			(HANDLE h);
/*	Mensajes de error */
LPCSTR	APIENTRY BdcError			(HANDLE h);


#else  /* BASE no definido */
/****************************************************************************/
/*	PARTE DEL ARCHIVO NECESARIA PARA LOS DESARROLLADORES DE PROGRAMAS		*/
/****************************************************************************/

/*	FUNCIONES REFERENTES AL PARAMÉTRICO GLOBAL	*****************************/
typedef HANDLE	(APIENTRY * BDCGLOLEE)		(VOID);
typedef LONG	(APIENTRY * BDCGLOPARNUMERO)(HANDLE h);
typedef LONG	(APIENTRY * BDCGLOOPCNUMERO)(HANDLE h, LONG par);
typedef LPCSTR	(APIENTRY * BDCGLOPARROTULO)(HANDLE h, LONG par);
typedef LPCSTR	(APIENTRY * BDCGLOOPCROTULO)(HANDLE h, LONG par, LONG opc);
typedef BOOL	(APIENTRY * BDCGLOCIERRA)	(HANDLE h);

/*	FUNCIONES REFERENTES AL RESTO DE PARAMÉTRICOS	*************************/
typedef HANDLE	(APIENTRY * BDCLEE)			(LPCSTR cod);
typedef LONG	(APIENTRY * BDCPARNUMERO)	(HANDLE h);
typedef LONG	(APIENTRY * BDCOPCNUMERO)	(HANDLE h, LONG par);
typedef LPCSTR	(APIENTRY * BDCPARROTULO)	(HANDLE h, LONG par);
typedef LPCSTR	(APIENTRY * BDCOPCROTULO)	(HANDLE h, LONG par, LONG opc);
typedef BOOL	(APIENTRY * BDCOPCIONES)	(HANDLE h, LPCSTR sub, LPLONG opcl);
typedef BOOL	(APIENTRY * BDCCALCULA)		(HANDLE h, LPLONG opcl, LONG gloparnum, LPLONG gloopcl);
typedef BOOL	(APIENTRY * BDCCIERRA)		(HANDLE h);
typedef LONG	(APIENTRY * BDCDESNUMERO)	(HANDLE h);
typedef LPCSTR	(APIENTRY * BDCDESCODIGO)	(HANDLE h, LONG des);
typedef double	(APIENTRY * BDCRENDIMIENTO)	(HANDLE h, LONG des);
typedef double	(APIENTRY * BDCPRECIO)		(HANDLE h);
typedef LPCSTR	(APIENTRY * BDCCODIGO)		(HANDLE h);
typedef LPCSTR	(APIENTRY * BDCRESUMEN)		(HANDLE h);
typedef LPCSTR	(APIENTRY * BDCTEXTO)		(HANDLE h);
typedef LPCSTR	(APIENTRY * BDCPLIEGO)		(HANDLE h);
typedef LPCSTR	(APIENTRY * BDCERROR)		(HANDLE h);

#endif /* de ifdef #BASE */
