# 🧠 Avaliação Técnica – Analista de Dados (Webscraping)

Este projeto foi desenvolvido como parte de uma **avaliação técnica para vaga de Analista de Dados**, com foco em **Webscraping, ETL, SQL e visualização interativa em Streamlit**.

O objetivo principal foi demonstrar habilidades práticas em coleta, tratamento, armazenamento e análise de dados do agronegócio, simulando um **pipeline de dados completo**, desde a camada **raw** até a **curated**.

---

## 📚 Estrutura do Projeto

```
├── clean_data/                             # Dados tratados e limpos
├── raw_data/                               # Dados brutos coletados (CSV/JSON)
├── notebooks/                              # Notebooks de análise e exploração
├── 1_scrapper.ipynb                        # Scripts de webscraping (Selenium)
├── 2_table_creation.ipynb                  # Scripts de tratamento e carga (ETL)
├── 3_SQL_questions.ipynb                   # Scripts SQL e respostas de perguntas pertinentes
├── 4_python_questions.ipynb                # Demonstração da aplicação streamlit
├── 5_insights_and_documentation.ipynb      # Análise dos dados e insights retirados do projeto
├── streamlit_dashboards.py                 # Aplicação interativa de visualização
├── requirements.txt                        # Dependências do projeto
├── README.md                               # Documentação principal
└── .env.example                            # Exemplo de variáveis de ambiente (credenciais do banco)
```

---

## ⚙️ Ambiente de Execução

- **Linguagem:** Python 3.10+
- **Banco de dados:** PostgreSQL 14+
- **Interface:** Streamlit
- **Bibliotecas principais:** `Selenium`, `pandas`, `sqlalchemy`, `streamlit`, `plotly`

---

## 🚀 Passos para Reproduzir o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/jovemadulto/agromercantil_challenge.git
cd agromercantil_challenge
```

### 2️⃣ Criar o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
.venv\Scripts\activate        # Windows
```

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o banco de dados PostgreSQL

Crie um banco de dados local (exemplo):

```sql
CREATE DATABASE database_etl;
```

Copie o arquivo `.env.example` e configure suas credenciais:

```
DB_USER=postgres
DB_PASS=senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=database_etl
```

### 5️⃣ Executar o pipeline ETL

Execute os arquivos `*.ipynb` para obter os dados, limpá-los e popular o banco de dados PostgreSQL criado.

### 6️⃣ Rodar a aplicação Streamlit

```bash
streamlit run streamlit_dashboards.py
```

Acesse em:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 📊 Funcionalidades da Aplicação

- Filtros interativos
- Gráficos dinâmicos (linhas, barras, boxplots)
- Estatísticas descritivas e detecção de outliers
- Indicadores SQL como **preço médio mensal** e **variação percentual (LAG)**

---

## 🧩 Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Webscraping | Selenium |
| ETL / Tratamento | Pandas, SQLAlchemy |
| Banco de Dados | PostgreSQL |
| Visualização | Streamlit, Plotly |
| Análises | SQL + Python (Pandas) |
| Controle de versão | Git / GitHub |

---

## 🧠 Resultados e Insights

- Identificação de tendências de preço por região e produto  
- Análise temporal com variação percentual mensal (função SQL `LAG`)  
- Detecção de outliers e correção de inconsistências  
- Proposta de índices para otimização de consultas em PostgreSQL  

---

## 📸 Evidências

O repositório inclui:
- Prints das consultas SQL
- Capturas da interface Streamlit
- Justificativas de modelagem e índices aplicados

---

## 🧾 Licença

Este projeto é de uso acadêmico/técnico, criado exclusivamente para fins de **avaliação profissional**.

---

**Autor:** João Ernane Barbosa
https://www.linkedin.com/in/joaoernane/
