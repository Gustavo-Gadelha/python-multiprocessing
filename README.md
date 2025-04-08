# Simulação de Entregas com Múltiplos Motoboys

## Contexto

Este projeto simula um sistema de entregas onde múltiplos motoboys trabalham de forma concorrente, retirando pedidos de
uma fila compartilhada e realizando entregas simultaneamente

## Requisitos Técnicos

- Criar **3 processos**, cada um representando um motoboy
- Utilizar uma **fila de pedidos compartilhada** com **15 pedidos**
- Cada motoboy deve:
    - Pegar um pedido da fila
    - Simular a entrega com `sleep()`
    - Exibir os status:
        - 'Retirando pedido'
        - 'Saindo para entrega'
        - 'Pedido entregue'
- Utilizar **semáforo ou lock** para controlar o acesso à fila
- Ao final da simulação, exibir:
    - Total de pedidos entregues por cada motoboy
    - Tempo médio por entrega

