table_types = {'*': {'MATRIX_MATRIX' : 'MATRIX',
                     'SCALAR_MATRIX' : 'MATRIX',
                     'NUMBER_MATRIX' : 'MATRIX',
                     'SCALAR_SCALAR' : 'SCALAR',
                     'SCALAR_VECTOR' : 'VECTOR',
                     'NUMBER_VECTOR' : 'VECTOR',
                     'NUMBER_NUMBER' : 'NUMBER'
                     },
               '@' : {
                     'MATRIX_MATRIX' : 'MATRIX',
                     'MATRIX_VECTOR' : 'VECTOR',
                     'VECTOR_VECTOR' : 'SCALAR'
               },
               '**': {'MATRIX_SCALAR' : 'MATRIX',
                      'MATRIX_NUMBER' : 'MATRIX',
                      'SCALAR_SCALAR' : 'SCALAR',
                      'SCALAR_NUMBER' : 'SCALAR',
                      'NUMBER_SCALAR' : 'SCALAR',
                      'NUMBER_NUMBER' : 'NUMBER'},
               '+' : {'MATRIX_MATRIX' : 'MATRIX',
                      'VECTOR_VECTOR' : 'VECTOR',
                      'SCALAR_SCALAR' : 'SCALAR',
                      'SCALAR_NUMBER' : 'SCALAR',
                      'NUMBER_SCALAR' : 'SCALAR'},
               '-' : {'MATRIX_MATRIX' : 'MATRIX',
                      'VECTOR_VECTOR' : 'VECTOR'},
               '/' : {'MATRIX_MATRIX' : 'MATRIX'},
               '~' : {'MATRIX_' : 'MATRIX'},
               'exp' : {'MATRIX_' : 'MATRIX'},
               'det' : {'MATRIX_' : 'SCALAR'},
               '^T' : {'MATRIX_' : 'MATRIX'}
               }

def calc_type(data,T):
    op = data[3]
    a = data[1]
    b = data[2]
    res = ""
    if op in table_types:

        if a in T and b in T:
            res = table_types[op][T[a] + "_" + T[b]]
        if a in T and b not in T:
            # print("Op ",op)
            res = table_types[op][T[a] + "_"]
        if a not in T and b in T:
            res = table_types[op]["_" + T[b]]
    return res

