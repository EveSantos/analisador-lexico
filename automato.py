caracteres = ['a','b']
transições =   [['1','1'],
                ['2','2'],
                ['1','1']]
  #     |  a  |   b
  # ----|-----|-------
  #   0 |  1  |   1
  # ----|-----|-------
  #   1 |  2  |   2
  # ----|-----|-------
  #   2 |  1  |  1
def automato(estado, palavra, cont):
  resultado=[]
  
  if((estado == 0)):
    prox_caracter = le_prox_caracter(palavra,cont)
    resultado.append(prox_caracter)
    estado = transições[estado][prox_caracter]
    resultado.append(estado)


  elif(estado == 1):
    prox_caracter = le_prox_caracter(palavra,cont)
    resultado.append(prox_caracter)
    estado = transições[estado][prox_caracter]
    resultado.append(estado)

  elif(estado == 2):
    prox_caracter = le_prox_caracter(palavra,cont)
    resultado.append(prox_caracter)
    estado = transições[estado][prox_caracter]
    resultado.append(estado)
  return resultado

def le_prox_caracter(palavra, cont):
  prox_caracter = palavra[cont]
  if(prox_caracter == caracteres[0]):
    prox_caracter = 0
  elif(prox_caracter == caracteres[1]):
    prox_caracter = 1
  else:
    print("Caracter ' "+ palavra[cont] + " ' não reconhecido")
    print("Fim da execução"  )
    exit()
  return prox_caracter

def main():
  input_plv = open('palavra.cic', 'r')
  palavra = input_plv.readlines()
  estado = 0
  cont = 0
  caracteres_plv=[]

  palavra = list(palavra[0])

  for n in palavra:
    result = automato(estado, palavra, cont)
    cont = cont + 1
    novo_estado = int(result[1])
    estado = novo_estado
    caracteres_plv.append(result[0])

  if(estado == 1):
    print("Palavra aceita!")
  else:
    print("Palavra rejeitada!")

main()