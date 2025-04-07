import calendar

# Crear un calendario de texto para un mes específico
year = 2023
month = 10
print(calendar.month(year, month))

# Crear un calendario completo para un año
print(calendar.calendar(year))

# Verificar si un año es bisiesto
is_leap = calendar.isleap(year)
print(f"¿El año {year} es bisiesto? {'Sí' if is_leap else 'No'}")

# Obtener el número de días en un mes
_, days_in_month = calendar.monthrange(year, month)
print(f"El mes {month} del año {year} tiene {days_in_month} días.")

# Iterar sobre los días de un mes
print("Días del mes:")
for week in calendar.monthcalendar(year, month):
    print(week)