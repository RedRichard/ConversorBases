import conversiones # CONTIENE LAS FUNCIONES PARA CAMBIAR DE BASE A UN NUMERO

# ===============================
# OBTENIENDO LOS DATOS DE ENTRADA
# ===============================

numero = input( "Numero: " ) # OBTENGO EL NUMERO QUE VOY A CONVERTIR
baseNumero = int( input( "Base inicial: " ) ) # OBTENGO LA BASE EN LA QUE SE ENCUENTRA EL NUMERO
baseNueva = int( input( "Base final: " ) ) # OBTENGO LA BASE A LA QUE QUIERO TRANSFORMAR

# ======================
# CONVIRTIENDO EL NUMERO
# ======================

resultado = conversiones.base_r_a_base_10( numero, baseNumero ) # INICIALMENTE TRANSFORMO AL NUMERO EN BASE 10
resultado = conversiones.base_10_a_base_r( resultado, baseNueva) # POSTERIORMENTE TRANSFORMO EL NUMERO AL A BASE DESEADA

# ========================
# MOSTRANDO LOS RESULTADOS
# ========================

print ( str(numero) + " en base " + str(baseNumero) + " es equivalente a " + resultado + " en base " + str(baseNueva) )