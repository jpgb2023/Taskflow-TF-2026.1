# 1. Requisitos Funcionais

<p align="justify">A <i>Tabela 1</i> a seguir contém os Requisitos Funcionais (RF) elicitados utilizando a técnica de Brainstorm e depois o refinamento.</p>

| ID | Requisito | Prioridade | Requisitos Relacionados |
| :--- | :--- | :---: | :---: |
| **RF01** | O usuário deve poder criar novas tarefas informando **título** (obrigatório), **descrição** (opcional) e **data de vencimento** (opcional). | Alta | - |
| **RF02** | O sistema deve exibir uma lista de tarefas, permitindo a visualização clara do título, status e prioridade. | Alta | RF01 |
| **RF03** | O usuário deve poder editar o título, a descrição e a prioridade de uma tarefa já existente. | Alta | RF01, RF02 |
| **RF04** | O usuário deve poder alternar o status de uma tarefa entre "Pendente" e "Concluída" com um clique. | Alta | RF02 |
| **RF05** | O usuário deve poder excluir uma tarefa, com uma janela de confirmação para evitar cliques acidentais. | Alta | RF02 |
| **RF06** | O usuário deve poder atribuir e filtrar tarefas por **Nível de Prioridade** (Baixa, Média, Alta). | Média | RF01, RF02 |
| **RF07** | O sistema deve permitir a busca de tarefas por texto, filtrando os resultados conforme o usuário digita no campo de pesquisa. | Média | RF02 |
| **RF08** | O usuário deve poder criar **Tags ou Categorias** (ex: Trabalho, Pessoal, Estudos) e associá-las às tarefas. | Média | RF01 |
| **RF09** | O sistema deve impedir a criação de tarefas sem título, exibindo uma mensagem de erro amigável ao usuário. | Alta | RF01 |
| **RF10** | O sistema deve destacar visualmente (ex: cor vermelha) tarefas cuja data de vencimento já expirou. | Baixa | RF01, RF02 |
<div style="text-align: center">
<p>Tabela 1: Requisitos Funcionais</p>
</div>

# 2. Referências

<a href="../README.md">VOLTAR INÍCIO</a>
