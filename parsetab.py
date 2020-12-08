
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTYPECASTrightUMINUSleftMASMENOSleftPOTENCIAleftPORDIVRESIDUOABS ACOS ACOSD ACOSH ADD ALL ALTER AND ANY AS ASC ASIN ASIND ASINH ATAN ATAN2 ATANH AUTO_INCREMENT AVG BEGIN BETWEEN BIGINT BOOLEAN BY CADENA CASE CBRT CEIL CEILING CHAR CHARACTER CHECK COLOCHO COLUMN COLUMNS COMA CONCAT CONSTRAINT CONT CONVERT CORCHETEDER CORCHETEIZQ COS COSD COSH COT COTD CREATE CURRENT CURRENT_USER DATABASE DATABASES DATE DAY DECIMAL DECIMALTOKEN DECLARE DECODE DEFAULT DEGREES DELETE DESC DESPLAZAMIENTODERECHA DESPLAZAMIENTOIZQUIERDA DIFERENTE DISTINCT DIV DIV DOSPUNTOS DOUBLE DROP ELSE ENCODE END ENTERO ENUM ENUM ESCAPE ETIQUETA EXCEPT EXISTS EXP FACTORIAL FALSE FIRST FLOOR FOREIGN FROM FULL FUNCTION GCD GET_BYTE GREATEST GROUP HAVING HOUR ID IF IGUAL IGUALIGUAL ILIKE IN INGERITS INHERITS INNER INSERT INTEGER INTERSECT INTERVAL INTO IS ISNULL JOIN KEY LAST LCM LEAST LEFT LENGTH LIKE LIMIT LN LOG LOG10 MAS MAX MAYOR MAYORIGUAL MD5 MENOR MENORIGUAL MENOS MIN MINUTE MIN_SCALE MOD MODE MONEY MONTH NATURAL NOT NOTEQUAL NOTNULL NULL NULLS NUMERAL NUMERIC OF OFFSET ON ONLY OR ORDER OUTER OWNER PARENTESISDERECHA PARENTESISIZQUIERDA PI POR POTENCIA POWER PRIMARY PUNTO PUNTOYCOMA RADIANS RANDOM REAL REFERENCES RENAME REPLACE RESIDUO RETURNING RETURNS RIGHT ROUND SCALE SECOND SELECT SESSION_USER SET SETSEED SET_BYTE SHA256 SHOW SIMBOLOAND SIMBOLOOR SIMBOLOOR2 SIN SIND SING SINH SMALLINT SOME SQRT SUBSTR SUBSTRING SUM SYMMETRIC TABLE TABLES TAN TAND TANH TEXT THEN TIME TIMESTAMP TO TRIM TRIM_SCALE TRUC TRUE TYPE TYPECAST UNION UNIQUE UNKNOWN UPDATE UPPER USING VALUES VARCHAR VARYING VIEW WHEN WHERE WIDTH_BUCKET YEARinicio               : queriesqueries               : queries queryqueries               : queryquery        : mostrarBD\n                    | crearBD\n                    \n    crearBD    : CREATE DATABASE ID PUNTOYCOMAcrearBD    : CREATE OR REPLACE DATABASE ID PUNTOYCOMAcrearBD    : CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMAcrearBD    : CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMAparametrosCrearBD : parametrosCrearBD parametroCrearBDparametrosCrearBD :  parametroCrearBDparametroCrearBD :  OWNER IGUAL final\n                        |  MODE IGUAL final\n    mostrarBD  : SHOW DATABASES PUNTOYCOMAoperacion : MENOS ENTERO  %prec UMINUSfinal              : DECIMAL\n                          | ENTEROfinal              : ID'
    
_lr_action_items = {'SHOW':([0,2,3,4,5,8,12,15,21,31,33,],[6,6,-3,-4,-5,-2,-14,-6,-9,-7,-8,]),'CREATE':([0,2,3,4,5,8,12,15,21,31,33,],[7,7,-3,-4,-5,-2,-14,-6,-9,-7,-8,]),'$end':([1,2,3,4,5,8,12,15,21,31,33,],[0,-1,-3,-4,-5,-2,-14,-6,-9,-7,-8,]),'DATABASES':([6,],[9,]),'DATABASE':([7,14,],[10,20,]),'OR':([7,],[11,]),'PUNTOYCOMA':([9,13,16,17,22,25,26,27,28,29,30,32,],[12,15,21,-11,-10,31,-12,-16,-17,-18,-13,33,]),'ID':([10,20,23,24,],[13,25,29,29,]),'REPLACE':([11,],[14,]),'OWNER':([13,16,17,22,25,26,27,28,29,30,32,],[18,18,-11,-10,18,-12,-16,-17,-18,-13,18,]),'MODE':([13,16,17,22,25,26,27,28,29,30,32,],[19,19,-11,-10,19,-12,-16,-17,-18,-13,19,]),'IGUAL':([18,19,],[23,24,]),'DECIMAL':([23,24,],[27,27,]),'ENTERO':([23,24,],[28,28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'queries':([0,],[2,]),'query':([0,2,],[3,8,]),'mostrarBD':([0,2,],[4,4,]),'crearBD':([0,2,],[5,5,]),'parametrosCrearBD':([13,25,],[16,32,]),'parametroCrearBD':([13,16,25,32,],[17,22,17,22,]),'final':([23,24,],[26,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> queries','inicio',1,'p_inicio_1','gramaticaAscendente.py',376),
  ('queries -> queries query','queries',2,'p_queries_1','gramaticaAscendente.py',380),
  ('queries -> query','queries',1,'p_queries_2','gramaticaAscendente.py',383),
  ('query -> mostrarBD','query',1,'p_query','gramaticaAscendente.py',387),
  ('query -> crearBD','query',1,'p_query','gramaticaAscendente.py',388),
  ('crearBD -> CREATE DATABASE ID PUNTOYCOMA','crearBD',4,'p_crearBaseDatos_1','gramaticaAscendente.py',400),
  ('crearBD -> CREATE OR REPLACE DATABASE ID PUNTOYCOMA','crearBD',6,'p_crearBaseDatos_2','gramaticaAscendente.py',404),
  ('crearBD -> CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA','crearBD',7,'p_crearBaseDatos_3','gramaticaAscendente.py',407),
  ('crearBD -> CREATE DATABASE ID parametrosCrearBD PUNTOYCOMA','crearBD',5,'p_crearBaseDatos_4','gramaticaAscendente.py',410),
  ('parametrosCrearBD -> parametrosCrearBD parametroCrearBD','parametrosCrearBD',2,'p_parametrosCrearBD_1','gramaticaAscendente.py',415),
  ('parametrosCrearBD -> parametroCrearBD','parametrosCrearBD',1,'p_parametrosCrearBD_2','gramaticaAscendente.py',418),
  ('parametroCrearBD -> OWNER IGUAL final','parametroCrearBD',3,'p_parametroCrearBD','gramaticaAscendente.py',421),
  ('parametroCrearBD -> MODE IGUAL final','parametroCrearBD',3,'p_parametroCrearBD','gramaticaAscendente.py',422),
  ('mostrarBD -> SHOW DATABASES PUNTOYCOMA','mostrarBD',3,'p_mostrarBD','gramaticaAscendente.py',426),
  ('operacion -> MENOS ENTERO','operacion',2,'p_operacion_menos_unario','gramaticaAscendente.py',430),
  ('final -> DECIMAL','final',1,'p_final','gramaticaAscendente.py',435),
  ('final -> ENTERO','final',1,'p_final','gramaticaAscendente.py',436),
  ('final -> ID','final',1,'p_final_id','gramaticaAscendente.py',439),
]
