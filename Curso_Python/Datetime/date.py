from datetime import datetime, timedelta

# Obtener la fecha y hora actual
now = datetime.now()
print("Fecha y hora actual:", now)

# Formatear la fecha y hora
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora formateada:", formatted_date)

# Crear una fecha específica
specific_date = datetime(2023, 10, 1, 12, 30, 0)
print("Fecha específica:", specific_date)

# Calcular una nueva fecha sumando días
future_date = now + timedelta(days=10)
print("Fecha futura (10 días después):", future_date)

# Calcular la diferencia entre dos fechas
date1 = datetime(2023, 10, 1)
date2 = datetime(2023, 10, 15)
difference = date2 - date1
print("Diferencia entre fechas:", difference.days, "días")