# Este script compara 2 sets de palabras clave con otro set, que sera otorgado por el usuario. 
# Al realizar una interseccion a los sets, colocaran todas las similitudes. Dependiendo de la cantidad 
# encontrada, decidira si esta escrito en un lenguaje u otro.

# Palabras encontradas en: 
# https://www.berlitz.com/es-co/blog/100-palabras-mas-usadas-en-ingles

EnglishWords = {'the', 'be', 'to', 'of', 'and', 'in', 'that', 'have', 'i', 
'it', 'for', 'not', 'on', 'with', 'as', 'you', 'at', 'this', 'but', 
'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 
'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 
'who', 'get', 'which', 'go', 'when', 'make', 'can', 'like', 'time', 'just', 
'him', 'know', 'take', 'person', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 
'see', 'other', 'than', 'then', 'now', 'look', 'only', 'its', 'over', 'think', 'also', 
'back', 'after', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 
'because', 'any', 'these', 'give', 'day', 'most', 'us', 'is'}

# Palabras encontradas en: 
# https://www.clarin.com/sociedad/palabras-mas-usadas-espanol-comunes-frecuentes-diccionario-real_academia_espanola_0_ByLqjSFvmg.html

SpanishWords = {'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en' , 'entre', 
'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'sobre', 'tras', 'versus', 'via',
"el", "la", "los", "las", "un", "una", "unos", "unas",'abajo', 'abrir', 'acá', 'acuerdo', 'adiós', 'afirmar', 
'ahí', 'ahora', 'al', 'algo', 'algún', 'alrededor', 'amigo', 'amo', 'anteayer', 'aquí', 'así', 'si', 
'aunque', 'ayer', 'bien', 'cada', 'cambio', 'casi', 'cerca', 'cierto', 'cinco', 'clase', 'comenzar', 
'como', 'compañero', 'conocer', 'cosas', 'creer', 'cual', 'cuando', 'cuatro', 'cuenta', 'dar', 
'decir', 'dentro', 'después', 'difícil', 'diferente', 'digo', 'donde', 'dos', 'durar', 
'él', 'ella', 'ello', 'encontrar', 'enero', 'entonces', 'es', 'esa', 'ese', 'eso', 'esos', 
'este', 'esto','esta', 'experiencia', 'fácil', 'feliz', 'fin', 'forma', 'frente', 'fuera', 'fuego', 
'general', 'gente', 'gracias', 'gran', 'grupo', 'haber', 'hablar', 'hacer', 'hombre', 'hora', 
'hoy', 'igual', 'importante', 'junto', 'lado', 'lamentablemente', 'largo', 'llegar', 'llevar',
'lugar', 'madre', 'mañana', 'mayoría', 'mejor', 'menos', 'mes', 'mismo', 'mujer', 'mundo', 
'nada', 'nadie', 'nombre', 'nuevo', 'ocho', 'octubre', 'ojalá', 'otro', 'parecer', 'parte', 
'pasar', 'paso', 'pequeño', 'pero', 'poco', 'poder', 'político', 'poner', 'posible', 'primer', 
'problema', 'proceso', 'pronto', 'quedar', 'querer', 'quién', 'realizar', 'razón', 'responder', 
'saber', 'sí', 'sido', 'siempre', 'siete', 'sino', 'solo', 'tan', 'tarde', 'tener', 'tiempo', 
'todavía', 'todo', 'tomar', 'trabajo', 'tratar', 'tres', 'uno', 'veces', 'ver', 'vida', 
'volver', 'ya', 'año', 'yendo','que', 'porque'}

Texto = set(input("Escriba su texto: ").lower().split())

EnglishWordFound = SpanishWordFound = set
EnglishWordFound =  len(EnglishWords.intersection(Texto))
SpanishWordFound = len(SpanishWords.intersection(Texto))

print(f"English Words Found = {EnglishWordFound}")
print(f"Spanish Words Found = {SpanishWordFound}")

if SpanishWordFound > 5 and EnglishWordFound > 5:
    print("El texto esta en Spanglish.")
elif EnglishWordFound > 5:
    print("El texto esta en ingles.")
elif SpanishWordFound > 5:
    print("El texto esta en español.")
else:
    #Si las palabras clave encontraads son menos de 5
    print("El texto es muy corto o no contiene ninguna palabra que detectemos.")


# Si encuentra palabras clave de ambos idiomas
if EnglishWordFound != 0 and SpanishWordFound != 0:
    print("El texto puede que contenga palabras en otro idioma.")
