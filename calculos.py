
import math

documentos = ['Administración Avanzada de Bases de Datos es un curso en el que se busca llevar al estudiante más allá',
             'del paradigma de base de datos relacional y SQL que se enseña tradicionalmente en el nivel de pregrado',
             'en las Escuelas de Ingeniería En este curso se pretende introducir al estudiante en temas de gran',
             'importancia en el ámbito de las bases de datos como desempeño y escalabilidad Además se busca',
             'presentar al estudiante paradigmas contemporáneos y complementarios del modelo relacional como bases',
             'de datos multidimensionales, geográficas y NoSQL',
             ]


dictadoDePalabras = {}

for indice, sentencia in enumerate(documentos):
    tokenPalabra = sentencia.split(' ')
    dictadoDePalabras[indice] = [(palabra,tokenPalabra.count(palabra)) for palabra in tokenPalabra]

termFrecuencia = {}

for i in range(0, len(documentos)):
    listaDeNoDuplicados = []
    for palabraFrequencia in dictadoDePalabras[i]:
        if palabraFrequencia not in listaDeNoDuplicados:
            listaDeNoDuplicados.append(palabraFrequencia)
        termFrecuencia[i] = listaDeNoDuplicados

terminoNormalizadoFrecuencia = {}
for i in range(0, len(documentos)):
    sentencia = dictadoDePalabras[i]
    lenDeSentencia = len(sentencia)
    listaDeNormalizados = []
    for palabraFrequencia in termFrecuencia[i]:
        normalizedFreq = palabraFrequencia[1]/lenDeSentencia
        listaDeNormalizados.append((palabraFrequencia[0],normalizedFreq))
    terminoNormalizadoFrecuencia[i] = listaDeNormalizados



todosDocumento = ''
for sentencia in documentos:
    todosDocumento += sentencia + ' '
todosDocumentosToken = todosDocumento.split(' ')


todosDocumentoNoDuplicados = []

for palabra in todosDocumentosToken:
    if palabra not in todosDocumentoNoDuplicados:
        todosDocumentoNoDuplicados.append(palabra)



dictDeNumDeDocConTermDentro = {}

for indice, voc in enumerate(todosDocumentoNoDuplicados):
    count = 0
    for sentencia in documentos:
        if voc in sentencia:
            count += 1
    dictDeNumDeDocConTermDentro[indice] = (voc, count)



dictOFIDFNoDuplicados = {}


for i in range(0, len(terminoNormalizadoFrecuencia)):
    listOfIDFCalcs = []
    for palabra in terminoNormalizadoFrecuencia[i]:
        for x in range(0, len(dictDeNumDeDocConTermDentro)):
            if palabra[0] == dictDeNumDeDocConTermDentro[x][0]:
                listOfIDFCalcs.append((palabra[0],math.log(len(documentos)/dictDeNumDeDocConTermDentro[x][1])))
    dictOFIDFNoDuplicados[i] = listOfIDFCalcs


dictOFTF_IDF = {}
for i in range(0,len(terminoNormalizadoFrecuencia)):
    listaOFTF_IDF = []
    TFsentencia = terminoNormalizadoFrecuencia[i]
    IDFsentencia = dictOFIDFNoDuplicados[i]
    for x in range(0, len(TFsentencia)):
        listaOFTF_IDF.append((TFsentencia[x][0],TFsentencia[x][1]*IDFsentencia[x][1]))
    dictOFTF_IDF[i] = listaOFTF_IDF



def result():
    return dictOFTF_IDF
