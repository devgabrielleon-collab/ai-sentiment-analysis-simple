# Ideia do Projeto: IA de Classificação de Sentimentos para Feedback de Clientes

## Resumo
Este projeto consiste numa ferramenta simples de IA que utiliza Processamento de Linguagem Natural (NLP) para classificar o sentimento (positivo, negativo ou neutro) de feedbacks de clientes. O objetivo é ajudar pequenas empresas a automatizar a triagem de comentários. Projeto do curso de IA em desenvolvimento.

## Background
Muitas pequenas empresas recebem centenas de comentários e avaliações diariamente, mas não têm tempo para ler todos. Identificar rapidamente clientes insatisfeitos é crucial para a retenção.
* Problema 1: Sobrecarga de informação manual.
* Problema 2: Tempo de resposta lento para feedbacks negativos.
* Motivação: Facilitar a gestão de reputação online para empreendedores.

## Como é utilizado?
O utilizador insere uma lista de comentários num script Python ou carrega um ficheiro CSV. A IA processa cada texto e gera um relatório com a polaridade predominante.
* Utilizadores: Gestores de redes sociais, donos de pequenos negócios.
* Contexto: Análise pós-venda ou monitorização de redes sociais.

## Dados e técnicas de IA
O projeto utiliza a biblioteca `TextBlob` ou `VADER` para análise de sentimentos baseada em léxico.
* Fontes de dados: Exemplos sintéticos de feedbacks de clientes.
* Técnicas: Análise de Sentimentos (NLP).

## Desafios
* O projeto não deteta sarcasmo de forma eficaz.
* Limitações linguísticas (focado inicialmente em Inglês/Português dependendo da biblioteca).

## Próximos passos
* Integrar com a API do Google Maps ou Instagram para recolha automática.
* Treinar um modelo personalizado com Scikit-Learn para maior precisão.

## Agradecimentos
* Inspirado no curso "Building AI" da Universidade de Helsínquia.
* Bibliotecas: TextBlob / NLTK.
