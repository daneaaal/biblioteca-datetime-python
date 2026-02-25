from datetime import datetime, timedelta

# Fecha y hora actual
ahora = datetime.now()

# Formatear fecha
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")

# Fecha futura
fin_ano = datetime(ahora.year, 12, 31)

# Diferencia
dias_restantes = (fin_ano - ahora).days

print("Fecha actual:", fecha_formateada)
print("Faltan", dias_restantes, "días para finalizar el año.")

# Ejemplo con timedelta
manana = ahora + timedelta(days=1)
print("Mañana será:", manana.strftime("%d/%m/%Y"))
