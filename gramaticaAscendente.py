
# -----------------------------------------------------------------------------
# Grupo 6
#
# Universidad de San Carlos de Guatemala
# Facultad de Ingenieria
# Escuela de Ciencias y Sistemas
# Organizacion de Lenguajes y Compiladores 2
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                       INICIA ANALIZADOR LEXICO
# -----------------------------------------------------------------------------
#palabras reservadas del lenguaje
reservadas = {
    #   PALABRAS RESERVADAS POR SQL
    'show' : 'SHOW',
    'databases' : 'DATABASES',
    'tables' : 'TABLES',
    'columns' : 'COLUMNS',
    'from' : 'FROM',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'of':'OF',
    'order' : 'ORDER',
    'by' : 'BY',
    'where' : 'WHERE',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'in' : 'IN',
    'concat' : 'CONCAT',
    'only':'ONLY',

    'as' : 'AS',
    'upper' : 'UPPER',
    'sqrt' : 'SQRT',
    'avg' : 'AVG',
    'sum' : 'SUM',
    'cont' :'CONT',
    'desc' : 'DESC',
    'asc' : 'ASC',
    'like' : 'LIKE',
    'min' : 'MIN',
    'max' : 'MAX',
    'abs' : 'ABS',
    'on' : 'ON',
    'union' : 'UNION',
    'all' : 'ALL',
    'insert' : 'INSERT',
    'unknown':'UNKNOWN',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'set' : 'SET',
    'delete' : 'DELETE',
    'create' : 'CREATE',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'null' : 'NULL',
    'nulls':'NULLS',

    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div':'DIV',
    'exp':'EXP',
    'factorial':'FACTORIAL',
    'floor':'FLOOR',
    'gcd':'GCD',
    'lcm':'LCM',
    'ln':'LN',
    'log':'LOG',
    'log10':'LOG10',
    'current':'CURRENT',
    'default' : 'DEFAULT',
    'auto_increment' : 'AUTO_INCREMENT',
    'alter' : 'ALTER',
    'table' : 'TABLE',
    'add' : 'ADD',
    'drop' : 'DROP',
    'column' : 'COLUMN',
    'rename' : 'RENAME',
    'to' : 'TO',
    'view' : 'VIEW',
    'replace' : 'REPLACE',
    'type' : 'TYPE',
    'enum' : 'ENUM',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'min_scale':'MIN_SCALE',
    'mod':'MOD',
    'pi':'PI',
    'power':'POWER',
    'radians':'RADIANS',
    'round':'ROUND',
    'scale':'SCALE',
    'sing':'SING',
    'mode' : 'MODE',
    'owner' : 'OWNER',
    'constraint' : 'CONSTRAINT',
    'foreign' : 'FOREIGN',
    'references' : 'REFERENCES',
    'inherits' : 'INHERITS',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'substring' : 'SUBSTRING',
    'inner' : 'INNER',
    'outer' : 'OUTER',
    'ingerits':'INGERITS',
    'trim_scale':'TRIM_SCALE',
    'truc':'TRUC',
    'width_bucket':'WIDTH_BUCKET',
    'random':'RANDOM',
    'setseed':'SETSEED',
    'acos':'ACOS',
    'acosd':'ACOSD',
    'asin':'ASIN',
    'asind':'ASIND',
    'atan':'ATAN',
    'atan2':'ATAN2',
    'cos':'COS',
    'cosd':'COSD',
    'cot':'COT',
    'cotd':'COTD',
    'sin':'SIN',
    'sind':'SIND',
    'tan':'TAN',
    'tand':'TAND',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'asinh':'ASINH',
    'acosh':'ACOSH',
    'atanh':'ATANH',
    'length':'LENGTH',
    'substring':'SUBSTRING',
    'trim':'TRIM',
    'get_byte':'GET_BYTE',
    'md5':'MD5',
    'set_byte':'SET_BYTE',
    'sha256':'SHA256',
    'substr':'SUBSTR',
    'convert':'CONVERT',
    'encode':'ENCODE',
    'decode':'DECODE',
    'escape':'ESCAPE',
    'any':'ANY',
    'some':'SOME',
    'using':'USING',
    'first':'FIRST',
    'last':'LAST',
    'current_user':'CURRENT_USER',
    'session_user':'SESSION_USER',
    'symmetric':'SYMMETRIC',
    'izquierda' : 'LEFT',
    'derecha' : 'RIGHT',
    'full' : 'FULL',
    'join' : 'JOIN',
    'natural' : 'NATURAL',
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'begin' : 'BEGIN',
    'end' : 'END',
    'else' : 'ELSE',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    #  tipos de datos permitidos
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'money' : 'MONEY',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'text' : 'TEXT',
    'boolean' : 'BOOLEAN',
    'timestamp':'TIMESTAMP',
    'time':'TIME',
    'date':'DATE',
    'interval':'INTERVAL',
    'year':'YEAR',
    'month':'MONTH',
    'day':'DAY',
    'hour':'HOUR',
    'minute':'MINUTE',
    'second':'SECOND',
    'to':'TO',
    'true':'TRUE',
    'false':'FALSE',
    'declare' : 'DECLARE',
    'function' : 'FUNCTION',
    'returns' : 'RETURNS',
    'returning':'RETURNING',

    'between' : 'BETWEEN',
    'ilike' : 'ILIKE',
    'is':'IS',
    'isnull':'ISNULL',
    'notnull':'NOTNULL',
    #enums
    'type':'TYPE',
    'ENUM':'ENUM',



# revisar funciones de tiempo y fechas
}
# listado de tokens que manejara el lenguaje (solo la forma en la que los llamare  en las producciones)
tokens  = [
    'PUNTOYCOMA',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
'DOSPUNTOS',
    'PUNTO',
    'TYPECAST',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'POTENCIA',
    'RESIDUO',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'DIFERENTE',
    'IGUALIGUAL',
    'PARENTESISIZQUIERDA',
    'PARENTESISDERECHA',

    'COMA',
    'NOTEQUAL',
    'SIMBOLOOR',
    'SIMBOLOAND',
    'SIMBOLOOR2',
    'NUMERAL',
    'COLOCHO',
    'DESPLAZAMIENTODERECHA',
    'DESPLAZAMIENTOIZQUIERDA',


#tokens que si devuelven valor
    'DECIMALTOKEN',
    'ENTERO',
    'CADENA',
    'ETIQUETA',
    'ID'
] + list(reservadas.values())

# Tokens y la forma en la que se usaran en el lenguaje
t_PUNTOYCOMA                            = r';'
t_MAS                                   = r'\+'
t_MENOS                                 = r'-'
t_POR                                   = r'\*'
t_DIV                                   = r'/'
t_DOSPUNTOS                             = r':'
t_PUNTO                                 = r'.'
t_TYPECAST                              = r'::'
t_CORCHETEDER                           = r']'
t_CORCHETEIZQ                           = r'\['
t_POTENCIA                              = r'\^'
t_RESIDUO                               = r'%'
t_MAYOR                                 = r'<'
t_MENOR                                 = r'>'
t_IGUAL                                 = r'='
t_MAYORIGUAL                            = r'>='
t_MENORIGUAL                            = r'<='
t_DIFERENTE                             = r'<>'
t_IGUALIGUAL                            = r'=='
t_PARENTESISIZQUIERDA                   = r'\('
t_PARENTESISDERECHA                     = r'\)'
t_COMA                                  = r','
t_NOTEQUAL                              = r'!='
t_SIMBOLOOR                             = r'\|\|'
t_SIMBOLOAND                            = r'&&'
t_SIMBOLOOR2                            = r'\|'
t_NUMERAL                               = r'\#'
t_COLOCHO                               = r'~'
t_DESPLAZAMIENTODERECHA                 = r'>>'
t_DESPLAZAMIENTOIZQUIERDA               = r'<<'



#definife la estructura de los decimales
def t_DECIMALTOKEN(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor decimal es muy largo %d", t.value)
        t.value = 0
    return t
#definife la estructura de los enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor del entero es muy grande %d", t.value)
        t.value = 0
    return t
#definife la estructura de los identificadores que en este caso seran $letra y numero
def t_ID(t):
     r'\$[t|a|v|ra|s|p]+[0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t
#definife la estructura de las cadenas
def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # quito las comillas del inicio y final de la cadena
    return t 
#definife la estructura de las etiquetas, por el momento las tomo unicamente como letras y numeros
def t_ETIQUETA(t):
     r'[a-zA-Z0-9]+'
     t.type = reservadas.get(t.value.lower(),'ETIQUETA')    # Check for reserved words
     return t

# Comentario simple # ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n|)*?\*/'
    t.lexer.lineno += t.value.count("\n")
# ----------------------- Caracteres ignorados -----------------------
# caracter equivalente a un tab
t_ignore = " \t"
#caracter equivalente a salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter lexico no permitido ==> '%s'" % t.value)
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# -----------------------------------------------------------------------------
#                       INICIA ANALIZADOR SINTACTICO
# -----------------------------------------------------------------------------

# Asociación de operadores y precedencia
precedence = (
    ('left','TYPECAST'),
    ('right','UMINUS'),
    ('left','MAS','MENOS'),
    ('left','POTENCIA'),
    ('left','POR','DIV','RESIDUO'),
    )



# estructura de mi gramatica



def p_inicio(t) :
    'inicio               : operacion' 
    t[0]=t[1]  
    


"""def p_query(t):
    '''query        : crearBD
                    
                    '''
                    # derivando cada produccion a cosas como el create, insert, select; funciones como avg, sum, substring irian como otra produccion 
                    #dentro del select (consulta)


# empiezan las producciones de las operaciones finales
#la englobacion de las operaciones"""

""" 
                    | mostrarBD
                    | eliminarBD
                    | crearTabla
                    | modificarBD
                    | eliminarTabla
                    | alterTabla
                    | insertarRegistro
                    | modificarRegistro
                    | eliminarRegistro
                    | consulta
                    | funciones

"""
def p_operacion(t):
    '''operacion        : ENTERO MAS ENTERO
                        | ENTERO MENOS ENTERO
                        '''
    if (t[2]=="+"):
        t[0]=t[1]+t[3]
    elif (t[2]=="-"):
        t[0]=t[1]-t[3]


def p_operacion_menos_unario(t):
    'operacion : MENOS ENTERO  %prec UMINUS'
    t[0] = -t[2]





#para manejar los errores sintacticos
#def p_error(t): #en modo panico :v
  #  print("token error: ",t)
   # print("Error sintáctico en '%s'" % t.value[0])
   # print("Error sintáctico en '%s'" % t.value[1])
    

#def p_error(t): #en modo panico :v
#   while True:
#        tok=parser.token()
#        if not tok or tok.type==';':break
#    parser.errok()
#    return tok
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    #print((token.lexpos - line_start) +1 )
    return (token.lexpos - line_start) 


def p_error(t):
     print("token: '%s'" %t)
     print("Error sintáctico en '%s' " % t.value)
     #h.filapivote+=1
     # Read ahead looking for a closing '}'
     while True:
         tok = parser.token()             # Get the next token
         if not tok or tok.type == 'PUNTOYCOMA': 
             break
     parser.restart()
     
import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)