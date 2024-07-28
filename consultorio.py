def dataLists():
    listNames = []
    listID = []
    listAge = []
    listaGenre = []
    listDiagnostics = []
    listCancelledAmount = []
    return listNames, listID, listAge, listaGenre, listDiagnostics, listCancelledAmount
#############################################################################################################################################################################################################################################################################################################################################################################################
def selectOptions(arreglo):
    if len(arreglo) == 0: dataOpc = intValidation(" - Menu de Opciones -\n:::>>> (1) Registrar Paciente\n:::>>> (2) Salir de Programa\n:::>>> Base de datos Vacia registre al primer paciente para habilitar demas opciones\n\n:::>>> Ingrese Opcion: ", False, True, False, 0, 3, 0, 0)
    else: dataOpc = intValidation(" - Menu de Opciones -\n:::>>> (1) Registrar Paciente\n:::>>> (2) Buscar por cedula e imprimir Diagnostico\n:::>>> (3) Imprimir datos de todos los pacientes \n:::>>> (4) Calcular promedio de Montos Totales\n:::>>> (5) Mostrar datos del Paciente Mayor de Edad\n:::>>> (6) Mostrar datos del Paciente Menor de Edad\n:::>>> (7) Salir del Programa\n\n:::>>> Ingrese Opcion: ", False, True, False, 0, 8, 0, 0)
    return dataOpc
#############################################################################################################################################################################################################################################################################################################################################################################################
def runOptions(dataOpc, arreglo):
    finish = False
    if len(arreglo) == 0:
        match dataOpc:
            case 1:
                while True:
                    formRegistration()
                    finishForm = finishProgram(" - Desea dejar de registrar? -\n:::>>> escriba (SI) para finalizarlo\n:::>>> presione cualquier boton y/o enter para continuar registrando pacientes\n\n:::>>> Ingrese respuesta: ")
                    if finishForm == True: break
            case 2: finish = finishProgram(" - Desea salir del programa? -\n:::>>> escriba (SI) para finalizarlo\n:::>>> presione cualquier boton y/o enter para continuar el programa\n\n:::>>> Ingrese respuesta: ")
            case _: print("Error")
    else:
        match dataOpc:
            case 1:
                while True:
                    formRegistration()
                    finishForm = finishProgram(" - Desea dejar de registrar? -\n:::>>> escriba (SI) para finalizarlo\n:::>>> presione cualquier boton y/o enter para continuar registrando pacientes\n\n:::>>> Ingrese respuesta: ")
                    if finishForm == True: break
            case 2: idSearch(listID)
            case 3: printLists()
            case 4: averageAmounts()
            case 5: olderOrYounger("major")
            case 6: olderOrYounger("minor")
            case 7: finish = finishProgram(" - Desea salir del programa? -\n:::>>> escriba (SI) para finalizarlo\n:::>>> presione cualquier boton y/o enter para continuar el programa\n\n:::>>> Ingrese respuesta: ")
            case _: print("Error")
        if dataOpc > 1 and dataOpc <7: input(":::>>> Enter para continuar")
    return finish
#############################################################################################################################################################################################################################################################################################################################################################################################
def formRegistration():
    name = stringValidation(":::>>> Por favor Introduzca el nombre del paciente\n:::>>> ", 3, 25)
    while True:
        id = intValidation(":::>>> Por favor Introduzca el numero de cedula del paciente\n:::>>> ", False, False, True, 0, 0, 7, 8)
        encontrada = idValidation(id)
        if len(listID) == 0: break
        if encontrada == False: break
        else: print(f":::>>> ERROR numero de cedula {id} ya esta registrada en base de datos")
    age = intValidation(":::>>> Por favor Introduzca la edad del paciente\n:::>>> ", False, True, False, 0, 105, 0, 0)
    while True:
        gender = stringValidation(":::>>> Por favor Introduzca el genero del paciente (M) para masculinos y (F) para femeninos\n:::>>> ", 1, 1)
        if gender.upper() == "M" or gender.upper() == "F": break
        else: print(f":::>>> ERROR: ({gender.upper()}) no es una opcion valida\n:::>>> Elija por favor una seleccion valida:\n:::>>> (F) para femenino\n:::>>> (M) para masculino")
    diagnostic = stringValidation(":::>>> Por favor Introduzca el diagnostico del paciente\n:::>>> ", 15, 100)
    cancelledAmount = intValidation(":::>>> Por favor Introduzca el monto total cancelado\n:::>>> ", True, False, True, 0, 0, 1, 6)
    listNames.append(name)
    listID.append(id)
    listAge.append(age)
    listaGenre.append(gender.upper())
    listDiagnostics.append(diagnostic)
    listCancelledAmount.append(cancelledAmount)
#############################################################################################################################################################################################################################################################################################################################################################################################
def printLists():
    for paciente in range(len(listNames)):
        print(f"#{paciente+1} -----------------------------------------\nNombre del Paciente: {listNames[paciente]}\nCedula: {listID[paciente]}\nEdad: {listAge[paciente]} | Genero: {listaGenre[paciente]}\nDiagnostico: {listDiagnostics[paciente]}\nMonto Cancelado: {listCancelledAmount[paciente]}")
#############################################################################################################################################################################################################################################################################################################################################################################################
def averageAmounts():
    accumulator = 0
    for paciente in range(len(listNames)):
        accumulator = accumulator + listCancelledAmount[paciente]
    print(f":::>>> Promedio por total de montos cancelados\n:::>>> Cantidad de pacientes: {len(listNames)}\n:::>>> Total cancelado: {accumulator}\n\n:::>>> Promedio Total es de: {accumulator/len(listNames)}")
#############################################################################################################################################################################################################################################################################################################################################################################################
def olderOrYounger(who):
    major = 0
    for doubleCycle in range(2):
        for paciente in range(len(listNames)):
            if doubleCycle==0 and listAge[paciente] > major: 
                major = listAge[paciente]
                idMajor = paciente
                minor = major
            if doubleCycle==1 and listAge[paciente] < minor:
                minor = listAge[paciente]
                idMinor = paciente
    if who == "major": print(f":::>>> El paciente mayor de edad es el paciente:\nNombre: {listNames[idMajor]}\nCedula: {listID[idMajor]}\nEdad: {listAge[idMajor]} | Genero: {listaGenre[idMajor]}\nDiagnostico: {listDiagnostics[idMajor]}")
    elif who == "minor": print(f":::>>> El paciente menor de edad es el paciente:\nNombre: {listNames[idMinor]}\nCedula: {listID[idMinor]}\nEdad: {listAge[idMinor]} | Genero: {listaGenre[idMinor]}\nDiagnostico: {listDiagnostics[idMinor]}")

#############################################################################################################################################################################################################################################################################################################################################################################################
def  intValidation(message, starInt, doRange, charRange, rankMinor, rankMajor, charMinor, charMajor):
    while True:
        data = input(message)
        firstValidation = isAnInt(data)
        if firstValidation == True:
            finalData = int(data)
            if starInt == True: secondValidation = isMajorNumber(finalData, rankMinor)
            else: secondValidation = True
            if doRange == True: thirdValidation = isRange(finalData, rankMinor, rankMajor)
            else: thirdValidation = True
            if charRange == True: fourthValidation = isCharRange(data, charMinor, charMajor)
            else: fourthValidation = True
        if firstValidation and secondValidation and thirdValidation and fourthValidation == True:
            return finalData   
#############################################################################################################################################################################################################################################################################################################################################################################################
def stringValidation(message, charMinor, charMajor):
    while True:
        data = input(message)
        dataWithoutSpaces = withoutSpaces(data)
        firstValidation = isString(dataWithoutSpaces)
        secondValidation = isCharRange(data, charMinor, charMajor)
        if firstValidation and secondValidation == True: break
    return data
#############################################################################################################################################################################################################################################################################################################################################################################################
def idValidation(id):
    for cedula in range(len(listID)):
        if id == listID[cedula]: return True
    return False
#############################################################################################################################################################################################################################################################################################################################################################################################
def idSearch(arreglo):
    dataSearch = intValidation(":::>>> Por favor Introduzca el numero de cedula del paciente que desea buscar\n:::>>> ", False, False, True, 0, 0, 7, 8)
    for paciente in range(len(arreglo)):
        if dataSearch == arreglo[paciente]: print(f":::>>> Paciente encontrado.\nNombre del Paciente: {listNames[paciente]} | Cedula: {listID[paciente]}\n Edad: {listAge[paciente]} | Genero: {listaGenre[paciente]}\nDiagnostico: {listDiagnostics[paciente]}\nMonto Cancelado: {listCancelledAmount[paciente]}")
        else: print(":::>>> Paciente no encontrado")
#############################################################################################################################################################################################################################################################################################################################################################################################
def withoutSpaces(data): #data variable que le quitare espacios
    dataWithoutSpaces = "" #creo una variable vacia
    for caracter in data: #itero la variable a ser chequeada caracter por caracter
        if caracter != " ": #si el caracter es distinto de un espacio
            dataWithoutSpaces = dataWithoutSpaces + caracter #sumalo a la variable vacia
    return dataWithoutSpaces #retorname el caracter sin espacios :D :D :D :D :D
#############################################################################################################################################################################################################################################################################################################################################################################################
def isAnInt(data):
    if data.isdigit(): return True
    else:
        print(":::>>> ERROR\n:::>>> Numero Introducido debe ser solamente numerico")
        return False
#############################################################################################################################################################################################################################################################################################################################################################################################
def isString(data):
    if data.isalpha(): return True
    else:
        print(":::>>> ERROR\n:::>>> Dato Introducido debe ser solamente alfabetico")
#############################################################################################################################################################################################################################################################################################################################################################################################
def isMajorNumber(data, dataMinor):
    if data >= dataMinor: return True
    else:
        print(f":::>>> ERROR\n:::>>> Dato no puede ser menor a {dataMinor}")
#############################################################################################################################################################################################################################################################################################################################################################################################
def isRange(data, dataMinor, dataMajor):
    if data > dataMinor and data < dataMajor: return True
    else:
        print(":::>>> ERROR")
        if data <= dataMinor: print(f":::>>> Dato no puede ser menor a {dataMinor+1}")
        elif data >= dataMajor: print(f":::>>> Dato no puede ser mayor a {dataMajor-1}")
#############################################################################################################################################################################################################################################################################################################################################################################################
def isCharRange(data, dataMinor, dataMajor):
    if len(data) >= dataMinor and len(data) <= dataMajor: return True
    else:
        print(":::>>> ERROR")
        if len(data) <= dataMinor: print(f":::>>> Dato no puede tener menos de {dataMinor} caracteres")
        elif len(data) >= dataMajor: print(f":::>>> Dato no puede tener mas de {dataMajor} caracteres")
#############################################################################################################################################################################################################################################################################################################################################################################################
def finishProgram(message):
    question = input(message).upper()
    if question == "SI": return True
    else: return False
#############################################################################################################################################################################################################################################################################################################################################################################################
#Cuerpo Principal
listNames, listID, listAge, listaGenre, listDiagnostics, listCancelledAmount = dataLists()
while True:
    dataOpc = selectOptions(listNames)
    Finish = runOptions(dataOpc, listNames)
    if Finish == True: break