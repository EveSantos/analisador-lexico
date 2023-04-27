import re

tabela = [ # dig  +   -   .     e  char  "  outro   _    <   >   =  ' '  (   )   :   ,   /   *   
            [-1 ,  1,  1, -1,  35,  35,  12  ,13   ,17, 23, 25, 27, -1, -1, -1, -1, -1, 28, -1], #estado 0
            [ 2,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 1
            [ 3,  -1, -1,  6,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 2
            [ 3,  -1, -1,  4,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 3
            [ 5,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 4
            [ 5,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 5
            [ 7,  -1, -1, -1,   8,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 6
            [7,  -1, -1, -1,   8,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 7
            [-1,   9,  9, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 8
            [10,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 9
            [10,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 10
            [ 7,  -1, -1, -1,   8,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 11
            [-1,  -1, -1, -1,  -1,  12,  13  ,12   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 12
            [-1,  -1, -1, -1,  -1,  -1,  12  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 13
            [15,  -1, -1, -1,  -1,  14,  -1  ,-1   ,16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 14
            [15,  -1, -1, -1,  -1,  14,  -1  ,-1   ,16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 15
            [14,  -1, -1, -1,  -1,  14,  -1  ,-1   ,16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 16
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,18, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 17
            [-1,  -1, -1, -1,  -1,  19,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 18
            [19,  -1, -1, -1,  -1,  20,  -1  ,-1   ,21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 19
            [19,  -1, -1, -1,  -1,  20,  -1  ,-1   ,21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 20
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 21
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1 ,-1, -1, -1, -1, -1, -1, -1, -1], #estado 22
            [-1,  -1, 24, -1,  -1,  -1,  -1  ,-1   ,-1, -1 ,24, 24, -1, -1, -1, -1, -1, -1, -1], #estado 23  
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1 ,-1, -1, -1, -1, -1, -1, -1, -1], #estado 24
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1  -1, 26, -1, -1, -1, -1, -1, -1, -1], #estado 25     
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1 ,-1, -1, -1, -1, -1, -1, -1, -1], #estado 26   
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, 26, -1, -1, -1, -1, -1, -1, -1], #estado 27   
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, 29, 31], #estado 28  
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,30   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 29   
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,30   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 30    
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,32   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 31  
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,32   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, 32, 33], #estado 32   
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,32   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, 34, 33], #estado 33    
            [-1,  -1, -1, -1,  -1,  -1,  -1  ,-1   ,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 34  
            [14,  -1, -1, -1,  -1,  14,  -1  ,-1   ,14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 35  
               
          ]

palavras_reservadas = [ "programa", "fim_programa", "caso", 
                        "entao", "fim_caso", "senao", "imprima",
                        "leia", "def", "return"]

delimitadores = [ "(", ")"]

operadores = [ "+", "-", "*", "/", ">", "<", ">=", "<=", "==", "<>", "<-", "e", "ou", "nao"]

cadeia = ["+", "-", "*", "/", ">", "<", ">=", "<=", "==", "<>", "<-"]

tabela_token = {
  "tk_numero": {},
  "tk_cadeia": {},
  "tk_iden_var": {},
  "tk_operador": {},
  "tk_iden_func": {},
  "tk_return" : {},
  "tk_def": {},
  "tk_caso": {},
  "tk_senao": {},
  "tk_fim_caso": {},
  "tk_entao": {},
  "tk_fim_programa": {},
  "tk_programa": {},
  "tk_imprima": {},
  "tk_leia": {},
  "tk_abre_parenteses": {},
  "tk_fecha_parenteses": {},
  "tk_virgula": {},
  "tk_dois_pontos": {},
  "tk_virgula": {}
}
# tabela_token["tk_cadeia"].append((nome,(l,c)))
erro = []
matriz_erro = [] 
arquivo_erro = open("erros.txt", "w") 
arquivo_token = open("tokens.txt", "w") 
comentario_nao_fechado = [True]

def verifica_menos_um(vet, n , estado_anterior, linha, coluna):
  if(n == 0):
    verifica_estado_final(estado_anterior, vet, erro, linha, coluna)
    return n
    # precisa voltar a linha 
  else:
    if (estado_anterior >= 30 and estado_anterior <= 34):
      return n
    elif(len(vet) > 1):
      verifica_estado_final(estado_anterior, vet[:-1], erro, linha, coluna)
      return n-1
    else:
      verifica_estado_final(estado_anterior, vet, erro, linha, n)
      return n

# se o estado for valido, vai armazer o vetor no item correspondente da chave
# se o estado for invalido, vai armazenar o vetor no item correspondente a erro
# verificar o que tem no vetor para saber se é alguma palavrva reservada, etc  
def verifica_estado_final(estado_final,vet, erro, linha, coluna): 
  if(len(vet) != 0):
    vet = "".join(vet)
  # veirificação do estado final de numero
  if( vet in palavras_reservadas):
    if not vet in tabela_token["tk_"+vet]:
      tabela_token["tk_"+vet][vet] = [(linha, coluna)]
    else:
      tabela_token["tk_"+vet][vet].append((linha, coluna))
  elif( vet == ':'):
    if not vet in tabela_token["tk_dois_pontos"]:
      tabela_token["tk_dois_pontos"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_dois_pontos"][vet].append((linha, coluna))
  elif( vet in operadores):
    if not vet in tabela_token["tk_operador"]:
      tabela_token["tk_operador"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_operador"][vet].append((linha, coluna))
  elif(vet == '('):
    if not vet in tabela_token["tk_abre_parenteses"]:
      tabela_token["tk_abre_parenteses"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_abre_parenteses"][vet].append((linha, coluna))
  elif(vet == ')'):
    if not vet in tabela_token["tk_fecha_parenteses"]:
      tabela_token["tk_fecha_parenteses"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_fecha_parenteses"][vet].append((linha, coluna))
  elif(vet == ','):
    if not vet in tabela_token["tk_virgula"]:
      tabela_token["tk_virgula"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_virgula"][vet].append((linha, coluna))
  elif(estado_final == 3 or estado_final == 2 or estado_final == 5 or estado_final == 7 or estado_final == 10 or estado_final == 11):
    if not vet in tabela_token["tk_numero"]:
      tabela_token["tk_numero"][vet] = [(linha, coluna)]
    else:
      tabela_token["tk_numero"][vet].append((linha, coluna))
  # verificação do estado final de cadeia
  elif(estado_final == 13):
    if not vet in tabela_token["tk_cadeia"]:
      tabela_token["tk_cadeia"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_cadeia"][vet].append((linha,coluna))

  # verificação do estado final de variavel
  elif(estado_final >= 14 and estado_final <= 16 or estado_final == 35):
    if(len(vet) <2 ):
      erro.append(vet)
      exibe_erro(linha, coluna)
    elif not vet in tabela_token["tk_iden_var"]:
      tabela_token["tk_iden_var"][vet] = [(linha, coluna)]
    else:
      tabela_token["tk_iden_var"][vet].append((linha, coluna))
  # verificação do estado final de função
  elif(estado_final == 22):
    if not vet in tabela_token["tk_iden_func"]:
      tabela_token["tk_iden_func"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_iden_func"][vet].append((linha, coluna))
  elif(estado_final == -1 and re.match(r'^[a-zA-Z]+$', vet)):
    if not vet in tabela_token["tk_iden_var"]:
      tabela_token["tk_iden_var"][vet]= [(linha, coluna)]
    else:
      tabela_token["tk_iden_var"][vet].append((linha, coluna))
  else:
    if(vet != ' ' and vet != '\n' and vet != "\t"):
      erro.append(vet)
      exibe_erro(linha, coluna)

def exibe_erro(linha, coluna):
  for i in range(len(matriz_erro)):
    if ( i == linha):
      arquivo_erro.write("  "+str(i+1)+ "   |" + matriz_erro[i] + "\n")
      arquivo_erro.write(" "*7 + '-'*(coluna) + "ˆ" + "\n")
      arquivo_erro.write("Erro léxico na linha " + str(linha+1) + " coluna " + str(coluna+1) + "\n")
    else:
      arquivo_erro.write("  "+str(i+1)+ "   |" + matriz_erro[i] + "\n")
  arquivo_erro.write("\n")
  arquivo_erro.write("--------------------------------------")
  arquivo_erro.write("\n")

def exibe_erro_comentario(linha, coluna):
  for i in range(len(matriz_erro)):
    if ( i == linha):
      arquivo_erro.write("  "+str(i+1)+ "   |" + matriz_erro[i] + "\n")
      arquivo_erro.write(" "*7 + '-'*(coluna-1) + "ˆ" + "\n")
      arquivo_erro.write("Comentario nao fechado "  + "\n")
    else:
      arquivo_erro.write("  "+str(i+1)+ "   |" + matriz_erro[i] + "\n")
  arquivo_erro.write("\n")
  arquivo_erro.write("--------------------------------------")
  arquivo_erro.write("\n")
# a partir do caracter define a posição da coluna que representa a leitura
# se o caracter por gerar caminhos diferentes, o estado sera usado na comparação

def proximo_caracter(caracter,estado):
  if( estado == 0 ):
    if(caracter == '/'):
      return 17
    elif(caracter == 'e'):
      return 4
  if(estado > 10 and estado < 14):
    if(caracter == '"' ):
      return 6
    elif( caracter == '\n'):
      return 12
    else:
      return 7
  elif(estado >= 14 and estado < 17):
    if(caracter == '_'):
      return 8
    elif( caracter == '\n'):
      return 15
    elif(re.match(r'^[a-zA-Z]+$', caracter)):
      return 5
    elif(caracter.isdigit()):
      return 0
    else:
      return 7
  elif(estado >= 17 and estado <= 22):
    if(caracter == '_'):
      return 8
    elif(re.match(r'^[a-zA-Z]+$', caracter)):
      return 5
    elif( caracter == '\n'):
      return 15
    elif (caracter.isdigit()):
      return 0
    else:
      return 7
  elif(estado > 27 and estado < 31):
    if(caracter == '*'):
      return 18
    elif(caracter == '/'):
      return 17
    elif( caracter == '\n'):
      return 15
    else:
      return 7
  elif(estado >= 31 and estado <= 34):
    if(caracter == '*'):
      return 18
    elif(caracter == '/'):
      return 17
    else:
      return 7
  elif(estado == 35):
    if(re.match(r'^[a-zA-Z]+$', caracter)):
       return 5
    elif(caracter.isdigit()):
      return 0
    elif(caracter == '_'):
      return 8
    else:
      return 7
  elif( caracter == '\n'):
    return 15
  elif( caracter == ' ' ):
    return 12
  elif(caracter == '_'):
    return 8
  elif(caracter == '"'):
    return 6
  elif(caracter.isdigit()):
    return 0
  elif(caracter == '/'):
    return 18
  elif(caracter == '+' ):
    return 1
  elif(caracter == '-'):
    return 2
  elif(caracter == '.'):
    return 3
  elif( caracter == '<'):
    return 9
  elif(caracter == '>'):
    return 10
  elif(caracter == '='):
    return 11
  elif (caracter == ':'):
    return 15
  elif (caracter == '('):
    return 13
  elif (caracter == ')'):
    return 13
  elif(caracter == 'e'):
    if( estado == 35 or estado >13 and estado < 17):
      return 5
    elif(estado == 7 or estado == 8):
      return 4
    elif( caracter == '\n'):
      return 15
    else:
      return 6
  elif (re.match(r'^[a-zA-Z]+$', caracter)):
    return 5
  else:
    return 8


def main():
  input_plv = open('palavra.cic', 'r')
  palavra = input_plv.readlines()
  estado = 0
  vet = []
  n = 0
  linha = 0
  global erro
  matriz_aux = palavra
  global comentario_nao_fechado
  global matriz_erro
  
  for i in range(len(matriz_aux)):
    matriz_erro.append(matriz_aux[i].strip())
    
  # primeiro for representa as linhas do arquivo
  # segundo fr representa as colunas do arquivo
  # ['+', '2', '.', '2', '2', '2', '3', '4', '\n'] linha 1
  # ['-', '5', '.', '0' ] linha 2

  while (linha <= (len(palavra)-1)):
    n = 0
    while ( n <= len(palavra[linha])-1):
      if(estado == 0):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
        coluna_aux = n
        comentario_nao_fechado = [True]
      elif(estado == 1):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 2):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 3):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 4):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 5):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 6):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb] 
        vet.append(palavra[linha][n])      
      elif(estado == 7):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 8):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 9):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 10):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 11):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 12):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb] 
        vet.append(palavra[linha][n])
      elif(estado == 13):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb] 
        vet.append(palavra[linha][n])
      elif(estado == 14):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 15):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 16):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 17):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 18):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 19):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 20):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 21):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 22):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 23):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 24):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 25):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 26):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 27):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif(estado == 28):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif (estado == 29):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif (estado == 30):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif (estado == 31):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif (estado == 32):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
        if(palavra[linha][n] == "\n" and comentario_nao_fechado[0] == True):
          comentario_nao_fechado.append(linha)
          comentario_nao_fechado.append(n-1)
          comentario_nao_fechado[0] = False
      elif (estado == 33):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif (estado == 34):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])
      elif (estado == 35):
        estado_aux = estado
        prox_simb = proximo_caracter(palavra[linha][n],estado)
        estado = tabela[estado][prox_simb]
        vet.append(palavra[linha][n])

      # else configura erro para -1 no estado
      if( estado == -1):
        n = verifica_menos_um(vet, n , estado_aux, linha, coluna_aux)
        estado = 0
        vet = []
      n += 1

    if(linha == (len(palavra)-1) and  (n-1) == (len(palavra[linha])-1) and estado == 32):
      linha = comentario_nao_fechado[1]
      estado = 0
      vet = []
      exibe_erro_comentario(linha, comentario_nao_fechado[2] )
    # else:
    linha += 1
  if(vet != []):
    verifica_estado_final(estado,vet,erro, linha-1, coluna_aux)

  arquivo_token.write("+"+ "-"*8+"+"+"-"*25 +"+"+ "-"*30 +"+"+"-"*40+"+" + "\n")
  arquivo_token.write("|"+" "*3 + "POS  "+"| TOKEN"+ " "*19+"| LEXEMA" + " "*23 + "|"+ " POS NA ENTRADA (linha, coluna)         |"+ "\n")
  linha_num = 1
  linha_colunas = []

  for chave, valor in tabela_token.items():
    if (valor is not None and len(valor) > 0):
      for chave2, valor2 in tabela_token[chave].items():
        for tupla in valor2:
          linha_colunas.append(tupla)
          chave2.strip("\n")
        arquivo_token.write("+"+ "-"*8+"+"+"-"*25 +"+"+ "-"*30 +"+"+"-"*40+"+" + "\n")
        if(linha_num > 9):
          arquivo_token.write("|"+" "*3+ str(linha_num)+" "*3 +"|"+" "*5+chave.ljust(20) + "|"+ " "*5 +chave2.ljust(18) +" "*7+ "|"+ " "*5+str(linha_colunas).ljust(18)+ "\n")
        else:
          arquivo_token.write("|"+" "*4+ str(linha_num)+" "*3 +"|"+" "*5+chave.ljust(20) + "|"+ " "*5 +chave2.ljust(18) +" "*7+ "|"+ " "*5+str(linha_colunas).ljust(18)+ "\n")

        linha_colunas = []
        linha_num += 1
  arquivo_token.write("+"+ "-"*8+"+"+"-"*25 +"+"+ "-"*30 +"+"+"-"*40+"+" + "\n")
  arquivo_token.write("\n\n\n")

  arquivo_token.write("+"+ "-"*27+"+"+"-"*10+"+"+"\n")
  arquivo_token.write("|"+" "*11 + "TOKENS" +" "*10+"|   USOS"+ " "*3+"|"+ "\n")
  arquivo_token.write("+"+ "-"*27+"+"+"-"*10+"+"+"\n")
  total = 0
  for chave in tabela_token:
    valor = tabela_token[chave]
    if valor is not None:
      coluna1 = chave.ljust(25)  
      coluna2 = str(len(valor)).ljust(8) 
      total = total + len(valor)
      arquivo_token.write("| {} | {} |\n".format(coluna1, coluna2)) 
      arquivo_token.write("+"+ "-"*27+"+"+"-"*10+"+\n")
  

  if(total > 9):
    arquivo_token.write("|"+" " + "TOTAL" +" "*21+"| "+str(total)+ " "*7+"|"+ "\n")
  else:
    arquivo_token.write("|"+" " + "TOTAL" +" "*21+"| "+str(total)+ " "*8+"|"+ "\n")
  arquivo_token.write("+"+ "-"*27+"+"+"-"*10+"+\n")
    


  arquivo_erro.write('\n\n')
  arquivo_erro.write("+"+ "-"*7 + "+"+ "-"*20 +"+")
  arquivo_erro.write('\n')
  arquivo_erro.write("|  POS  "+"|        ERROS       |")
  arquivo_erro.write('\n')
  arquivo_erro.write("+"+ "-"*7 + "+"+ "-"*20 +"+")
  arquivo_erro.write('\n')

  linha_num = 1
  for i in range(len(erro)):
    if erro[i] not in ['\n', ' ']:
      arquivo_erro.write("|  "+str(linha_num)+"    |         " +"{:<10} |".format(erro[i]))
      arquivo_erro.write('\n')
      if(linha_num > 9):
        arquivo_erro.write("+"+ "-"*6 + "+"+ "-"*20 +"+")
      else:
        arquivo_erro.write("+"+ "-"*7 + "+"+ "-"*20 +"+")
      arquivo_erro.write('\n')  
    linha_num += 1 
  return
  
main()