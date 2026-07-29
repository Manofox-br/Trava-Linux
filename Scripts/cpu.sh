#!/bin/bash

# ==============================================================================
# SCRIPT DE ESTRESSE DE CPU UNIFICADO E INTEGRADO (SEM DEPENDÊNCIAS EXTERNAS)
# ==============================================================================

# Identifica automaticamente o número de núcleos da CPU
NUCLEOS=$(nproc)

echo "=================================================="
echo "   INICIANDO SIMULAÇÃO NATIVA DE CARGA MÁXIMA     "
echo "================================================--"
echo "[*] Detectados $NUCLEOS núcleos de CPU."
echo "[*] O sistema operará em capacidade máxima de processamento."
echo "[!] Para encerrar o teste a qualquer momento, pressione CTRL+C."
echo "=================================================="

# Array para armazenar os identificadores dos processos de carga
PIDS=()

# Inicializa um processo de carga contínua para cada núcleo detectado
for i in $(seq 1 $NUCLEOS); do
    # O comando dd transfere dados infinitos gerando processamento contínuo
    dd if=/dev/zero of=/dev/null &> /dev/null &
    PIDS+=($!)
done

echo "[+] Carga aplicada com sucesso em todos os núcleos."
echo "[*] Monitorando a execução... (Aguardando interrupção)"

# Função de captura (trap) para encerrar os processos criados se o usuário apertar CTRL+C
trap 'echo -e "\n[*] Interrupção detectada. Encerrando processos de teste..."; kill ${PIDS[@]} 2>/dev/null; echo "[+] Sistema liberado."; exit 0' INT

# Mantém o script em execução monitorando os processos em segundo plano
wait ${PIDS[@]}
