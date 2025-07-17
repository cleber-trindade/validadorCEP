# Funcionalidade: Consulta de CEP

## Requisitos:
- O sistema deve aceitar um CEP como entrada
- Retornar endereço completo via API pública (ViaCEP)
- Tratar erros como CEP inválido ou inexistente

## Critérios de aceitação:
- CEP correto retorna status 200 e dados válidos
- CEP inválido retorna erro 400
- CEP inexistente retorna mensagem de "não encontrado"