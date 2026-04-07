import met
import sys

if len(sys.argv) > 1:
    expr = sys.argv[1]
else:
    expr = "(Y^T @ X) @ (~(X^T @ X))"

met.mylex.input(expr)
while True:
    tok = met.mylex.token()
    if not tok: break

    met.T[str(tok.value)] = tok.type
    if tok.type in met.U:
        met.U[tok.type].append(tok.value)
    else:
        met.U[tok.type] = [tok.value]
# print(met.T)

met.parser.parse(expr)

code = met.translate(met.R,met.T)

print(code)