import re
def Mul(x,a,b,Tr):
    res = "?"
    t_a = Tr[a]
    t_b = Tr[b]
    t_x = Tr[x]
    if t_x == "MATRIX":
        res =  f"{x}.Mul({a},{b})\n"
    if t_x == "VECTOR":
        res = f"{x}.MulVec({a},{b})\n"
    if t_a == 'VECTOR' and t_b == 'VECTOR':
        res = f"{x} := mat.Dot({a},{b})\n"
        refs.append(x)
    return res

def Add(x,a,b,Tr):
    res = "?"
    t_a = Tr[a]
    t_b = Tr[b]
    t_x = Tr[x]
    if t_a == 'MATRIX' and t_b == 'MATRIX':
        res = f"{x}.Add({a},{b})\n"
    elif (t_a == 'SCALAR' or t_a == 'NUMBER') and (t_b == 'SCALAR' or t_b == 'NUMBER'):
        res = f"{x} := {a} + {b}\n"
    elif t_a == 'VECTOR' and t_b == 'VECTOR':
        res = f"{x}.AddVec({a},{b})\n"
    return res

def Sub(x,a,b,Tr):
    res = '?'
    t_a = Tr[a]
    t_b = Tr[b]
    t_x = Tr[x]
    if t_a == 'MATRIX' and t_b == 'MATRIX':
        res = f"{x}.Sub({a},{b})\n"
    elif (t_a == 'SCALAR' or t_a == 'NUMBER') and (t_b == 'SCALAR' or t_b == 'NUMBER'):
        res = f"{x} := {a} - {b}\n"
    elif t_a == 'VECTOR' and t_b == 'VECTOR':
        res = f"{x}.SubVec({a},{b})\n"
    return res

def MulElem(x,a,b,Tr):
    res = "?"
    t_a = Tr[a]
    t_b = Tr[b]
    t_x = Tr[x]
    if (t_a == "SCALAR" or t_a == "NUMBER") and t_b == 'MATRIX':
        res = f"{x}.Scale({a},{b})\n"
    elif t_a == "MATRIX" and (t_a == 'SCALAR' or t_b == 'NUMBER'):
        res = f"{x}.MulElem({a},{b})\n"
    elif (t_a == 'SCALAR' or t_a == 'NUMBER') and (t_b == 'SCALAR' or t_b == 'NUMBER'):
        res = f"{x} := {a} * {b}\n"

    return res



def DivElem(x,a,b,Tr):
    res = "?"
    t_type = Tr[x]
    return f"{x}.DivElem({a},{b})\n"

def Exp(x,a,b,Tr):
    res = "?"
    t_type = Tr[x]
    return f"{x}.Exp({a})\n"

def Det(x,a,b,Tr):
    res = "?"
    t_type = Tr[x]

    return f"{x} := mat.Det({a})\n"
def Inv(x,a,b,Tr):
    res = "?"
    t_type = Tr[x]
    return f"{x}.Inverse({a})\n"

def T(x,a,b,Tr):
    res = "?"
    t_type = Tr[x]
    refs.append(x)
    return f"{x} := {a}.T()\n"
def Power(x,a,b,Tr):
    res = '?'
    t_a = Tr[a]
    t_b = Tr[b]
    t_x = Tr[x]
    if t_a == 'MATRIX':
        res = f"{x}.Power({a},{b})\n"
    elif t_a == 'SCALAR' or t_a == 'NUMBER':
        res = f"{x} := ({a})**({b})\n"

    return res
operations = {
    '@' : Mul,
    '+' : Add,
    '*' : MulElem,
    '**' : Power,
    '/' : DivElem,
    '-' : Sub,
    '^T' : T,
    '~' : Inv,
    'exp': Exp,
    'det': Det

}

refs = []
def translate(R,Tr):
    code = ''
    # print(Tr[3.0])

    for r in R:
        func = operations[r[3]]

        try:
            t_type = Tr[r[0]]
        except:
            t_type = "NONE"

        code += func(r[0],r[1],r[2],Tr)
    for x in refs:
        # code = code.replace(x,"&"+x)
        rx = re.compile(rf"({x})(?=,|\))")
        code = rx.sub(r"&\1",code)
    return code

def test_operations():
    R=[['X1','A','B','+'],
       ['X2','X1','C','@']]
    code = translate(R)
    # print(code)


if __name__ == "__main__":
    test_operations()
