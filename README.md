# MatrixExpressionTranslator
Транслятор матричных выражений  в код библиотеки Gonum  для языка программирования Go
Пример использования

python3 prog.py "A\*\*3 + 3*A\*\*2"

Вывод программы:
x1.Power(A,3.0)

x2.Power(A,2.0)

x3.Scale(3.0,x2)

x4.Add(x1,x3)
