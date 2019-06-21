def readNumber(line, index):
  number = 0
  flag = 0
  keta = 1
  while index < len(line) and (line[index].isdigit() or line[index] == '.'):
    if line[index] == '.':
      flag = 1
    else:
      number = number * 10 + int(line[index])
      if flag == 1:
        keta *= 0.1
    index += 1
  token = {'type': 'NUMBER', 'number': float(number * keta)}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1


def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1


def readMultiply(line, index):
  token = {'type': 'MULTIPLY'}
  return token, index + 1


def readDivide(line, index):
  token = {'type': 'DIVIDE'}
  return token, index + 1


def readLeft(line, index):
  token = {'type': 'LEFT'}
  return token, index + 1


def readRight(line, index):
  token = {'type': 'RIGHT'}
  return token, index + 1


def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMultiply(line, index)
    elif line[index] == '/':
      (token, index) = readDivide(line, index)
    elif line[index] == '(':
      (token, index) = readLeft(line, index)
    elif line[index] == ')':
      (token, index) = readRight(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def evaluateTerm(tokens, index):
  (number, index) = evaluateFactor(tokens, index)
  result = number
  while index < len(tokens) and (tokens[index]['type'] == 'MULTIPLY' or tokens[index]['type'] == 'DIVIDE'):
    if tokens[index]['type'] == 'MULTIPLY':
      (number, index) = evaluateFactor(tokens, index + 1)
      result *= number
    else:
      (number, index) = evaluateFactor(tokens, index + 1)
      if number == 0:
        print('Error: Division by 0')
        exit(1)
      result /= number
  return (result, index)


def evaluateExpression(tokens, index):
  (number, index) = evaluateTerm(tokens, index)
  result = number
  while index < len(tokens) and (tokens[index]['type'] == 'PLUS' or tokens[index]['type'] == 'MINUS'):
    if tokens[index]['type'] == 'PLUS':
      (number, index) = evaluateTerm(tokens, index + 1)
      result += number
    else:
      (number, index) = evaluateTerm(tokens, index + 1)
      result -= number
  return (result, index)


def evaluateFactor(tokens, index):
  if tokens[index]['type'] == 'NUMBER':
    return (tokens[index]['number'], index + 1)
  if tokens[index]['type'] == 'LEFT':
    (number, index) = evaluateExpression(tokens, index + 1)
    if tokens[index]['type'] == 'RIGHT':
      return (number, index + 1)
    print('Parse error')
    exit()
  print('Parse error')
  exit(1)


def evaluate(tokens):
  (number, index) = evaluateExpression(tokens, 0)
  assert(index == len(tokens))
  return number


def test(line):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


def runTest():
    print("==== Test started! ====")
    test("1") #数字のみ
    test("11") #数字のみ(2桁)
    test("2+3") #通常の足し算
    test("2-3") #通常の引き算
    test("2*3") #通常の掛け算
    test("2/3") #通常の割り算
    test("2+3+4") #3項
    test("2-3-4") #3項
    test("2*3+4") #掛け算と足し算
    test("2+3*4") 
    test("2/3+4") #割り算と足し算
    test("2+3/4")
    test("2*3-4*5-6/7+8/9") #四則混合計算
    test("11.1") #少数
    test("1.1+2.2") #少数の足し算
    test("1.1-2.2") #少数の引き算
    test("1.1*2.2") #少数の掛け算
    test("1.1/2.2") #少数の割り算
    test("1.1*2.2-3.3*4.4-5.5/6.6+7.7/8.8") #少数の四則混合計算
    test("(1+2)*3") #カッコを含む掛け算
    test("(1+2)/3") #カッコを含む割り算
    test("1*(2+3)")
    test("1/(2+3)")
    test("(1+2)*(3+4)") #カッコ同士の掛け算
    test("(1+2)/(3+4)") #カッコ同士の割り算
    test("1-(2-3)") #カッコのある加減
    test("1-(2-(3-4))")
    test("1-(2-(3-(4-5)))")
    test("1-(2-(3-(4-5)-6))")
    test("(1+2)*3-4/(5-(6-7*8+9/(10-11)*12))")
    test("(1.1+2.2)*3.3-4.4/(5.5-(6.5-7.7*8.8+9.9/(10.0-11.1)*12.2))")
    test("2/0") #0の割り算 
    test("2*0") #0の掛け算
    print("==== Test finished! ====\n")

runTest()

while True:
    print('>')
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)