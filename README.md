# analisador-lexico

Esse projeto consiste na implementação de um analisador léxico para a materia de compiladores utilizando automatos de estados. 
Esse programa interpreta uma linguagem que foi criada previamente pela professora da disciplina.
Abaixo as regras para implementação do código.

O trabalho consiste na implementação de um analisador léxico para a linguagem de programação
fictícia cic_2023.1 (especificada na seção 3). O programa deve receber como entrada um arquivo
de texto com extensão .cic contendo o programa fonte escrito na linguagem cic_2023.1.
O analisador léxico deve:
  - Reconhecer as palavras reservadas, operadores e delimitadores e utilizar códigos únicos
  para cada um.
  - Criar e atualizar uma tabela de símbolos para os tokens que possuem lexemas.
  - Informar possíveis erros e onde ele se encontra
  - Ser implementado como uma sub-rotina (função ou método) que, a cada chamada:
    - Processa a entrada caractere por caractere
    - Identifica um único token na entrada
    - Retorna o código do token e, se for o caso, uma referência à sua entrada na tabela de símbolos. 

1. Especificação da linguagem cic_2023.1
1.1 Tipo de dados
  Há dois tipos de dados em cic_2023.1: número e cadeia.
  Um número consiste de ao menos um dígito (quando houver ponto, ao menos um dígito antes e
  um dígito depois do ponto), com sinal, ponto opcional e expoente opcionais. Quando expoente
  está presente, o número apenas pode ter 1 algarismo antes do .(ponto). Exemplos de tokens
  TK_NUMERO: -15, +001, +1234567890, -0.134e-7, +3.4564e+10
  Não são permitidos: 13 (falta sinal), -.45 (precisa ter 1 dígito antes do .), +2523.4e-10 (quando
  exponencia, apenas 1 dígito antes do ponto) ou +123. (quando houver ., ao menos um dígito
  depois do .)
  Uma cadeia é uma sequência de caracteres delimitada por aspas duplas e totalmente contida em
  uma única linha. Uma cadeia aberta em uma linha e fechada em outra deve gerar erro léxico.
  Exemplos de tokens tk_CADEIA: “-.15” , “cic 2023\n” e “”.
  No trecho de programa a seguir, +2 é uma constante do tipo número e “Media=” uma constante do
  tipo cadeia; seu analisador léxico deve reconhecê-los como tais.
    **media <- soma/+2**
    **escreva (“Media=”)**
    **escreva(media)**

1.2 Identificadores para nomes de variáveis
  Identificadores (nomes de variáveis) devem começar com uma letra e conter apenas letras, dígitos
  e sublinhado, devem ter no mínimo 2 caracteres. Letras acentuadas não são permitidas.
  Exemplos permitidos: v_1, vAr, Var, v_
  Exemplos não permitidos: _var, 3var, x, vár
  1.3 Identificadores para nomes de funções
  Identificadores (nomes de funções) devem começar e terminar com 2 sublinhados, conter pelo
  menos 1 letra e pode conter ou não dígitos. Não devem contem outro sublinhado. Exemplo:
    **def __funcao1__():**
    **return 10**
    **my_var= __funcao1()**

1.4. Comandos
  O comando imprima aceita variáveis ou constantes como argumentos; leia aceita apenas
  variáveis. Contudo, cada comando leia ou imprima aceita apenas um argumento. Assim, a
  impressão de texto e valores numéricos misturados deve ser feita com vários comandos imprima.
  Todos os comandos devem ser tratados como palavras reservadas. Sua sintaxe e semântica sãoirrelevantes para o analisador léxico; a descrição acima visa apenas ajudá-lo a compreender os
  arquivos de teste.
  Seguem os comandos da linguagem, em negrito, as palavras reservadas, operadores e
  delimitadores.

  **programa comandos fim_programa**
  **caso expressao entao comandos fim_caso**
  **caso expressao entao comandos senao comandos fim_caso**
  **leia(identificador)**
  **imprima(identificador)**
  **imprima(numero)**
  **imprima(cadeia)**
  **identificador <- expressao**
  **def identificador_funcao (identificadores|numeros|cadeias):**
   **comandos return identificador|numero|cadeia**

1.5. Maiúsculas, minúsculas e acentuação
  Nomes de identificadores: Letras maiúsculas e minúsculas são permitidas e distinguíveis: media,
  Media, MeDiA e MEDIA devem ser tratados como identificadores diferentes. Rejeite acentos no
  reconhecimento de identificadores: media deve ser aceito como identificador, mas média deve
  causar erro léxico e a mensagem de erro deve apontar o é como caractere inválido.
  Palavras reservadas: Maiúsculas e minúsculas são permitidas e indistinguíveis: caso, Caso,
  CaSo e CASO são formas válidas do mesmo comando, devendo ser reconhecidos como a
  mesma palavra reservada.
  
1.6 Operadores

Unários Binários

Aritméticos e lógicos |() - nao | +  -  *  /  e  ou
Relacionais                     | <> == >= <= > <
Atribuição                      | <-

1.7 Declaração de variáveis

  **numero : identificador**
  **numero : identificador, ..., identicador**
  **cadeia : identificador**
  **cadeia : identificador, ..., identicador**
  
1.8 Delimitadores, operadores e brancos
  Devem ser identificados por tokens próprios os delimitadores para dois pontos (:) e vírgula (,).
  Operadores também devem ser identificados por tokens próprios.
  Branco é um termo que se aplica tanto ao espaço (‘ ’) quanto ao tab (‘\t’), brancos não geram
  token. O branco na cadeia ‘x1 x2’ deve causar o reconhecimento de dois identificadores, x1 e x2;
  um delimitador (,) no lugar do branco teria o mesmo efeito.
  Uma sequência de espaços e tabs, em qualquer combinação, é equivalente a um único branco.

1.9 Comentários
  Existem dois tipos de comentários: de linha e de bloco. Comentários de linha são iniciados pelos
  caracteres // e terminam no final da linha, por exemplo:
  numero: x, y, z // Tres valores a serem ordenados
  cadeia: maior, menor // O maior e o menor dos tres
  Comentários de bloco são demarcados pelas sequências /* e */, por exemplo:

    ** /* Este programa le tres numeros * **
    ** * e os coloca em ordem crescente */ **
    ** numero: x, y, z, maior, menor **

  Comentários devem ser ignorados pelo analisador léxico. Ao encontrar o início de comentário de
  bloco, o analisador deve consumir e descartar caracteres da entrada até encontrar o final do
  comentário ou o final do arquivo, o que ocorrer primeiro. Um comentário de bloco aberto e não
  fechado deve gerar erro léxico do tipo: “Comentário não fechado”; a seguir, a análise deve ser
  retomada a partir da linha seguinte àquela onde o comentário foi aberto, efetivamente
  transformando o comentário de bloco em comentário de linha.
