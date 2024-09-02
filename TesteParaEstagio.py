#   1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#   Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#   Imprimir(SOMA);
#   Ao final do processamento, qual será o valor da variável SOMA?

indice, soma, K = 13, 0, 0

while K < indice:
    K = K + 1
    soma = soma + K

print(soma)
#   Resposta: O valor da variável SOMA será 91

# -----------------------------------------------------------------------------------
#   2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
#   (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
#   ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def pertence_fibonacci(numero):
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False


num = int(input("Digite um número: "))

if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

# -----------------------------------------------------------------------------------
#   3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#   O menor valor de faturamento ocorrido em um dia do mês;
#   O maior valor de faturamento ocorrido em um dia do mês;
#   Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


def analise_faturamento(faturamento_diario):

    faturamento_diario = [valor for valor in faturamento_diario if valor > 0]

    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)

    dias_acima_media = sum(valor > media_mensal for valor in faturamento_diario)

    return menor_valor, maior_valor, dias_acima_media


faturamento = [1000, 1500, 0, 2000, 1200]
menor, maior, dias_acima_media = analise_faturamento(faturamento)

print("Menor valor de faturamento:", menor)
print("Maior valor de faturamento:", maior)
print("Número de dias com faturamento acima da média:", dias_acima_media)

# -----------------------------------------------------------------------------------
#   4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#   SP – R$67.836,43
#   RJ – R$36.678,66
#   MG – R$29.229,88
#   ES – R$27.165,48
#   Outros – R$19.849,53
#   Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.


def calcula_percentual_faturamento(faturamento_por_estado):
    faturamento_total = sum(faturamento_por_estado.values())

    percentuais = {
        estado: (valor / faturamento_total) * 100
        for estado, valor in faturamento_por_estado.items()
    }

    return percentuais


faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53,
}

percentuais_faturamento = calcula_percentual_faturamento(faturamento)

for estado, percentual in percentuais_faturamento.items():
    print(f"O estado {estado} representou {percentual:.2f}% do faturamento total.")

# -----------------------------------------------------------------------------------
#   5) Escreva um programa que inverta os caracteres de um string.
#   IMPORTANTE:
#   a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#   b) Evite usar funções prontas, como, por exemplo, reverse;


def inverter_string(string):

    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida


minha_string = "Quero iniciar minha carreira como programador!"
string_invertida = inverter_string(minha_string)
print(string_invertida)
