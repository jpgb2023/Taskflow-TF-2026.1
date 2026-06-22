# TaskFlow - Gerenciador de Tarefas

Este é o projeto acadêmico "TaskFlow", um sistema To-Do List desenvolvido para a disciplina de Desenvolvimento Ágil do curso de Engenharia da Computação.

## Visão Geral

O TaskFlow é um gerenciador de tarefas simples e funcional, desenvolvido em Python com interface gráfica Tkinter e persistência de dados em MySQL. Ele permite criar, listar, marcar como concluídas e excluir tarefas, além de filtrá-las por status.

## Estrutura do Projeto

```
taskflow/
│
├── main.py
├── database/
│   ├── conexao.py
│   └── database.sql
│
├── models/
│   └── tarefa.py
│
├── services/
│   └── tarefa_service.py
│
├── ui/
│   ├── interface.py
│   └── componentes.py
│
├── assets/
│   └── (imagens e outros recursos)
│
├── requirements.txt
└── README.md
```

## Tecnologias Utilizadas

- Python
- Tkinter (para a interface gráfica)
- MySQL (como banco de dados)
- `mysql-connector-python` (para conexão com o banco de dados)

## Como Instalar e Executar

Siga os passos abaixo para configurar e executar o projeto TaskFlow em sua máquina local.

### 1. Pré-requisitos

Certifique-se de ter instalado:

- Python 3.x
- MySQL Server
- MySQL Workbench (ou outro cliente MySQL para executar o script SQL)

### 2. Configuração do Banco de Dados MySQL

1. **Crie o banco de dados e a tabela:**
   Abra o MySQL Workbench (ou seu cliente MySQL preferido) e execute o script `database/database.sql`.
   Este script criará o banco de dados `taskflow` e a tabela `tarefas`.

   ```sql
   CREATE DATABASE IF NOT EXISTS taskflow;
   USE taskflow;

   CREATE TABLE IF NOT EXISTS tarefas (
       id INT AUTO_INCREMENT PRIMARY KEY,
       titulo VARCHAR(255) NOT NULL,
       descricao TEXT,
       prioridade VARCHAR(50),
       data_tarefa DATE,
       concluida BOOLEAN DEFAULT FALSE
   );
   ```

2. **Credenciais do Banco de Dados:**
   O sistema está configurado para usar as seguintes credenciais padrão:
   - `host`: "localhost"
   - `user`: "root"
   - `password`: "" (vazio)
   - `database`: "taskflow"

   Se suas credenciais MySQL forem diferentes, edite o arquivo `database/conexao.py` para atualizá-las.

### 3. Instalação das Dependências Python

Navegue até o diretório raiz do projeto (`taskflow/`) e instale as dependências usando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Execução do Projeto

Após instalar as dependências e configurar o banco de dados, você pode executar o aplicativo:

```bash
python main.py
```

Isso abrirá a interface gráfica do TaskFlow.

## Funcionalidades

- **Criar Tarefa:** Adicione novas tarefas com título, descrição, prioridade e data.
- **Listar Tarefas:** Visualize todas as tarefas, com status de conclusão e prioridade.
- **Marcar como Concluída:** Altere o status de uma tarefa para concluída.
- **Excluir Tarefa:** Remova tarefas do sistema.
- **Filtrar Tarefas:** Filtre a lista de tarefas para exibir apenas as pendentes ou as concluídas.

## Screenshots (Placeholder)

![Screenshot da Interface Principal](assets/screenshot_main.png)
*Captura de tela da interface principal do TaskFlow (placeholder)*

![Screenshot da Criação de Tarefas](assets/screenshot_create.png)
*Captura de tela da tela de criação de tarefas (placeholder)*

## Contribuição

Este projeto é parte de um trabalho acadêmico. Contribuições externas não são esperadas neste momento.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` (se aplicável) para mais detalhes.
