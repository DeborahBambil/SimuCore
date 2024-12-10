# Definir processadores com suas frequências (em GHz)
processadores = {
    'Intel Core i5': 3.0,  # 3.0 GHz
    'AMD Ryzen 5': 3.6,    # 3.6 GHz
    'Intel Xeon': 2.5,     # 2.5 GHz
    'ARM Cortex-A53': 1.4  # 1.4 GHz
}

# Função para calcular o tempo de execução
def calcular_tempo(num_instrucoes, frequencia_ghz):
    # Converter frequência de GHz para Hz
    frequencia_hz = frequencia_ghz * 1e9
    # Calcular tempo de execução em segundos
    tempo = num_instrucoes / frequencia_hz
    return tempo

# Função principal
def main():
    while True:  # Loop para evitar que o programa feche após erro
        try:
            # Obter número de instruções
            num_instrucoes = int(input("Digite o número de instruções: "))

            print("\nTipos de processadores disponíveis:")
            for i, (nome, freq) in enumerate(processadores.items(), 1):
                print(f"{i}. {nome} - {freq} GHz")

            # Obter escolha do processador
            escolha = int(input("\nEscolha o tipo de processador (número): "))

            # Verificar se a escolha está dentro do intervalo
            if 1 <= escolha <= len(processadores):
                # Obter o nome e a frequência do processador selecionado
                processador_selecionado = list(processadores.keys())[escolha - 1]
                frequencia_selecionada = processadores[processador_selecionado]

                # Calcular o tempo
                tempo_execucao = calcular_tempo(num_instrucoes, frequencia_selecionada)

                print(f"\nProcessador selecionado: {processador_selecionado}")
                print(f"Tempo de execução: {tempo_execucao:.10f} segundos")

                # Perguntar ao usuário se deseja continuar
                continuar = input("\nDeseja realizar outro cálculo? (s/n): ").lower()
                if continuar != 's':
                    break  # Sai do loop se o usuário não quiser continuar
            else:
                print("Escolha inválida! Por favor, selecione um número válido.\n")
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar números inteiros válidos.\n")

if __name__ == "__main__":
    main()
