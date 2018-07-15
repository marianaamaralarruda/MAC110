# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Mariana Frasson Amaral Arruda
    NUSP: 10736802

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte: função crie_matriz feita em aula.

'''

#--------------------------------------------------------------------------        
def crie_matriz(nlin, ncol, valor):
    ''' (int, int, int) -> list

    Recebe dois inteiros nlin e ncol e um valor. 
    Cria e retorna uma matriz de dimensão nlin x ncol com valor em cada 
    posição.

    Exemplos:
    >>> t = crie_matriz(3,4,-1)
    >>> t
    [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
    >>> tt = crie_matriz(3,3,0)
    >>> tt
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> 
    '''
    matrix = []
    for i in range(nlin):
        line = ncol*[valor]
        matrix += [line]
    return matrix

#--------------------------------------------------------------------------        
def copie_matriz(dest, orig):
    ''' (list) -> list

    Recebe duas matriz de mesma dimensão e copia o conteúdo de orig para dest.

    Exemplo:

    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = [[11, 22, 33],[44, 55, 66]]
    >>> copie_matriz(tt, t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 777
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[777, -122, 3], [1, 2, 3]]
    '''
    for value in range(len(orig)):
        for num in range(len(orig[value])):
            dest[value][num] = orig[value][num]

#--------------------------------------------------------------------------        
def clone_matriz(matriz):
    ''' (list) -> list

    Recebe uma matriz e retorna uma cópia/clone da matriz

    Exemplo:
    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = clone_matriz(t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 111111
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[111111, -122, 3], [1, 2, 3]]
    >>> 
    '''
    nlin = len(matriz)
    ncol = len(matriz[0])
    dest = crie_matriz(nlin,ncol,0)
    for value in range(nlin):
        for num in range(ncol):
            dest[value][num] = matriz[value][num]

    
#--------------------------------------------------------------------------        
def max_simbolos(matriz):
    ''' (list) -> int

    Recebe uma matriz de inteiros e retorna o maior número de símbolos,
    dígitos e sinal negativo, usado para representar um número da matriz.

    Exemplos:
    >>> max_simbolos([[1, 2], [3, 4]])
    1
    >>> max_simbolos([[1, -2], [3, 4]])
    2
    >>> max_simbolos([[111, 222], [-33333, 4], [1, 2]])
    6
    '''
    nlin = len(matriz)
    ncol = len(matriz[0])
    len1 = len(str(matriz[0][0]))
    for i in range(nlin):
        for j in range(ncol):
            len2 = len(str(matriz[i][j]))
            if len1 < len2:
                len1 = len2
    return int(len1)

#--------------------------------------------------------------------------
def to_string(matriz):
    '''(list) -> str

    Recebe  uma matriz  de  inteiros e  cria e  retorna  uma string  que
    representa  a matriz  em  um formato  preparado  para impressão  com
    print().

    Esse formato deve ser o mais compacto possível e compátivel:
 
       na string, o comprimento das posições ocupadas por _cada
       elemento_ da matriz deve ser igual a __maior quantidade de
       símbolos__ na representação de um número da matriz.

    Esse __maior quantidade de símbolos__  deve levar em consideração os
    dígitos  na  representação  de  cada  número.  No  caso  de  números
    negativos o sinal também deve ser levado em consideração.

    As molduras compostas pelos caracteres "+", "|" e "-" __devem__ fazer 
    parte da string retornada; como mostram os exemplos a seguir. 

    Nos exemplos preste atenção especial aos caracteres ' ' e '\n' entre
    os símbolos  da string. A  string retornada pela função  deve seguir
    exatemente a regra de formação das strings ilustradas nos exemplos.

    Esta função deve utilizar a função max_simbolos().

    Exemplos:
    >>> t = [[0], [0], [0], [5], [0], [0], [0]] # exemplo 1
    >>> to_string(t)
    '+---+\n| 0 |\n+---+\n| 0 |\n+---+\n| 0 |\n+---+\n| 5 |\n+---+\n| 0 |\n+---+\n| 0 |\n+---+\n| 0 |\n+---+\n'
    >>> print(to_string(t))
    +---+
    | 0 |
    +---+
    | 0 |
    +---+
    | 0 |
    +---+
    | 5 |
    +---+
    | 0 |
    +---+
    | 0 |
    +---+
    | 0 |
    +---+

    >>> tt = [[11, 2, -3]] # exemplo 2: uma linha e três colunas
    >>> to_string(tt)
    '+----+----+----+\n| 11 |  2 | -3 |\n+----+----+----+\n'
    >>> len(to_string(tt))
    51
    >>> print(to_string(tt))
    +----+----+----+
    | 11 |  2 | -3 |
    +----+----+----+
                
    >>> ttt = [[12, -122, 3],[1, 2, 3]] # exemplo 3
    >>> to_string(ttt)
    '+------+------+------+\n|   12 | -122 |    3 |\n+------+------+------+\n|    1 |    2 |    3 |\n+------+------+------+\n'
    >>> len(to_string(ttt))
    115
    >>> print(to_string(ttt))
    +------+------+------+
    |   12 | -122 |    3 |
    +------+------+------+
    |    1 |    2 |    3 |
    +------+------+------+

    >>> tttt = [[-123, 0, -1]] # exemplo 4
    >>> s = to_string(tttt)
    >>> len(s)
    69
    >>> print(s)
    +------+------+------+
    | -123 |    0 |   -1 |
    +------+------+------+

    >>> 
    '''
    s = ""
    nlin = len(matriz)
    ncol = len(matriz[0])
    len_pos = int(max_simbolos(matriz))
    traco = len_pos + 2
    s += len(matriz[0]) * ("+" + traco * "-") + "+"
    for i in range(nlin):
        s += "\n"
        for j in range(ncol):
            s += "|"
            n = int(len(str(matriz[i][j])))
            for k in range(len_pos-n):
                s += " "
            s += " %d " %(matriz[i][j])
        s += "|"
        s += "\n"
        s += len(matriz[0]) * ("+" + traco * "-")
        s += "+"
    return s

#--------------------------------------------------------------------------            
def pause():
    ''' (None) -> None 

    Para a execução do programa até que um ENTER seja teclado.
    '''
    input("Tecle ENTER para continuar.")
    
