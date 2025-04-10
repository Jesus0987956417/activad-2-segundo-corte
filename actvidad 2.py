import os
import re

# Ruta base
carpeta_principal = "C:\\Users\\USER\\Downloads"

# Expresiones regulares para IPs, fechas y códigos de error comunes
regex_ip = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
regex_fecha = re.compile(r"\b(?:[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\b")  # ejemplo: Apr 10 12:34:56
regex_error = re.compile(r"\b(?:4\d{2}|5\d{2})\b")  # códigos como 404, 500, etc.

# Conjuntos para almacenar datos únicos
ips_unicas = set()
fechas = set()
codigos_error = set()

# Leer todos los archivos
for carpeta_raiz, _, archivos in os.walk(carpeta_principal):
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_raiz, archivo)

        try:
            with open(ruta_completa, "r", encoding="utf-8", errors="ignore") as f:
                for linea in f:
                    ips_unicas.update(regex_ip.findall(linea))
                    fechas.update(regex_fecha.findall(linea))
                    codigos_error.update(regex_error.findall(linea))
        except Exception as e:
            print(f"Error leyendo {ruta_completa}: {e}")

# Mostrar resultados
print("\n IPs únicas encontradas:")
for ip in sorted(ips_unicas):
    print(ip)

print("\n Fechas encontradas:")
for fecha in sorted(fechas):
    print(fecha)

print("\nCódigos de error encontrados:")
for codigo in sorted(codigos_error):
    print(codigo)

