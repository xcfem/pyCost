#include <windows.h>
#include <stdio.h>
#include <stdarg.h>
#include <string.h>

#include "Base.h"


Cfiebdc::Cfiebdc (void) {
	estado (ST_VACIO);
}

Cfiebdc::~Cfiebdc (void) {
	estado (ST_VACIO);
}

Cfiebdc::inicializa (
short	operacion )
{
	int i,j;

	if (operacion == BORRA) {
		estado (ST_VACIO);
		
		// parámetros y opciones por parámetro
		for (i=0; i<parnum; i++) {
			if (parrot[i]) {
				delete[] parrot[i];
				parrot[i] = (char *)0;
			}
			for (j=0; j< opcnum[i]; j++) {
				if (opcrot[i][j]) {
					delete[] opcrot[i][j];
					opcrot[i][j]= (char *)0;
				}
			}
			if (opcrot[i]) {
				delete[] opcrot[i];
				opcrot[i]= (char **)0;
			}
		}

		parnum=0;
		pre=0.;

		//parámetros globales
		if (opcg) {
			delete [] opcg;
			opcg = (long *)0;
		}
		opcgnum = 0;

		// sinónimos
		for (j=0; j<2; j++) {
			for (i=0; i<sinnum; i++) {
				if (codsin[j][i]) {
					delete[] codsin[j][i];
					codsin[j][i]= (char *)0;
				}
			}
			if (codsin[j]) {
				delete[] codsin[j];
				codsin[j]= (char **)0;
			}
		}
		sinnum=0;

		// descomposición
		if (desren) {
			delete[] desren;
			desren = (double *)0;
		}
		for (i=0; i<desnum; i++) {
			if (descod[i]) {
				delete[] descod[i];
				descod[i] = (char *)0;
			}
		}
		if (descod) {
			delete[] descod;
			descod = (char **)0;
		}
		desnum=0;
	
		// textos
		if (err)	{ delete[] err;		err		= (char *)0; }
		if (res)	{ delete[] res;		res		= (char *)0; }
		if (tex)	{ delete[] tex;		tex		= (char *)0; }
		if (pli)	{ delete[] pli;		pli		= (char *)0; }
		if (codfam)	{ delete[] codfam;	codfam	= (char *)0; }
		if (subcod)	{ delete[] subcod;	subcod	= (char *)0; }
		if (codder)	{ delete[] codder;	codder	= (char *)0; }
	}

	else if (operacion == LEE) {
		estado (ST_FAMILIA);
/*
		parnum=0;
		pre=0.;
		desnum=0;
		sinnum=0;

		for (i=0; i<MAX_PARAM; i++) {
			opcnum[i] = opc[i] = 0;
			parrot[i] = (char *)0;
			opcrot[i] = (char **)0;
		}
		err = res = tex = pli = codfam = subcod = codder = (char *)0;
		descod = (char **)0;
		desren = (double *)0;
		codsin[0] = codsin[1] = (char **)0;
*/
	}

	else if (operacion==CALCULA) {
		estado (ST_DERIVADO);

		pre=0.;

		// descomposición
		if (desren) {
			delete[] desren;
			desren = (double *)0;
		}
		for (i=0; i<desnum; i++) {
			if (descod[i]) {
				delete[] descod[i];
				descod[i] = (char *)0;
			}
		}
		if (descod) {
			delete[] descod;
			descod = (char **)0;
		}
		desnum=0;
	
		if (err)	{ delete[] err;		err		= (char *)0; }
		if (res)	{ delete[] res;		res		= (char *)0; }
		if (tex)	{ delete[] tex;		tex		= (char *)0; }
		if (pli)	{ delete[] pli;		pli		= (char *)0; }
		if (codfam)	{ delete[] codfam;	codfam	= (char *)0; }
		if (subcod)	{ delete[] subcod;	subcod	= (char *)0; }
		if (codder)	{ delete[] codder;	codder	= (char *)0; }
	}
	return TRUE;
}

BOOL
Cfiebdc::parametro (
char	*rot, ... )
{
	int		i, len;
	long	Opcnum=0;
	char	*s;
	va_list	marker;

	if (parnum>=MAX_PARAM) return FALSE;

	len = strlen(rot);
	parrot[parnum] = new char[len+1];
	strcpy (parrot[parnum], rot);

	va_start( marker, rot );
	do {
		s = va_arg( marker, char *);
		len = strlen (s);
		if (len==0) break;
		Opcnum++;
	} while ( s[0] != '\0' );

	va_start( marker, rot );
	opcrot[parnum] = new char* [Opcnum];
	for (i=0; i<Opcnum; i++) {
		s = va_arg( marker, char *);
		len = strlen (s);
		opcrot[parnum][i] = new char[len+1];
		strcpy (opcrot[parnum][i], s);
	}

	va_end( marker );

	opcnum[parnum]=Opcnum;
	parnum++;

	return TRUE;
}

BOOL
Cfiebdc::precio (
double	Pre )
{
	pre=Pre;
	return TRUE;
}

BOOL
Cfiebdc::descompuesto (
double	Ren,
char	*Cod,... )
{
	int		i, len;
	char	s[255], **Descod;
	va_list	marker;
	double	*Desren;

	Desren = new double [desnum+1];
	memcpy (Desren, desren, desnum*sizeof(double));
	delete[] desren;
	desren = Desren;
	desren [desnum] = Ren;

	Descod = new char *[desnum+1];
	for (i=0; i<desnum; i++)
		Descod[i] = descod[i];
	delete[] descod;
	descod = Descod;
	
	va_start( marker, Cod );

	vsprintf (s,Cod,marker);

	len = strlen (s);
	descod[desnum] = new char[len+1];
	strcpy (descod[desnum], s);

	va_end( marker );
	desnum++;
	return TRUE;
}

BOOL
Cfiebdc::resumen (
char	*Res, ... )
{
	char	*s = new char [MAX_TXT];
	int		len;
	va_list	marker;

	va_start( marker, Res );

	vsprintf (s,Res,marker);

	len = strlen (s);
	res = new char[len+1];
	strcpy (res, s);
	delete[] (s);

	va_end( marker );

	return TRUE;
}

BOOL
Cfiebdc::texto (
char	*Tex, ...)
{
	char	*s = new char [MAX_TXT];
	int		len;
	va_list	marker;

	va_start( marker, Tex );

	vsprintf (s,Tex,marker);

	len = strlen (s);
	tex = new char[len+1];
	strcpy (tex, s);
	delete[] (s);

	va_end( marker );

	return TRUE;
}

BOOL
Cfiebdc::pliego (
char	*Pli, ...)
{
	char	*s = new char [MAX_TXT];
	int		len;
	va_list	marker;

	va_start( marker, Pli );

	vsprintf (s,Pli,marker);

	len = strlen (s);
	pli = new char[len+1];
	strcpy (pli, s);
	delete[] (s);

	va_end( marker );

	return TRUE;
}

BOOL
Cfiebdc::error (
char	*Err, ...)
{
	char	*s = new char [MAX_TXT];
	int		len;
	va_list	marker;

	va_start( marker, Err );

	vsprintf (s,Err,marker);

	len = strlen (s);
	err = new char[len+1];
	strcpy (err, s);
	delete[] (s);

	va_end( marker );

	estado (ST_ERROR);
	return FALSE;
}

long
Cfiebdc::lee_opcion (
long	Par)
{
	if (Par>=parnum) return -1;
	return opc[Par];
}

char
*Cfiebdc::lee_rotulo (
long	Par)
{
	if (Par>=parnum || opc[Par]>=opcnum[Par]) return NULL;
	return opcrot[Par][opc[Par]];
}

BOOL
Cfiebdc::codigo (
char	*Cod, ...)
{
	char	*s = new char [MAX_TXT];
	int		i,len;
	va_list	marker;

	va_start( marker, Cod );

	vsprintf (s,Cod,marker);

	len = strlen (s);
	for (i=0; i<len; i++)
		if (s[i] == '$') break;

	if (codfam) delete[] codfam;
	if (i<len) {
		codfam = new char[len+1];
		strcpy (codfam, s);
	} else {
		codfam = new char[len+2];
		sprintf (codfam, "%s%c", s, '$');
	}
	delete[] s;

	va_end( marker );

	if (status==ST_DERIVADO)
		return subcodigo();
	return TRUE;
}

BOOL
Cfiebdc::opciones (
long	*Opc )
{
	int		i;
	BOOL	ret=TRUE;

	for (i=0; i<parnum; i++) {
		if (Opc[i]<0 || Opc[i]>=opcnum[i]) {
			opc[i] = 0;
			ret=FALSE;
		} else {
			opc[i] = Opc[i];
		}
	}
	return ret;
}

BOOL
Cfiebdc::opciones_glo (
long	OpcGNum,
long	*OpcG )
{
	opcgnum = OpcGNum;
	if (opcg) delete[] opcg;
	if (OpcGNum) {
		opcg = new long [OpcGNum];
		memcpy (opcg, OpcG, OpcGNum * sizeof (long));
	}
	return TRUE;
}

BOOL
Cfiebdc::sinonimo (
char	*Subcod,
char	*Codsin )
{
	char	**Sin[2];
	int		i,j,len1,len2;

	len1 = strlen (Subcod);
	len2 = strlen (Codsin);

	if (!len1 || !len2) return FALSE;

	for (i=0; i<2; i++) {
		Sin[i] = new char *[sinnum+1];
		for (j=0; j<sinnum; j++) {
			Sin[i][j] = codsin[i][j];
		}
		if (codsin[i]) delete[] codsin[i];
	}
	Sin[0][sinnum] = new char [len1+1];
	Sin[1][sinnum] = new char [len2+1];
	strcpy (Sin[0][sinnum], Subcod);
	strcpy (Sin[1][sinnum], Codsin);

	codsin[0]=Sin[0];
	codsin[1]=Sin[1];

	sinnum++;

	return TRUE;
}

char
*Cfiebdc::lee_rot_par (
long	id_par)
{
	if (id_par >= parnum || !parrot[id_par])
		return "";
	else
		return parrot[id_par];
}

char
*Cfiebdc::lee_rot_opc
(long	id_par,
long	id_opc) {
	if (id_par >= parnum || id_opc >= opcnum[id_par] || !opcrot[id_par] || !opcrot[id_par][id_opc])
		return "";
	else
		return opcrot[id_par][id_opc];
}

char
*Cfiebdc::lee_cod_des (
long	id_des )
{
	if (id_des >= desnum || !descod[id_des])
		return "";
	else
		return descod[id_des];
}

double
Cfiebdc::lee_ren_des (
long	id_des )
{
	if (id_des >= desnum)
		return .0;
	else
		return desren[id_des];
}

char
*Cfiebdc::lee_codigo (void) {
	if (codder)
		return codder;
	else if (codfam)
		return codfam;
	else
		return "";
}

char
*Cfiebdc::lee_resumen (void) {
	if (res)	return res;
	else		return "";
}
char
*Cfiebdc::lee_texto (void) {
	if (tex)	return tex;
	else		return "";
}
char
*Cfiebdc::lee_pliego (void) {
	if (pli)	return pli;
	else		return "";
}

char
*Cfiebdc::lee_error (void) {
	if (err)	return err;
	else		return "";
}

BOOL
Cfiebdc::subcodigo (void) {
	int		i, az='z'-'a', AZ='Z'-'A';
	BOOL	ret=TRUE;
	char	*s = new char [MAX_TXT];
	
	// Obtención del subcódigo automático
	subcod = new char [parnum+1];
	for (i=0; i<parnum; i++) {
		if (opc[i]>=0 && opc[i]<=0+az)
			subcod[i]=opc[i]+'a';
		else if (opc[i]>0+az && opc[i]<=0+az+AZ)
			subcod[i]=opc[i]-az+'A';
		else if (opc[i]>0+az+AZ && opc[i]<=9+az+AZ)
			subcod[i]=opc[i]-az-AZ;
		else {
			subcod[i]='_';
			ret = FALSE;
		}
	}
	subcod[i]='\0';
	
	// Comprobar lista de sinónimos
	for (i=0; i<sinnum; i++) {
		if (strcmp(subcod,codsin[0][i]) == 0) {
			delete [] subcod;
			subcod = new char [strlen (codsin[1][i])+1];
			strcpy (subcod, codsin[1][i]);
		}
	}
	
	// Rellenar codfam y codder
	strcpy (s, codfam);
	for (i=0; i<(int)strlen(codfam); i++)
		if (codfam[i]=='$') break;
	strcpy (s+i, subcod);

	codder = new char [strlen(s)+1];
	strcpy (codder, s);

	return ret;
}

BOOL
Cfiebdc::lee_opciones (
char	*Cod,	// parte variable del código
long	*Opc )	// opciones a devolver
{
	int		i, len, az='z'-'a', AZ='Z'-'A';
	char	*s;
	BOOL	ret=TRUE;

	for (i=0; i<sinnum; i++) {
		if (strcmp(Cod, codsin[1][i])==0) {
			len = strlen (codsin[0][i]);
			s = codsin[0][i];
			break;
		}
	}
	if (i==sinnum) {
		s = Cod;
		len = strlen (s);
	}

	for (i=0; i<len; i++) {
		if (s[i] >= 'a' && s[i] <= 'z')
			Opc[i] = s[i]-'a';
		else if (s[i] >= 'A' && s[i] <= 'Z')
			Opc[i] = s[i]-'A' + az;
		else if (s[i] >= '0' && s[i] <= '9')
			Opc[i] = s[i]-'0' + az + AZ;
		else {
			// excedida capacidad
			Opc[i] = az + AZ + 11;
			ret = FALSE;
		}
	}
	return ret;
}
