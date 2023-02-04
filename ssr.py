# Entendendo server rendering
# Carregar dados
dados = [
    {"nome": "Wallace", "cidade": "Caieiras"},
    {"nome": "Moyses", "cidade": "São Paulo"},
    {"nome": "Matheus", "cidade": "São Paulo"}
]

# Processar
# fstring tem avaliação imediata
template = """\
<html>
    <header>
    </header>

    <body>
        <ul>
            <li>Nome: {dados[nome]}</li>
            <li>Cidade: {dados[cidade]}</li>
        </ul>

    </body>

</html>
"""

# Renderizar

for item in dados:
    print(template.format(dados=item))