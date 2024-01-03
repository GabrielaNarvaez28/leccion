import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
empleados = requests.get(url).json()
print(empleados)

#obtener numero de empleados
if 'data' in empleados:
    lista_empleados = empleados['data']
# Obtener la cantidad de empleados
    cantidad_empleados = len(lista_empleados)
    print(f'Cantidad de empleados: {cantidad_empleados}')
else:
    print('Error al obtener la lista de empleados')


# promedio de salario de los empleados
if 'data' in empleados:
    lista_empleados = empleados['data']

    # Obtener salarios y calcular el promedio
    salarios = [empleado['employee_salary'] for empleado in lista_empleados]

    if salarios:
        promedio_salarios = sum(salarios) / len(salarios)
        print(f'El promedio de salarios es: {promedio_salarios:.2f}')
    else:
        print('No hay información de salarios disponible.')
else:
    print('Error al obtener la lista de empleados')


# promedio de edad de los empleados
if 'data' in empleados:
    lista_empleados = empleados['data']

    # Obtener edades y calcular el promedio
    edades = [empleado['employee_age'] for empleado in lista_empleados]

    if edades:
        promedio_edades = sum(edades) / len(edades)
        print(f'El promedio de edades es: {promedio_edades:.2f}')
    else:
        print('No hay información de edades disponible.')
else:
    print('Error al obtener la lista de empleados')


# nos enseña el salario mínimo y máx
if 'data' in empleados:
    lista_empleados = empleados['data']

    # Obtener salarios
    salarios = [empleado['employee_salary'] for empleado in lista_empleados]

    if salarios:
        salario_minimo = min(salarios)
        salario_maximo = max(salarios)

        print(f'Salario mínimo: {salario_minimo}')
        print(f'Salario máximo: {salario_maximo}')
    else:
        print('No hay información de salarios disponible.')
else:
    print('Error al obtener la lista de empleados')



# nos indica las edades mínimo y máx de los empleados
if 'data' in empleados:
    lista_empleados = empleados['data']

    # Obtener edades
    edades = [empleado['employee_age'] for empleado in lista_empleados]

    if edades:
        edad_minima = min(edades)
        edad_maxima = max(edades)

        print(f'Edad mínima: {edad_minima}')
        print(f'Edad máxima: {edad_maxima}')
    else:
        print('No hay información de edades disponible.')
else:
    print('Error al obtener la lista de empleados')
