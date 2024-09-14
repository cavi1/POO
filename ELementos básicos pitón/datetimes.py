from datetime import datetime

fecha_hora_actual = datetime.now()
print(fecha_hora_actual)  # Ejemplo de salida: 2024-09-14 12:30:45.123456


from datetime import datetime

fecha_hora_actual = datetime.now()
formato = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")  # Día/Mes/Año Hora:Minuto:Segundo
print(formato)  # Ejemplo de salida: 14/09/2024 12:30:45


from datetime import datetime

fecha_especifica = datetime(2024, 9, 14, 12, 30, 45)
print(fecha_especifica)  # Salida: 2024-09-14 12:30:45


from datetime import datetime, timedelta

fecha_hora_actual = datetime.now()
# Restar 7 días
hace_una_semana = fecha_hora_actual - timedelta(days=7)
print(hace_una_semana)

# Sumar 2 horas
en_dos_horas = fecha_hora_actual + timedelta(hours=2)
print(en_dos_horas)


from datetime import datetime

fecha_hora_actual = datetime.now()

solo_fecha = fecha_hora_actual.date()  # Obtiene solo la fecha
solo_hora = fecha_hora_actual.time()   # Obtiene solo la hora

print(solo_fecha)  # Ejemplo: 2024-09-14
print(solo_hora)   # Ejemplo: 12:30:45.123456


from datetime import datetime

cadena_fecha = "14/09/2024 12:30:45"
fecha_convertida = datetime.strptime(cadena_fecha, "%d/%m/%Y %H:%M:%S")
print(fecha_convertida)  # Salida: 2024-09-14 12:30:45


from datetime import datetime

fecha1 = datetime(2024, 9, 14)
fecha2 = datetime(2024, 10, 14)

diferencia = fecha2 - fecha1
print(diferencia.days)  # Salida: 30 (días de diferencia)


from datetime import datetime

fecha_hora_actual = datetime.now()
dia_semana = fecha_hora_actual.strftime("%A")  # Obtiene el nombre del día de la semana en inglés
print(dia_semana)  # Ejemplo de salida: Saturday


anio = fecha_hora_actual.year   # Año
mes = fecha_hora_actual.month   # Mes
dia = fecha_hora_actual.day     # Día
hora = fecha_hora_actual.hour   # Hora
minuto = fecha_hora_actual.minute  # Minutos
segundo = fecha_hora_actual.second  # Segundos
