"""
Objetivo: Ensinar o conceito de aportes e rendimentos (renda fixa vs. ativos de risco) diretamente no terminal.

Conceitos: Lógica de programação, variáveis, estruturas de repetição, aleatoriedade e cálculos financeiros básicos.
"""

import random


def ler_float(mensagem):
    """Lê um float do usuário, validando entrada e valor positivo."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número (ex: 1000.50).")


def ler_int(mensagem):
    """Lê um inteiro do usuário, validando entrada e valor positivo."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro (ex: 12).")


def simular_renda_fixa(saldo_inicial, meses, taxa_mensal):
    """Renda fixa: crescimento previsível via juros compostos."""
    historico = [saldo_inicial]
    saldo = saldo_inicial
    for _ in range(meses):
        saldo *= (1 + taxa_mensal)
        historico.append(saldo)
    return historico


def simular_acoes(saldo_inicial, meses, retorno_medio, volatilidade):
    """
    Ações: cada mês tem um retorno aleatório (distribuição normal) em torno
    de uma média, para ilustrar que risco = variação, não apenas 'rende mais'.
    """
    historico = [saldo_inicial]
    saldo = saldo_inicial
    for _ in range(meses):
        retorno_mes = random.gauss(retorno_medio, volatilidade)
        saldo *= (1 + retorno_mes)
        saldo = max(saldo, 0)  # não deixa o saldo virar negativo
        historico.append(saldo)
    return historico


def simulador_investimentos():
    print("=" * 45)
    print("   SIMULADOR DE INVESTIMENTOS - B3 APRENDIZ   ")
    print("=" * 45)
    print("\nAviso: simulação educacional. Não considera IR, taxas")
    print("de custódia/corretagem, nem reflete o mercado real.")

    saldo_inicial = ler_float("\nInforme o valor do aporte inicial (R$): ")
    meses = ler_int("Informe o período de investimento (em meses): ")

    # Parâmetros simulados (ao mês)
    taxa_renda_fixa = 0.008      # 0.8% a.m., fixo e previsível
    retorno_medio_acoes = 0.010  # 1.0% a.m. em média
    volatilidade_acoes = 0.045   # ±4.5% a.m. de oscilação (o "risco")

    hist_rf = simular_renda_fixa(saldo_inicial, meses, taxa_renda_fixa)
    hist_acoes = simular_acoes(saldo_inicial, meses, retorno_medio_acoes, volatilidade_acoes)

    print("\n" + "-" * 45)
    print(f"Evolução mês a mês:")
    print(f"{'Mês':<6}{'Renda Fixa (R$)':<20}{'Ações (R$)':<20}")
    for m in range(meses + 1):
        print(f"{m:<6}{hist_rf[m]:<20.2f}{hist_acoes[m]:<20.2f}")

    print("-" * 45)
    print(f"Resultado final após {meses} meses:")
    print(f"• Renda Fixa (CDB/Tesouro): R$ {hist_rf[-1]:.2f}")
    print(f"• Mercado de Ações (simulado): R$ {hist_acoes[-1]:.2f}")
    print("-" * 45)

    ganho_rf = hist_rf[-1] - saldo_inicial
    ganho_acoes = hist_acoes[-1] - saldo_inicial
    print(f"\nGanho/perda Renda Fixa: R$ {ganho_rf:.2f}")
    print(f"Ganho/perda Ações: R$ {ganho_acoes:.2f}")

    if ganho_acoes < 0:
        print("\nNote: neste cenário, as ações tiveram perda — isso é")
        print("normal e esperado em ativos de risco. Rode o programa")
        print("de novo e veja como o resultado muda a cada simulação.")


if __name__ == "__main__":
    simulador_investimentos()