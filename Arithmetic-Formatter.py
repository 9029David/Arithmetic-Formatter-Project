def crear_lista(problems):
    lista = {
        'operando_uno': [],
        'signo': [],
        'operando_dos': [],
        'resultado': []
    }
    for operacion in problems:
        operacion = operacion.split()

        lista['operando_uno'] += operacion[::3] 
        lista['signo'] += operacion[1::3]
        lista['operando_dos'] += operacion[2::3]
        lista['resultado'] += operacion_sublista(operacion[::3],    operacion[2::3], operacion[1::3])
    return lista


def operacion_sublista(sublista_uno, sublista_dos, signos):
    operacion = []
    
    for num1, num2, signo in zip(sublista_uno, sublista_dos, signos):
        if num1.isdigit() and num2.isdigit():
            if len(num1) <= 4 or len(num2) <= 4:
                if signo == '+':
                    operacion.append(int(num1) + int(num2))
                else:
                    operacion.append(int(num1) - int(num2))  
    return operacion


def espacio_operando(operando_uno_var, operando_dos_var, signo, resultado_var):
    max_len = max(len(operando_uno_var), len(operando_dos_var)) + 2
    espacio = " "

    if len(operando_uno_var) > len(operando_dos_var):
        numerador = espacio * 2 + operando_uno_var  
        denominador = signo + espacio * (max_len - len(operando_dos_var) - 1) + operando_dos_var
    else:
        numerador = espacio * (max_len - len(operando_uno_var)) + operando_uno_var
        denominador = signo + espacio + operando_dos_var

    linea = max_len * "-"
    resultado = espacio * (max_len - len(resultado_var)) + resultado_var

    return numerador, denominador, linea, resultado 



def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    lista = crear_lista(problems)
    
    operando_uno = lista['operando_uno']
    signos = lista['signo']
    operando_dos = lista['operando_dos']
    resultado = lista['resultado']

    numerador_lista = []
    denominador_lista = []
    linea_lista = []
    resultado_lista = []

    for indice in range(len(operando_uno)):
        operando_uno_var = operando_uno[indice]
        signo = signos[indice]
        operando_dos_var = operando_dos[indice]
        resultado_var = resultado[indice]
        
        if not operando_uno_var.isdigit() or not operando_dos_var.isdigit():
            return 'Error: Numbers must only contain digits.'
        if signo not in ['+', '-']:
            return "Error: Operator must be '+' or '-'." 
        if len(operando_uno_var) > 4 or len(operando_dos_var) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        cuenta = espacio_operando(operando_uno_var, operando_dos_var, signo, str(resultado_var))
        numerador_lista.append(cuenta[0])
        denominador_lista.append(cuenta[1])
        linea_lista.append(cuenta[2])
        resultado_lista.append(cuenta[3])
    
    numerador_str = "    ".join(numerador_lista)
    denominador_str = "    ".join(denominador_lista)
    linea_str = "    ".join(linea_lista)
    resultado_str = "    ".join(resultado_lista)

    if show_answers:
        resultado = f"{numerador_str}\n{denominador_str}\n{linea_str}\n{resultado_str}"
    else:
        resultado = f"{numerador_str}\n{denominador_str}\n{linea_str}"

    return resultado
    
print(f'{arithmetic_arranger(["323 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "2 + 2000"], True)}')

    














