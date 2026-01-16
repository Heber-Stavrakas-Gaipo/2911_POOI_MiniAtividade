# 🐍 Mini Atividades Python - POO I

> *Exercícios práticos de Programação Orientada a Objetos aplicados em Python*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Paradigm-OOP-blue?style=for-the-badge)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![Algoritmos](https://img.shields.io/badge/Algoritmos-Estruturas-green?style=for-the-badge)](https://en.wikipedia.org/wiki/Algorithm)
[![Console](https://img.shields.io/badge/Interface-Console-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/Command-line_interface)

## 🎯 Visão Geral

As **Mini Atividades Python** são uma coleção de exercícios práticos desenvolvidos para a disciplina de **Programação Orientada a Objetos I (POOI)** do Curso de Engenharia da Computação. Este conjunto de atividades demonstra conceitos fundamentais de programação em Python, com foco em **estruturas de controle**, **manipulação de dados**, **algoritmos** e **funções**.

### 👩‍🏫 Informações da Aula

- **Professora**: Cristina Maria Valadares de Lima
- **Data**: 01 de Novembro de 2025
- **Disciplina**: Programação Orientada a Objetos I (POOI)
- **Linguagem**: Python 3.8+
- **Modalidade**: Exercícios Práticos em Console

### ✨ Por que este conjunto é especial?

- 🎯 **Progressão Estruturada**: Do básico ao avançado
- 🔄 **Conceitos Variados**: Condicionais, loops, arrays, funções
- 📊 **Algoritmos Reais**: Problemas práticos do dia a dia
- 💡 **Aprendizado Incremental**: Cada exercício complementa o anterior
- 🛡️ **Tratamento de Dados**: Validações e conversões de tipos
- 🎮 **Interface Interativa**: Input/output com usuário
- 🔍 **Análise Estatística**: Cálculos e agregações de dados

## 📋 Lista de Atividades

### 1️⃣ **Mini Atividade 1 - Comparação de Números**

**Arquivo**: [miniAtividade1.py](miniAtividade1.py)

**Objetivo**: Comparar dois números e identificar o maior

**Conceitos Abordados**:
- ✅ **Entrada de Dados**: `input()` para capturar valores do usuário
- ✅ **Condicionais**: `if`, `elif` para comparação
- ✅ **Strings**: Comparação de strings e interpolação com f-strings
- ✅ **Saída Formatada**: `print()` com formatação

**Problema Resolvido**:
```
O programa solicita dois números ao usuário e exibe qual é o maior
```

**Conceitos POO Aplicados**:
- 📦 **Abstração**: O programa abstrai a complexidade de comparação
- 🔄 **Controle de Fluxo**: Uso de estruturas condicionais para dirigir a lógica

---

### 2️⃣ **Mini Atividade 2 - Cálculo de Área**

**Arquivo**: [miniAtividade2.py](miniAtividade2.py)

**Objetivo**: Calcular a área de um terreno e classificá-lo por tamanho

**Conceitos Abordados**:
- ✅ **Conversão de Tipos**: `int()` para converter strings em inteiros
- ✅ **Operações Aritméticas**: Multiplicação para cálculo de área
- ✅ **Condicionais Simples**: Classificação por valor limiar
- ✅ **Formatação de Strings**: Exibição com unidades (m²)

**Problema Resolvido**:
```
Calcula a área de um terreno (largura × profundidade)
Classifica como "Terreno grande!" se area > 100m²
```

**Conceitos POO Aplicados**:
- 🏗️ **Encapsulamento**: O cálculo encapsula a lógica de área
- 📊 **Abstração de Dados**: Valores abstratos representam propriedades físicas

---

### 3️⃣ **Mini Atividade 3 - Aumento de Salário**

**Arquivo**: [miniAtividade3.py](miniAtividade3.py)

**Objetivo**: Calcular aumento de salário baseado em faixas de renda

**Conceitos Abordados**:
- ✅ **Condicionais Encadeadas**: `if`, `elif`, `else` para múltiplas faixas
- ✅ **Operadores Lógicos**: `and` para combinar condições
- ✅ **Cálculos Percentuais**: Multiplicação por fatores de aumento
- ✅ **Precisão Numérica**: Trabalhar com valores monetários

**Problema Resolvido**:
```
Define percentuais de aumento por faixa de salário:
- Até R$ 280: +20%
- R$ 280-700: +15%
- R$ 700-1500: +10%
- Acima de R$ 1500: +5%
```

**Conceitos POO Aplicados**:
- 🔄 **Lógica Condicional Complexa**: Demonstra estruturas de decisão avançadas
- 💾 **Mutabilidade**: Alteração de variável durante execução

---

### 5️⃣ **Mini Atividade 5 - Análise de Números (Positivos e Negativos)**

**Arquivo**: [miniAtividade5.py](miniAtividade5.py)

**Objetivo**: Analisar uma coleção de números, calculando somas e médias

**Conceitos Abordados**:
- ✅ **Arrays/Listas**: `append()` para adicionar elementos dinamicamente
- ✅ **Loops while**: Entrada condicionada por usuário
- ✅ **String Comparison**: `lower()` para normalizar entrada
- ✅ **Loops for**: Iteração sobre coleção
- ✅ **Operadores Condicionais**: Classificação de números
- ✅ **Acumuladores**: Somas e contadores
- ✅ **Cálculos Estatísticos**: Médias aritméticas

**Problema Resolvido**:
```
Coleta números até o usuário desistir
Calcula:
- Soma de positivos e negativos
- Média de positivos e negativos
- Diferença entre quantidade de cada tipo
```

**Complexidade Algorítmica**:
- **Coleta**: O(n) onde n = quantidade de números
- **Processamento**: O(n) para cada iteração

**Conceitos POO Aplicados**:
- 📦 **Estrutura de Dados**: Uso de listas como coleção dinâmica
- 🔄 **Iteração**: Padrão de cada-um (for-each) para processamento
- 📊 **Agregação de Dados**: Múltiplos acumuladores para análise

---

### 6️⃣ **Mini Atividade 6 - Sequência de Fibonacci**

**Arquivo**: [miniAtividade6.py](miniAtividade6.py)

**Objetivo**: Gerar a sequência de Fibonacci até um limite especificado

**Conceitos Abordados**:
- ✅ **Listas**: Armazenamento de sequência
- ✅ **Loops while**: Iteração com critério de parada
- ✅ **Acesso a Índices**: `fibonacci[i-1]`, `fibonacci[i-2]`
- ✅ **Recursão Iterativa**: Padrão de Fibonacci implementado iterativamente
- ✅ **Casos Base**: Tratamento especial para primeiros elementos

**Problema Resolvido**:
```
Gera sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...
Cada número é a soma dos dois anteriores
Critério de parada: até n termos
```

**Complexidade Algorítmica**:
- **Tempo**: O(n)
- **Espaço**: O(n) para armazenar a sequência

**Conceitos POO Aplicados**:
- 🔄 **Padrão Iterativo**: Implementação não-recursiva de algoritmo clássico
- 📊 **Otimização**: Evita recalcular valores através de armazenamento
- 🧮 **Algoritmo Clássico**: Demonstra compreensão de padrões matemáticos

---

### 7️⃣ **Mini Atividade 7 - Pessoas Acima da Média**

**Arquivo**: [miniAtividade7.py](miniAtividade7.py)

**Objetivo**: Encontrar quantidade de pessoas com idade acima da média

**Conceitos Abordados**:
- ✅ **Funções**: Definição de `contaPessoasAcimaMedia()` com parâmetro
- ✅ **Listas**: Coleta de 10 idades
- ✅ **Loops for**: Duas iterações (cálculo de média e contagem)
- ✅ **Acumuladores**: Soma das idades
- ✅ **Estatística**: Cálculo de média aritmética
- ✅ **Função Reutilizável**: Encapsulação de lógica em função

**Problema Resolvido**:
```
Coleta 10 idades de pessoas
Calcula a idade média
Conta quantas pessoas estão acima dessa média
```

**Complexidade Algorítmica**:
- **Coleta**: O(10) = O(1) (número fixo)
- **Cálculo de Média**: O(n) onde n = 10
- **Contagem**: O(n) onde n = 10
- **Total**: O(n) = O(1)

**Conceitos POO Aplicados**:
- 🏗️ **Encapsulamento**: Lógica de cálculo encapsulada em função
- 🔄 **Reutilização**: Função pode ser chamada com diferentes listas
- 📦 **Modularização**: Separação de responsabilidades

---

### 8️⃣ **Mini Atividade 8 - Contagem de Vogais**

**Arquivo**: [miniAtividade8.py](miniAtividade8.py)

**Objetivo**: Contar a quantidade de vogais em um texto

**Conceitos Abordados**:
- ✅ **Iteração sobre Strings**: Loop for para cada caractere
- ✅ **Métodos de String**: `lower()` para normalizar case
- ✅ **Operadores Lógicos**: Múltiplas condições com `or`
- ✅ **Contadores**: Incremento para cada vogal encontrada
- ✅ **Busca**: Padrão de busca de caracteres específicos

**Problema Resolvido**:
```
Recebe um texto do usuário
Conta quantas vogais (A, E, I, O, U) estão presentes
Ignora case (maiúsculas e minúsculas)
```

**Complexidade Algorítmica**:
- **Tempo**: O(n) onde n = comprimento da string
- **Espaço**: O(1) apenas um contador

**Conceitos POO Aplicados**:
- 🔄 **Iteração sobre Coleção**: Strings são sequências em Python
- 🎯 **Busca Linear**: Padrão clássico de busca
- 📊 **Normalização**: Tratamento uniforme de dados (lower case)

---

## 🎓 Conceitos de POO Demonstrados

### 🏗️ **Encapsulamento**
```python
def contaPessoasAcimaMedia(lista):
    # Lógica encapsulada em função
    somaDasIdades = 0
    for idade in lista:
        somaDasIdades += idade
    media = somaDasIdades / len(lista)
    # ... resto da lógica
```

**Por que usar?**
- ✅ Agrupa comportamento relacionado
- ✅ Oculta detalhes de implementação
- ✅ Facilita reutilização de código
- ✅ Melhora legibilidade e manutenção

### 📦 **Abstração**
```python
# Usuário não precisa saber COMO calcular a média
# Apenas chama a função e obtém o resultado
resultado = contaPessoasAcimaMedia(lista)
```

**Benefícios**:
- ✅ Simplifica interface de uso
- ✅ Permite mudanças de implementação sem afetar código chamador
- ✅ Foca no "O QUÊ" em vez do "COMO"

### 🔄 **Reutilização de Código**
```python
# Estruturas de controle reutilizáveis
# Funções podem ser chamadas múltiplas vezes
# Padrões de algoritmos aplicados em diferentes contextos
```

### 📊 **Estruturas de Dados**
```python
vetor = []              # Lista dinâmica
fibonacci = []          # Sequência
lista = []              # Coleção de idades
```

**Progressão**:
- Strings (Mini Atividade 1, 8)
- Listas (Mini Atividade 5, 6, 7)
- Índices e acesso (Mini Atividade 5, 6, 7)

### 🎯 **Funções e Modularização**
```python
def contaPessoasAcimaMedia(lista):
    """Conta pessoas com idade acima da média"""
    # Função: unidade básica de modularização
```

---

## 🛠️ Como Executar

### Pré-requisitos
- 🐍 Python 3.8+ instalado
- 💻 IDE (VS Code, PyCharm, Thonny) ou terminal
- 📝 Editor de texto qualquer

### Passos de Execução

#### Opção 1: Terminal Windows (PowerShell ou CMD)
```bash
cd "c:\Users\heber\Documents\Programacao\POOI\Python\2911\(Mini) Atividade"
python miniAtividade1.py
```

#### Opção 2: VS Code
1. Abra o arquivo `.py` desejado
2. Pressione `Ctrl + F5` (ou click no botão Run)
3. Execute no terminal integrado

#### Opção 3: IDE Python
1. Abra a IDE (PyCharm, Thonny, etc)
2. Carregue o arquivo
3. Pressione Play/Run

### 🎮 Exemplo de Execução (Mini Atividade 1)

```
Digite o primeiro número: 10
Digite o segundo número: 25
O maior número é: 25
Números digitados: 10 e 25
```

---

## 📊 Progressão de Dificuldade

### Nível 1️⃣ - Fundamentação (Atividades 1-3)
- ✅ Entrada/saída de dados
- ✅ Conversão de tipos
- ✅ Operações aritméticas
- ✅ Condicionais simples e encadeadas

**Competências Desenvolvidas**:
- Compreensão de tipos de dados
- Uso de estruturas de decisão
- Formatação de saída

---

### Nível 2️⃣ - Intermediário (Atividades 5-6)
- ✅ Listas e coleções dinâmicas
- ✅ Loops (while e for)
- ✅ Acumuladores e contadores
- ✅ Índices e acesso a elementos
- ✅ Algoritmos mais complexos

**Competências Desenvolvidas**:
- Manipulação de estruturas de dados
- Iteração eficiente sobre coleções
- Padrões de agregação de dados
- Implementação de algoritmos clássicos

---

### Nível 3️⃣ - Avançado (Atividades 7-8)
- ✅ Funções e modularização
- ✅ Parametrização de comportamento
- ✅ Retorno de valores
- ✅ Lógica reutilizável
- ✅ Algoritmos especializados

**Competências Desenvolvidas**:
- Design modular de código
- Encapsulamento de lógica
- Reutilização efetiva
- Pensamento abstrato

---

## 🔧 Técnicas e Padrões Utilizados

### 🔄 **Padrão: Acumuladores**
```python
# Mini Atividade 5
somaPositivos = 0
for num in vetor:
    if num > 0:
        somaPositivos += num  # Acumula valor
```

**Uso**: Agregar valores (somas, produtos, contagens)

---

### 🔍 **Padrão: Contador**
```python
# Mini Atividade 5
contaPositivos = 0
for num in vetor:
    if num > 0:
        contaPositivos += 1  # Incrementa contador
```

**Uso**: Contar ocorrências ou elementos

---

### 🔀 **Padrão: Busca Linear**
```python
# Mini Atividade 8
counter = 0
for letra in texto:
    if letra.lower() in "aeiou":  # Busca caractere
        counter += 1
```

**Complexidade**: O(n)  
**Uso**: Localizar elementos em coleção

---

### 📈 **Padrão: Construção Iterativa**
```python
# Mini Atividade 6
fibonacci = []
while i < valor:
    if i == 0:
        fibonacci.append(0)
    # ... construir sequência
```

**Uso**: Construir estruturas incrementalmente

---

### 📊 **Padrão: Cálculo Estatístico**
```python
# Mini Atividade 7
somaDasIdades = 0
for idade in lista:
    somaDasIdades += idade
media = somaDasIdades / len(lista)
```

**Uso**: Análise e agregação de dados

---

## 🎓 Competências Desenvolvidas

### 💡 **Conceitual**
- ✅ Compreensão de tipos primitivos (int, str, float)
- ✅ Estruturas de controle de fluxo
- ✅ Lógica de programação
- ✅ Design de algoritmos

### 🔧 **Prático**
- ✅ Entrada/saída de dados
- ✅ Manipulação de strings
- ✅ Operações com listas
- ✅ Implementação de funções
- ✅ Debugging e testes

### 📚 **Estruturas de Dados**
- ✅ Strings como sequências de caracteres
- ✅ Listas como coleções dinâmicas
- ✅ Índices e acesso de elementos
- ✅ Iteração eficiente

### 🧮 **Algoritmos**
- ✅ Busca linear
- ✅ Contagem e acumulação
- ✅ Geração de sequências (Fibonacci)
- ✅ Cálculos estatísticos
- ✅ Classificação por categorias

### 🎯 **Habilidades POO**
- ✅ Encapsulamento em funções
- ✅ Abstração de lógica
- ✅ Reutilização de código
- ✅ Modularização
- ✅ Pensamento orientado a objetos

---

## 🔮 Extensões Propostas

### 🚀 **Melhorias Imediatas**
- 🔄 **Reutilização**: Refatorar código repetido em funções auxiliares
- 📝 **Documentação**: Adicionar docstrings em todas as funções
- 🧪 **Validações**: Implementar tratamento de exceções (try/except)
- 🎨 **Formatação**: Melhorar apresentação com cores e tabelas

### 📦 **Próximos Passos (Classes)**
- 🏗️ Transformar lógica em classes reutilizáveis
- 🔐 Implementar encapsulamento com atributos privados
- 🔄 Herança para especialização
- 💾 Persistência de dados em arquivos

### 💾 **Persistência**
```python
# Possível extensão: salvar resultados em arquivo
import json

def salvarResultados(dados):
    with open('resultados.json', 'w') as f:
        json.dump(dados, f)
```

### 🔐 **Validação Avançada**
```python
# Possível extensão: tratamento de erros
try:
    valor = int(input("Digite um número: "))
except ValueError:
    print("Erro: Entrada inválida!")
```

---

## 📚 Estrutura do Projeto

```
(Mini) Atividade/
├── 📄 README.md                 # Esta documentação
├── 🐍 miniAtividade1.py        # Comparação de números
├── 🐍 miniAtividade2.py        # Cálculo de área
├── 🐍 miniAtividade3.py        # Aumento de salário
├── 🐍 miniAtividade5.py        # Análise de números
├── 🐍 miniAtividade6.py        # Sequência de Fibonacci
├── 🐍 miniAtividade7.py        # Pessoas acima da média
└── 🐍 miniAtividade8.py        # Contagem de vogais
```

---

## 🤝 Notas Pedagógicas

### 🎓 **Sequência de Aprendizado**

As atividades foram ordenadas **propositalmente** para criar uma progressão:

1. **Atividades 1-3**: Fundamentação em tipos e condicionais
2. **Atividades 5-6**: Introdução a coleções e loops
3. **Atividades 7-8**: Funções e padrões algorítmicos avançados

### 💡 **Objetivos de Aprendizagem**

Ao completar este conjunto, o aluno será capaz de:

- ✅ Escrever programas Python funcionais
- ✅ Implementar estruturas de controle apropriadas
- ✅ Manipular coleções de dados
- ✅ Criar e usar funções reutilizáveis
- ✅ Aplicar padrões de algoritmos comuns
- ✅ Pensar em termos de encapsulamento e abstração
- ✅ Preparar-se para Programação Orientada a Objetos com classes

### 🔗 **Conexão com POO Completa**

Estes exercícios são **ponte** para conceitos avançados:

| Conceito | Atividade | Evolução POO |
|----------|-----------|--------------|
| Funções | 7 | → Métodos de Classes |
| Encapsulamento | 7 | → Atributos Privados |
| Estruturas | 5, 6, 7 | → Composição de Objetos |
| Reutilização | 7, 8 | → Herança |
| Abstração | Todas | → Classes Abstratas |

---

## 📞 Referências e Recursos

### 📖 **Documentação Oficial**
- [Python.org Documentation](https://docs.python.org/3/)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Data Types](https://docs.python.org/3/tutorial/datastructures.html)

### 🎓 **Conceitos de POO**
- Encapsulamento: Agrupamento de dados e comportamento
- Abstração: Simplificação de interface
- Reutilização: Compartilhamento de código
- Modularização: Separação em unidades independentes

### 💻 **Ferramentas Recomendadas**
- **Visual Studio Code**: Editor leve e poderoso
- **PyCharm Community**: IDE especializada em Python
- **Thonny**: IDE para iniciantes
- **Jupyter Notebook**: Para exploração interativa

---

<div align="center">

**🐍 Desenvolvido em Python durante POOI I**

*"A programação é a arte de dizer a outro humano o que você quer que o computador faça." - Donald Knuth*

**Professora: Cristina Maria Valadares de Lima**  
**Data: 01 de Novembro de 2025**

</div>
