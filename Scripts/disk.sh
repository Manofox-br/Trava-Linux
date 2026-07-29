#!/bin/bash

# Script de teste de I/O com dd
echo "Criando arquivo de 1GB para teste..."
dd if=/dev/zero of=teste_io.txt bs=1M count=1024

echo "Lendo arquivo para simular carga..."
dd if=teste_io.txt of=/dev/null bs=1M

echo "Teste concluído."