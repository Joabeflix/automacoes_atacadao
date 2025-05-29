import asyncio
import telnetlib3

# Tempo de espera entre etapas (em segundos)
delay = 5

# Dicionário com códigos das teclas
TELAS_KEYS = {
    'DOWN': '\x1b[B',    # seta para baixo
    'UP': '\x1b[A',      # seta para cima
    'RIGHT': '\x1b[C',   # seta para direita
    'LEFT': '\x1b[D',    # seta para esquerda
    'TAB': '\t',         # tecla TAB
    'ENTER': '\r\n'      # tecla ENTER
}


async def esperar_prompt(reader, echo=False):
    response = await reader.read(1024)
    if echo:
        print(response)
    return response


async def enviar_tecla(writer, tecla):
    writer.write(TELAS_KEYS[tecla])
    await asyncio.sleep(delay)


async def enviar_texto(writer, texto):
    writer.write(texto + TELAS_KEYS['ENTER'])
    await asyncio.sleep(delay)


async def processar_produtos(reader, writer, produtos: dict):
    for ean, endereco in produtos.items():
        # await esperar_prompt(reader, echo=True)
        
        # Enviar EAN e confirmar
        await enviar_texto(writer, ean)

        # Confirmar troca com 's' + ENTER
        await enviar_texto(writer, 's')

        # Esperar campo de endereço
        await esperar_prompt(reader, echo=True)

        # Enviar endereço
        await enviar_texto(writer, endereco)

        # Aguardar antes do próximo item
        await esperar_prompt(reader, echo=True)

        await asyncio.sleep(delay)
    print("Todos os produtos processados.")


async def main(produtos: dict):
    reader, writer = await telnetlib3.open_connection(
        host='atacadao185010.protheus.cloudtotvs.com.br',
        port=10555
    )

    print("Conectado ao servidor!")

    # Navegação inicial até tela de endereçamento
    await esperar_prompt(reader, echo=True)
    await enviar_tecla(writer, 'ENTER')

    await esperar_prompt(reader, echo=True)
    await enviar_tecla(writer, 'ENTER')

    await esperar_prompt(reader, echo=True)
    await enviar_texto(writer, 'col1')  # Usuário

    await esperar_prompt(reader, echo=True)
    await enviar_texto(writer, '1')     # Senha

    await esperar_prompt(reader, echo=True)
    await enviar_tecla(writer, 'ENTER')

    await esperar_prompt(reader, echo=True)
    await enviar_tecla(writer, 'ENTER')

    await esperar_prompt(reader, echo=True)
    await enviar_tecla(writer, 'ENTER')

    for _ in range(3):
        await esperar_prompt(reader, echo=True)
        await enviar_tecla(writer, 'DOWN')

    await esperar_prompt(reader, echo=True)
    await enviar_tecla(writer, 'ENTER')

    await esperar_prompt(reader, echo=True)


    # Começa a processar produtos
    await processar_produtos(reader, writer, produtos)

    writer.close()
    print("Conexão encerrada.")


# Exemplo de uso (você pode importar isso e chamar com seu dicionário):
if __name__ == '__main__':
    produtos_ean_endereco = {
        '7897707511044': '002-24-E'
    }

    asyncio.run(main(produtos_ean_endereco))
