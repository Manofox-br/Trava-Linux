#!/bin/bash

# Script de teste de I/O com dd
echo "Criando arquivo de 1GB para teste..."
dd if=/dev/zero of="id_$random".txt bs=1024M count=5120

echo "Lendo arquivo para simular carga..."
dd if=teste_io.txt of=/dev/null bs=1024M

echo "Teste concluído."