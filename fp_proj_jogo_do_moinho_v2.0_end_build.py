# Tiago Alexandre Pereira Antunes   99331

# -------------------------------------------------------------------------------
# TADs
# -------------------------------------------------------------------------------

# -------------------------------------
# TAD posicao
# representacao interna: tuplo com 2 elementos (c, l), sendo c a coluna 'a', 'b'
# ou 'c' e l a linha '1', '2' ou '3'.
# cria_posicao(c,l): str x str --> posicao
# cria_copia_posicao(p): posicao --> posicao
# obter_pos_c(p): posicao --> str
# obter_pos_l(p): posicao --> str
# eh_posicao(arg): universal --> booleano
# posicoes_iguais(p1, p2): posicao x posicao --> booleano
# posicao_para_str(p): posicao --> str
# -------------------------------------
name = input("Your name: ")
print(
    "Hello,",
    name,
    "\nWelcome to Jogo do Moinho\nTo start write moinho(<your peca>,<dificulty>)",
)


def cria_posicao(c, l):
    """
    str x str --> posicao
    devolve a posicao correspondente a coluna c e a linha l
    """
    if c in ("a", "b", "c") and l in ("1", "2", "3"):
        return (c, l)
    else:
        raise ValueError("cria_posicao: argumentos invalidos")


def cria_copia_posicao(p):
    """
    posicao --> posicao
    devolve uma copia da posicao inserida
    """
    c = p[0]
    l = p[1]
    return (c, l)


def obter_pos_c(p):
    """
    posicao --> str
    devolve a componente coluna c da posicao p
    """
    return p[0]


def obter_pos_l(p):
    """
    posicao --> str
    devolve a componente linha l da posicao p
    """
    return p[1]


def eh_posicao(arg):
    """
    universal --> booleano
    devolve True apenas caso o seu argumento seja um TAD posciao
    """
    return (
        isinstance(arg, tuple)
        and len(arg) == 2
        and arg[0] in ("a", "b", "c")
        and arg[1] in ("1", "2", "3")
    )


def posicoes_iguais(p1, p2):
    """
    posicao x posicao --> booleano
    devolve True apenas se p1 e p2 sao posicoes e sao iguais
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


def posicao_para_str(p):
    """
    posicao --> str
    devolve a cadeia de caracteres 'cl' que representa o seu argumento, sendo os
    valores c e l as componentes caluna e linha de p
    """
    return obter_pos_c(p) + obter_pos_l(p)


def obter_posicoes_adjacentes(p):
    """
    posicao --> tuplo de posicoes
    devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a
    ordem de leitura do tabuleiro
    """
    coluna = obter_pos_c(p)
    linha = obter_pos_l(p)
    if coluna in ("a", "c") and linha in ("1", "3"):
        return pos_adjacentes_canto(p)
    elif coluna == "b" and linha == "2":
        return (
            cria_posicao("a", "1"),
            cria_posicao("b", "1"),
            cria_posicao("c", "1"),
            cria_posicao("a", "2"),
            cria_posicao("c", "2"),
            cria_posicao("a", "3"),
            cria_posicao("b", "3"),
            cria_posicao("c", "3"),
        )
    else:
        return pos_adjacentes_lateral(p)


def pos_adjacentes_canto(p):
    """
    posicao --> tuplo de posicoes
    recebe um posicao no canto do tabuleiro e retorna um tuplo com as posicoes
    adjacentes
    """
    coluna = obter_pos_c(p)
    linha = obter_pos_l(p)
    if coluna == "a":
        if linha == "1":
            return (
                cria_posicao("b", "1"),
                cria_posicao("a", "2"),
                cria_posicao("b", "2"),
            )
        else:
            return (
                cria_posicao("a", "2"),
                cria_posicao("b", "2"),
                cria_posicao("b", "3"),
            )
    elif coluna == "c":
        if linha == "1":
            return (
                cria_posicao("b", "1"),
                cria_posicao("b", "2"),
                cria_posicao("c", "2"),
            )
        else:
            return (
                cria_posicao("b", "2"),
                cria_posicao("c", "2"),
                cria_posicao("b", "3"),
            )


def pos_adjacentes_lateral(p):
    """
    posicao --> tuplo de posicoes
    recebe um posicao na lateral do tabuleiro e retorna um tuplo com as
    posicoes adjacentes
    """
    coluna = obter_pos_c(p)
    linha = obter_pos_l(p)
    if linha == "1":
        return (cria_posicao("a", "1"), cria_posicao("c", "1"), cria_posicao("b", "2"))
    elif linha == "2":
        if coluna == "a":
            return (
                cria_posicao("a", "1"),
                cria_posicao("b", "2"),
                cria_posicao("a", "3"),
            )
        else:
            return (
                cria_posicao("c", "1"),
                cria_posicao("b", "2"),
                cria_posicao("c", "3"),
            )
    else:
        return (cria_posicao("b", "2"), cria_posicao("a", "3"), cria_posicao("c", "3"))


# -------------------------------------
# TAD peca
# representacao interna: tuplo de um elemento (('X',), ('O',) ou (' ',))
# cria_peca(s): str --> peca
# cria_copia_peca(j): peca --> peca
# eh_peca(arg): universal --> booleano
# pecas_iguais(j1, j2): peca x peca --> booleano
# peca_para_str(j): peca --> str
# peca_para_inteiro(j): peca --> inteiro
# -------------------------------------


def cria_peca(s):
    """
    str --> peca
    recebe uma cadeia de caracteres correspondente ao identificador de um dos
    jogadores ('X', 'O') ou a uma peca livre (' ') e devolve a peca
    correspondente
    """
    if s in ("X", "O", " "):
        return (s,)
    else:
        raise ValueError("cria_peca: argumento invalido")


def cria_copia_peca(j):
    """
    peca --> peca
    recebe uma peca e devolve uma copia da peca
    """
    return cria_peca(j[0])


def eh_peca(arg):
    """
    universal --> booleano
    apenas devolve True caso o seu argumento seja um TAD peca
    """
    return isinstance(arg, tuple) and len(arg) == 1 and arg[0] in ("X", "O", " ")


def pecas_iguais(j1, j2):
    """
    peca x peca --> booleano
    devolve True apenas se j1 e j2 sao pecas e sao iguais
    """
    return eh_peca(j1) and eh_peca(j2) and j1 == j2


def peca_para_str(j):
    """
    peca --> str
    devolve a cadeia de caracteres que representa o jogador da peca
    """
    return "[" + str(j[0]) + "]"


def peca_para_inteiro(j):
    """
    peca --> inteiro
    devolve o inteiro 1, -1 ou 0 dependendo se a peca e do jogador 'X', 'O' ou
    livre, respetivamente
    """
    if peca_para_str(j) == "[X]":
        return 1
    elif peca_para_str(j) == "[O]":
        return -1
    else:
        return 0


# ------------------------------------
# TAD tabuleiro
# representacao interna: dicionario com 9 chaves, cada chave corresponde a
# representacao externa duma posicao e o que lhe esta associado e a peca
# na forma da sua representacao interna
# cria_tabuleiro(): {} --> tabuleiro
# cria_copia_tabuleiro(t): tabuleiro --> tabuleiro
# obter_peca(t, p): tabuleiro x posicao --> peca
# obter_vetor(t, s): tabuleiro x str --> tuplo de pecas
# coloca_peca(t,j,p): tabuleiro x peca x posicao --> tabuleiro
# remove_peca(t, p): tabuleiro x posicao --> tabuleiro
# move_peca(t, p1, p2): tabuleiro x posicao x posicao --> tabuleiro
# eh_tabuleiro(arg): universal --> booleano
# eh_posicao_livre(t, p): tabuleiro x posicao --> booleano
# tabuleiros_iguais(t1, t2): tabuleiro x tabuleiro --> booleano
# tabuleiro_para_str(t): tabuleiro --> str
# tuplo_para_tabuleiro(t): tuplo --> tabuleiro
# ------------------------------------


def cria_tabuleiro():
    """
    {} --> tabuleiro
    devolve um tabuleiro de jogo do moinho 3x3 sem posicoes ocupadas por pecas
    de jogador
    """
    vazio = cria_peca(" ")
    return {
        "a1": vazio,
        "b1": vazio,
        "c1": vazio,
        "a2": vazio,
        "b2": vazio,
        "c2": vazio,
        "a3": vazio,
        "b3": vazio,
        "c3": vazio,
    }


def cria_copia_tabuleiro(t):
    """
    tabuleiro --> tabuleiro
    recebe um tabuleiro e devolve uma copia nova do tabuleiro
    """
    return {
        "a1": t["a1"],
        "b1": t["b1"],
        "c1": t["c1"],
        "a2": t["a2"],
        "b2": t["b2"],
        "c2": t["c2"],
        "a3": t["a3"],
        "b3": t["b3"],
        "c3": t["c3"],
    }


def obter_peca(t, p):
    """
    tabuleiro x posicao --> peca
    devolve a peca na posicao p do tabuleiro, caso a posicao esteja livre
    devolve uma peca livre
    """
    return t[posicao_para_str(p)]


def obter_vetor(t, s):
    """
    tabuleiro x str --> tuplo de pecas
    devolve todas as pecas da linha ou coluna especificada pelo argumento
    """
    res = ()
    if s in ("a", "b", "c"):
        for l in ("1", "2", "3"):
            res = res + (t[posicao_para_str(cria_posicao(s, l))],)

    elif s in ("1", "2", "3"):
        for c in ("a", "b", "c"):
            res = res + (t[posicao_para_str(cria_posicao(c, s))],)

    return res


def coloca_peca(t, j, p):
    """
    tabuleiro x peca x posicao --> tabuleiro
    modifica destrutivamente o tabuleiro t colocando a peca j na posicao p e
    devolve o tabuleiro
    """
    t[posicao_para_str(p)] = j
    return t


def remove_peca(t, p):
    """
    tabuleiro x posicao --> tabuleiro
    modifica destrutivamente o tabuleiro t removendo a peca da posicao p e
    devolve o tabuleiro
    """
    t[posicao_para_str(p)] = cria_peca(" ")
    return t


def move_peca(t, p1, p2):
    """
    tabuleiro x posicao x posicao --> tabuleiro
    modifica destrutivamente o tabuleiro t movendo a peca que se encontra na
    posicao p1 para a posicao p2, e devolve o proprio tabuleiro
    """
    j = obter_peca(t, p1)
    remove_peca(t, p1)
    coloca_peca(t, j, p2)
    return t


def eh_tabuleiro(arg):
    """
    universal --> booleano
    devolve True apenas caso o seu argumento seja um TAD tabuleiro
    """
    if isinstance(arg, dict) and len(arg) == 9:
        num_pecas_x = 0
        num_pecas_o = 0
        for pos in ("a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"):
            if (pos not in arg) or (not eh_peca(arg[pos])):
                return False
            peca = obter_peca(arg, cria_posicao(pos[0], pos[1]))
            if peca_para_str(peca) == "[X]":
                num_pecas_x = num_pecas_x + 1
            elif peca_para_str(peca) == "[O]":
                num_pecas_o = num_pecas_o + 1

        if (abs(num_pecas_x - num_pecas_o) > 1) or (num_pecas_x > 3 or num_pecas_o > 3):
            return False

        num_ganhadores = 0
        for c in ("a", "b", "c"):
            t = obter_vetor(arg, c)
            if (
                pecas_iguais(t[0], t[1])
                and pecas_iguais(t[0], t[2])
                and not pecas_iguais(t[0], cria_peca(" "))
            ):
                num_ganhadores = num_ganhadores + 1
        for l in ("1", "2", "3"):
            t = obter_vetor(arg, l)
            if (
                pecas_iguais(t[0], t[1])
                and pecas_iguais(t[0], t[2])
                and not pecas_iguais(t[0], cria_peca(" "))
            ):
                num_ganhadores = num_ganhadores + 1
        if num_ganhadores > 1:
            return False
        return True
    else:
        return False


def eh_posicao_livre(t, p):
    """
    tabuleiro x posicao --> booleano
    devolve True apenas no caso da posicao p corresponder a uma posicao livre
    """
    return peca_para_str(t[posicao_para_str(p)]) == "[ ]"


def tabuleiros_iguais(t1, t2):
    """
    tabuleiro x tabuleiro --> booleano
    devolve True apenas se t1 e t2 sao tabuleiros e sao iguais
    """
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        for c in ("a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"):
            if not pecas_iguais(t1[c], t2[c]):
                return False
        return True
    return False


def tabuleiro_para_str(t):
    """
    tabuleiro --> str
    devolve a cadeia de caracteres que representa o tabuleiro
    """
    tab = ""
    l_jogo = 1
    tab = tab + "   a   b   c\n"
    for l in (1, 2, 3, 4, 5):
        if l in (1, 3, 5):
            linha_str = ""
            for c in ("a", "b", "c"):
                linha_str = linha_str + peca_para_str(
                    obter_peca(t, cria_posicao(c, str(l_jogo)))
                )
                if c != "c":
                    linha_str = linha_str + "-"

            tab = tab + str(l_jogo) + " " + linha_str
            if l != 5:
                tab = tab + "\n"
            l_jogo = l_jogo + 1

        elif l == 2:
            tab = tab + "   | \ | / |\n"

        elif l == 4:
            tab = tab + "   | / | \ |\n"

    return tab


def tuplo_para_tabuleiro(t):
    """
    tuplo --> tabuleiro
    devolve o tabuleiro que e representado pelo tuplo t
    """
    tab = {}
    for l in range(len(t)):
        col = 0  # representa o numero da coluna
        for c in ("a", "b", "c"):
            if t[l][col] == -1:
                peca = cria_peca("O")
            elif t[l][col] == 0:
                peca = cria_peca(" ")
            elif t[l][col] == 1:
                peca = cria_peca("X")
            tab[posicao_para_str(cria_posicao(c, str(l + 1)))] = peca
            col = col + 1
    return tab


def obter_ganhador(t):
    """
    tabuleiro --> peca
    devolve a peca do jogador que tenha as suas 3 pecas em linha na vertical ou
    na horizontal no tabuleiro. Caso nao exista um ganhador devolve a peca
    livre
    """
    for c in ("a", "b", "c", "1", "2", "3"):
        v = obter_vetor(t, c)
        if (
            pecas_iguais(v[0], v[1])
            and pecas_iguais(v[0], v[2])
            and peca_para_inteiro(v[0]) != 0
        ):
            return v[0]

    return cria_peca(" ")


def obter_posicoes_livres(t):
    """
    tabuleiro --> tuplo do posicoes
    devolve um tuplo com as posicoes das pecas livres
    """
    pos_livres = ()
    for l in ("1", "2", "3"):
        for c in ("a", "b", "c"):
            p = cria_posicao(c, l)
            if eh_posicao_livre(t, p):
                pos_livres = pos_livres + (p,)
    return pos_livres


def obter_posicoes_jogador(t, j):
    """
    tabuleiro x peca --> tuplo de posicoes
    devolve um tuplo com as posicoes das ocupadas pelas pecas j de um dos 2
    jogadores na ordem de leitura do tabuleiro
    """
    pos_jogador = ()
    for l in ("1", "2", "3"):
        for c in ("a", "b", "c"):
            p = cria_posicao(c, l)
            if pecas_iguais(obter_peca(t, p), j):
                pos_jogador = pos_jogador + (p,)
    return pos_jogador


# -------------------------------------------------------------------------------
# FUNCOES ADICIONAIS
# -------------------------------------------------------------------------------


def obter_movimento_manual(t, j):
    """
    tabuleiro x peca --> tuplo de posicoes
    recebe um tabuleiro e uma peca de um jogador e devolve um tuplo com uma ou
    2 posicoes que representam uma posicao ou um movimento introduzido
    manualmente pelo jogador
    """
    if cont_pecas(t):
        mov = input("Turno do jogador. Escolha um movimento: ")
        m = movimento_manual(t, j, mov)
        if m != ():
            return m
        else:
            raise ValueError("obter_movimento_manual: escolha invalida")

    else:
        pos = input("Turno do jogador. Escolha uma posicao: ")
        m = colocacao_manual(t, pos)
        if m != ():
            return m
        else:
            raise ValueError("obter_movimento_manual: escolha invalida")


def movimento_manual(t, j, m):
    """
    tabuleiro x peca x str --> tuplo de posicoes
    recebe um tabuleiro, a peca do jogador e uma cadeia de caracteres que
    corresponde a um movimento introduzido pelo jogador e devolve um tuplo
    com essas posicoes caso corresponda a um movimento valido
    """
    res = ()
    if len(m) == 4:
        if ver_entrada(m):
            pos_partida = cria_posicao(m[0], m[1])
            pos_chegada = cria_posicao(m[2], m[3])
            if pecas_iguais(obter_peca(t, pos_partida), j):
                if eh_posicao_adjacente(pos_partida, pos_chegada):
                    if eh_posicao_livre(t, pos_chegada):
                        return (pos_partida, pos_chegada)
                elif posicoes_iguais(pos_partida, pos_chegada):
                    if mov_impossivel(t, pos_partida):
                        return (pos_partida, pos_chegada)
    return res


def ver_entrada(m):
    """
    str --> booleano
    recebe uma cadeia de caracteres correspondente a um movimento introduzido
    pelo jogador e devolve True apenas se o que foi introduzido corresponde a
    um input valido
    """
    return (
        m[0] in ("a", "b", "c")
        and m[2] in ("a", "b", "c")
        and m[1] in ("1", "2", "3")
        and m[3] in ("1", "2", "3")
    )


def colocacao_manual(t, m):
    """
    tabuleiro x str --> tuplo de posicoes
    recebe um tabuleiro e uma cadeia de caracteres correspondente a uma posicao
    para colocar a peca introduzida pelo jogador na fase de colocacao e devolve
    um tuplo com essa posicao caso seja valida
    """
    res = ()
    if len(m) == 2:
        if m[0] in ("a", "b", "c") and m[1] in ("1", "2", "3"):
            pos = cria_posicao(m[0], m[1])
            if eh_posicao_livre(t, pos):
                return (pos,)
    return res


def eh_posicao_adjacente(p1, p2):
    """
    posicao x posicao --> booleano
    devolve True apenas se p2 for uma posicao adjacente a p1
    """
    for pos in obter_posicoes_adjacentes(p1):
        if posicoes_iguais(pos, p2):
            return True

    return False


def mov_impossivel(t, p):
    """
    tabuleiro x posicao --> booleano
    recebe um tabuleiro e uma posicao e retorna True apenas se a posicao nao
    tem posicoes adjacentes livres
    """
    for i in obter_posicoes_adjacentes(p):
        if eh_posicao_livre(t, i):
            return False
    else:
        return True


def cont_pecas(t):
    """
    tabuleiro --> booleano
    recebe um tabuleiro e devolve True caso esteja na fase de movimentacao e
    False caso esteja na fase de colocacao
    """
    num_x = 0
    num_o = 0
    for l in ("1", "2", "3"):
        for c in ("a", "b", "c"):
            p = cria_posicao(c, l)
            if peca_para_str(obter_peca(t, p)) == "[X]":
                num_x = num_x + 1
            elif peca_para_str(obter_peca(t, p)) == "[O]":
                num_o = num_o + 1
    if num_x == 3 and num_o == 3:
        return True
    return False


def obter_movimento_auto(t, j, d):
    """
    tabuleiro x peca x str --> tuplo de posicoes
    recebe um tabuleiro, uma peca de um jogador e uma string representando a
    dificuldade do jogo e retorna um tuplo com uma ou 2 posicoes que
    representam a posicao ou o movimento escolhido automaticamente
    """
    if cont_pecas(t):
        if d == "facil":
            return facil(t, j)

        elif d == "normal":
            v = minimax(t, j, 1, ())
            if v[0] == peca_para_inteiro(j):
                return v[1][0]
            else:
                return facil(t, j)

        elif d == "dificil":
            r, s = minimax(t, j, 5, ())
            return s[0]

    else:
        if vitoria(t, j) != ():
            return (vitoria(t, j)[0],)
        elif bloqueio(t, j) != ():
            return (bloqueio(t, j)[0],)
        elif centro(t) != ():
            return (centro(t)[0],)
        elif canto_vazio(t) != ():
            return (canto_vazio(t)[0],)
        elif lateral_vazio(t) != ():
            return (lateral_vazio(t)[0],)


def facil(t, j):
    """
    tabuleiro x peca --> tuplo de posicoes
    recebe um tuplo e uma peca de um jogador e devolve o tuplo com o movimento
    escolhido automaticamente de acordo com a dificuldade facil
    """
    bkup = ()
    for l in ("1", "2", "3"):
        for c in ("a", "b", "c"):
            pos = cria_posicao(c, l)
            if pecas_iguais(obter_peca(t, pos), j):
                bkup = bkup + (pos,)
                pos_adj = obter_posicoes_adjacentes(pos)
                for p in pos_adj:
                    if eh_posicao_livre(t, p):
                        return (pos, p)
    return (bkup[0], bkup[0])


def moinho(peca_jogador, d):
    """
    str x str --> str
    recebe a representacao externa da peca do jogador humano e o nivel de
    dificuldade do jogo e devolve a representacao externa da peca ganhadora
    """
    if peca_jogador in ("[X]", "[O]") and d in ("facil", "normal", "dificil"):
        print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + d + ".")
        t = cria_tabuleiro()
        print(tabuleiro_para_str(t))
        j = ext_para_int(peca_jogador)
        adv = outro_jogador(j)
        while pecas_iguais(obter_ganhador(t), cria_peca(" ")):
            if pecas_iguais(j, cria_peca("X")):
                mov_(t, j, d, obter_movimento_manual(t, j))
                if verif_ganhador(t) != "[ ]":
                    return verif_ganhador(t)
                print("Turno do computador (" + d + "):")
                mov_(t, adv, d, obter_movimento_auto(t, adv, d))
                if verif_ganhador(t) != "[ ]":
                    return verif_ganhador(t)
            elif pecas_iguais(j, cria_peca("O")):
                print("Turno do computador (" + d + "):")
                mov_(t, adv, d, obter_movimento_auto(t, adv, d))
                if verif_ganhador(t) != "[ ]":
                    return verif_ganhador(t)
                mov_(t, j, d, obter_movimento_manual(t, j))
                if verif_ganhador(t) != "[ ]":
                    return verif_ganhador(t)

    else:
        raise ValueError("moinho: argumentos invalidos")


def verif_ganhador(t):
    """
    tabuleiro --> str
    retorna a cadeia de caracteres que representa o jogador ganhador ou '[ ]'
    se nao existir ganhador
    """
    return peca_para_str(obter_ganhador(t))


def ext_para_int(j):
    """
    str --> peca
    retorna a peca que e representada pela cadeia de caracteres
    """
    if j == "[X]":
        return cria_peca("X")
    elif j == "[O]":
        return cria_peca("O")


def mov_(t, j, d, m):
    """
    funcao que coloca as pecas ou faz os movimentos dados por m e imprime o
    tabuleiro resultante
    """
    if not cont_pecas(t):
        coloca_peca(t, j, m[0])
    elif cont_pecas(t):
        move_peca(t, m[0], m[1])
    print(tabuleiro_para_str(t))


# -------------------------------------------------------------------------------
# Minimax
# -------------------------------------------------------------------------------


def minimax(t, j, d, s):
    """
    tabuleiro x peca x str x tuple --> lista
    recebe um tabuleiro, uma peca, uma string com a dificuldade do jogo e um
    tuplo com uma sequencia de movimentos e retorna uma lista cujo primeiro
    elemento representa o valor do tabuleiro e o segundo a sequencia de
    movimentos que mais beneficia o jogador
    """
    melhor_seq_movimentos = ()

    if not pecas_iguais(obter_ganhador(t), cria_peca(" ")) or d == 0:
        return lista_final(t, s)

    else:
        melhor_resultado = melhor_res(j)
        pecas_jog = obter_posicoes_jogador(t, j)
        for p in pecas_jog:
            pos_adj = obter_posicoes_adjacentes(p)
            for p_a in pos_adj:
                if eh_posicao_livre(t, p_a):
                    t1 = move_peca(cria_copia_tabuleiro(t), p, p_a)
                    novo_resultado, nova_seq_movimentos = minimax(
                        t1, outro_jogador(j), d - 1, s + ((p, p_a),)
                    )

                    if (
                        melhor_seq_movimentos == ()
                        or (
                            pecas_iguais(cria_peca("X"), j)
                            and novo_resultado > melhor_resultado
                        )
                        or (
                            pecas_iguais(cria_peca("O"), j)
                            and novo_resultado < melhor_resultado
                        )
                    ):
                        melhor_resultado = novo_resultado
                        melhor_seq_movimentos = nova_seq_movimentos
        return melhor_resultado, melhor_seq_movimentos


def lista_final(t, s):
    """
    tabuleiro x tuplo --> lista
    devolve uma lista em que o primeiro elemento e o valor do tabuleiro e o
    segundo e a sequencia de movimentos para chegar a esse resultado
    """
    if pecas_iguais(obter_ganhador(t), cria_peca("X")):
        return 1, s
    elif pecas_iguais(obter_ganhador(t), cria_peca("O")):
        return -1, s
    else:
        return 0, s


def melhor_res(j):
    """
    peca --> inteiro
    retorna o valor minimo do tabuleiro para a peca
    """
    if pecas_iguais(cria_peca("X"), j):
        melhor_resultado = -1
    elif pecas_iguais(cria_peca("O"), j):
        melhor_resultado = 1
    return melhor_resultado


def outro_jogador(j):
    """
    peca --> peca
    recebe uma peca e retorna a peca oposta
    """
    if pecas_iguais(cria_peca("X"), j):
        return cria_peca("O")
    else:
        return cria_peca("X")


# -------------------------------------------------------------------------------
# Estrategias fase de colocacao
# -------------------------------------------------------------------------------


def centro(t):
    """
    tabuleiro --> tuplo de posicoes
    recebe um tabuleiro e devolve um tuplo com a posicao central caso esteja
    livre
    """
    res = ()
    if eh_posicao_livre(t, cria_posicao("b", "2")):  # centro
        res = res + (cria_posicao("b", "2"),)
    return res


def canto_vazio(t):
    """
    tabuleiro --> tuplo de posicoes
    recebe um tabuleiro e devolve um tuplo com todas as posicoes dos cantos
    livres
    """
    res = ()
    for l in ("1", "3"):
        for c in ("a", "c"):
            if eh_posicao_livre(t, cria_posicao(c, l)):  # canto vazio
                res = res + (cria_posicao(c, l),)
    return res


def lateral_vazio(t):
    """
    tabuleiro --> tuplo de posicoes
    recebe um tabuleiro e devolve um tuplo com todas as posicoes laterais
    que nao sao cantos e estao livres
    """
    res = ()
    for l in ("1", "2", "3"):  # lateral vazio
        if l in ("1", "3"):
            if eh_posicao_livre(t, cria_posicao("b", l)):
                res = res + (cria_posicao("b", l),)
        else:
            for c in ("a", "c"):
                if eh_posicao_livre(t, cria_posicao(c, l)):
                    res = res + (cria_posicao(c, l),)

    return res


def vitoria(t, j):
    """
    tabuleiro x peca --> tuplo de posicoes
    recebe um tabuleiro e devolve um tuplo com todas as posicoes livres onde
    o jogador identificado pelo inteiro pode jogar de forma a ganhar o jogo
    """
    res = ()
    for l in ("1", "2", "3", "a", "b", "c"):
        p = [0, 1, 2]
        if l in ("1", "2", "3"):
            c = ("a", "b", "c")
        else:
            c = ("1", "2", "3")
        for i in range(len(p)):
            p = [0, 1, 2]
            if l in ("1", "2", "3"):
                res = vitoria_bloqueio_123(t, l, c, i, p, j, res, "vitoria")

            else:
                res = res + vitoria_bloqueio_abc(t, l, c, i, p, j, res, "vitoria")
    return res


def bloqueio(t, j):
    """
    tabuleiro x peca --> tuplo de posicoes
    recebe um tabuleiro e devolve um tuplo com as posicoes livres onde o jogador
    identificado pelo inteiro pode jogar para bloquear a vitoria do adversario
    """
    res = ()
    for l in ("1", "2", "3", "a", "b", "c"):
        p = [0, 1, 2]
        if l in ("1", "2", "3"):
            c = ("a", "b", "c")
        else:
            c = ("1", "2", "3")
        for i in range(len(p)):
            p = [0, 1, 2]
            if l in ("1", "2", "3"):
                res = vitoria_bloqueio_123(t, l, c, i, p, j, res, "bloqueio")
            else:
                res = res + vitoria_bloqueio_abc(t, l, c, i, p, j, res, "bloqueio")
    return res


def vitoria_bloqueio_123(t, l, c, i, p, j, res, fn):
    """
    tabuleiro x linha x coluna x inteiro x lista x peca x tuplo x str --> tuplo
    devolve um tuplo com as possiveis posicoes de vitoria caso o argumento fn
    seja 'vitoria' ou as posicoes de bloqueio caso fn seja 'bloqueio'
    """
    if eh_posicao_livre(t, cria_posicao(c[i], l)):
        possivel_pos = p[i]
        del p[i]
        if pecas_iguais(
            obter_peca(t, cria_posicao(c[p[0]], l)),
            obter_peca(t, cria_posicao(c[p[1]], l)),
        ):
            if (
                not pecas_iguais(obter_peca(t, cria_posicao(c[p[0]], l)), j)
                and peca_para_str(obter_peca(t, cria_posicao(c[p[0]], l))) != "[ ]"
                and fn == "bloqueio"
            ) or (
                pecas_iguais(obter_peca(t, cria_posicao(c[p[0]], l)), j)
                and fn == "vitoria"
            ):
                res = res + (cria_posicao(c[possivel_pos], l),)
    return res


def vitoria_bloqueio_abc(t, l, c, i, p, j, res, fn):
    """
    tabuleiro x coluna x linha x inteiro x lista x peca x tuplo x str --> tuplo
    devolve um tuplo com as possiveis posicoes de vitoria caso o argumento fn
    seja 'vitoria' ou as posicoes de bloqueio caso fn seja 'bloqueio'
    """
    if eh_posicao_livre(t, cria_posicao(l, c[i])):
        possivel_pos = p[i]
        del p[i]
        if pecas_iguais(
            obter_peca(t, cria_posicao(l, c[p[0]])),
            obter_peca(t, cria_posicao(l, c[p[1]])),
        ):
            if (
                not pecas_iguais(obter_peca(t, cria_posicao(l, c[p[1]])), j)
                and peca_para_str(obter_peca(t, cria_posicao(l, c[p[1]]))) != "[ ]"
                and fn == "bloqueio"
            ) or (
                pecas_iguais(obter_peca(t, cria_posicao(l, c[p[1]])), j)
                and fn == "vitoria"
            ):
                if cria_posicao(l, c[possivel_pos]) not in res:
                    res = res + (cria_posicao(l, c[possivel_pos]),)
    return res
