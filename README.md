# 📊 Projeto NPS - Net Promoter Score

Este projeto consiste em um sistema simples, desenvolvido em Python, para calcular o **Net Promoter Score (NPS)**, uma métrica utilizada para avaliar o nível de satisfação e lealdade dos clientes em relação a uma empresa ou serviço.

## 🚀 Funcionalidades

- Adição de notas (de 0 a 10) dadas por usuários.
- Cálculo do NPS com base nas notas coletadas.
- Classificação do NPS em zonas de satisfação:
  - Zona Crítica
  - Zona Neutra (Razoável)
  - Zona de Qualidade (Muito bom)
  - Zona de Excelência (Excelente)
- Modo interativo de coleta de dados via terminal.

## 🧠 Lógica do NPS

As notas são classificadas da seguinte forma:

- **Detratores:** notas de 0 a 6
- **Neutros:** notas 7 e 8 (não afetam o cálculo do NPS)
- **Promotores:** notas 9 e 10


```
NPS = % Promotores - % Detratores
```

## 💻 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Execute o script principal:
   ```bash
   python nome_do_arquivo.py
   ```

3. Siga as instruções no terminal para inserir as notas dos usuários. Para encerrar, digite `sair`.

## 🧪 Exemplo de uso

```bash
Em uma escala de 0 a 10, o quanto você recomendaria essa empresa a um amigo ou colega
Digite sair para encerrar a pesquisa: 10
Digite sair para encerrar a pesquisa: 9
Digite sair para encerrar a pesquisa: 7
Digite sair para encerrar a pesquisa: sair
```

Saída esperada:
```
Notas registradas: [10, 9, 7]
NPS: 66.67
Zona de qualidade (Muito bom)
```

## 📂 Estrutura do projeto

```
.
├── nps.py            # Classe Nps com métodos de cálculo e classificação
├── main.py           # Script com execução e entrada interativa
└── README.md         # Este arquivo
```

## 🛠️ Requisitos

- Python 3.6+
- Nenhuma biblioteca externa é necessária.
