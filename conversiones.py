import math # PARA OBTENER EL COCIENTE ENTERO DE LA DIVISION

# =========
# VARIABLES
# =========

numeros = "0123456789ABCDEF" # DIGITOS A LOS QUE PUEDO CONVERTIR MI NUMERO

# =======================================================
# FUNCION PARA CONVERTIR UN NUMERO EN BASE 10 A OTRA BASE
# =======================================================

def base_10_a_base_r( numero, base ):	
	if ( numero < base ): # CASO BASE, SI EL COCIENTE ES MENOR A LA BASE, ENTONCES:
		return numeros[numero] # REGRESAMOS EL COCIENTE CONVERTIDO

	cociente = math.floor( numero/base ) # OBTENEMOS EL COCIENTE
	residuo = numero % base # OBTENEMOS EL RESIDUO

	return base_10_a_base_r( cociente, base ) + numeros[residuo] # ANEXAMOS EL DIGITO OBTENIDOA AL INICIO DE LA CADENA

# =======================================================
# FUNCION PARA CONVERTIR UN NUMERO EN OTRA BASE A BASE 10
# =======================================================

def base_r_a_base_10( numero, base ):
	return int( numero, base )