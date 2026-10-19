#      comando pip para importar algumas ferramentas da biblioteca COLORAMA
#      comando pip para importar a biblioteca tempo


import time
from colorama import Fore, Style, init

# Inicializa o colorama (necessario para o correto funcionamento no Windows)
init()

# 1. Lista para armazenar as situacoes do reservatorio (indice + 1 corresponde ao Nível)
SITUACOES = [
    "Muito baixo (critico)", # Nivel 1
    "Baixo",                 # Nivel 2
    "Medio",                 # Nivel 3
    "Alto",                  # Nivel 4
    "Muito alto (alerta)"    # Nivel 5
]

# 2. Funcao responsavel por retornar a cor e a mensagem conforme o nivel
def monitorar_reservatorio(nivel):
    """
    Define a cor e a mensagem com base no nivel informado (1 a 5).
    Retorna a mensagem formatada com a cor correspondente.
    """
    # Validacao para garantir que o nivel esta no intervalo correto
    if nivel < 1 or nivel > 5:
        return f"{Fore.WHITE}Nivel {nivel}: Invalido ou fora de escala.{Style.RESET_ALL}"
    
    # Busca a mensagem na lista (ajustando o indice que comeca em 0)
    mensagem = SITUACOES[nivel - 1]
    
    # Define a cor usando a estrutura de decisao
    if nivel == 1:
        cor = Fore.RED
    elif nivel == 2:
        cor = Fore.YELLOW
    elif nivel == 3:
        cor = Fore.GREEN
    elif nivel == 4:
        cor = Fore.CYAN
    elif nivel == 5:
        cor = Fore.BLUE
        
    # Retorna a string colorida e aplica o Style.RESET_ALL no final
    return f"{cor}Status do Reservatorio -> Nivel {nivel}: {mensagem}{Style.RESET_ALL}"

# 3. Simulacao do ambiente real de monitoramento
if __name__ == "__main__":

    print("====== INICIANDO SISTEMA DE MONITORAMENTO DE RESERVATORIO ===\n")
    
    # Simulando a variacao do nivel da agua ao longo do tempo (do Nivel 1 ao 5)
    for nivel_atual in range(1, 6):
        alerta = monitorar_reservatorio(nivel_atual)
        print(alerta)
        time.sleep(2) 
        
    # Pausa de 2 segundo entre as leituras para simular tempo real

        
    print("\n====== MONITORAMENTO ENCERRADO ===")