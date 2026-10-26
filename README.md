# Controle de Estufa de Temperaturas

## Descrição do Problema
Sistema para monitorar a temperatura em uma estufa de mudas. O sistema recebe leituras de sensores e determina se é necessário ativar o aquecedor ou o ventilador de resfriamento.

## Requisitos
- Receber uma lista de leituras de temperatura (em graus Celsius).
- Se a temperatura média for maior que 30°C, ativar o ventilador.
- Se a temperatura mínima for menor que 15°C, ativar o aquecedor.
- Caso contrário, manter o sistema em modo automático.

## Exemplo de Uso
Entrada: [25, 28, 32, 14, 22]
Saída: Modo de operação: AQUECER