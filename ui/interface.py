import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from services.tarefa_service import TarefaService
from models.tarefa import Tarefa
from ui.componentes import Componentes


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskFlow - Gerenciador de Tarefas")
        self.root.geometry("1000x600")

        self.tarefa_service = TarefaService()
        self.componentes = Componentes(root)
        self.tarefa_editando_id = None  # Controla se está editando

        self.criar_estilos()
        self.criar_layout()
        self.tarefa_service.inserir_tarefas_exemplo()
        self.carregar_tarefas()

    def criar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        self.primary_color = "#4CAF50"
        self.secondary_color = "#FFC107"
        self.background_color = "#F5F5F5"
        self.text_color = "#333333"

        self.root.configure(bg=self.background_color)

        style.configure("TFrame", background=self.background_color)
        style.configure("TLabel", background=self.background_color, foreground=self.text_color)
        style.configure("TButton", background=self.primary_color, foreground="white", font=("Arial", 10, "bold"))
        style.map("TButton", background=[("active", "#66BB6A")])
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background=self.primary_color, foreground="white")
        style.configure("Treeview", font=("Arial", 10), rowheight=25)
        style.map("Treeview", background=[("selected", self.primary_color)])

    def criar_layout(self):
        form_frame = self.componentes.criar_frame(row=0, column=0, sticky="nsew", padding=10)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=0)

        self.componentes.criar_label("Título:", row=0, column=0, parent=form_frame)
        self.titulo_entry = self.componentes.criar_entry(row=0, column=1, parent=form_frame)

        self.componentes.criar_label("Descrição:", row=1, column=0, parent=form_frame)
        self.descricao_text = self.componentes.criar_text(row=1, column=1, parent=form_frame)

        self.componentes.criar_label("Prioridade:", row=2, column=0, parent=form_frame)
        self.prioridade_combobox = self.componentes.criar_combobox(
            ["Baixa", "Média", "Alta"], row=2, column=1, parent=form_frame
        )
        self.prioridade_combobox.set("Média")

        self.componentes.criar_label("Data (YYYY-MM-DD):", row=3, column=0, parent=form_frame)
        self.data_entry = self.componentes.criar_entry(row=3, column=1, parent=form_frame)
        self.data_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        button_frame = self.componentes.criar_frame(row=4, column=0, columnspan=2, parent=form_frame)
        self.btn_salvar = self.componentes.criar_button(
            "Adicionar Tarefa", self.salvar_tarefa, row=0, column=0, parent=button_frame
        )
        self.componentes.criar_button("Limpar Campos", self.limpar_campos, row=0, column=1, parent=button_frame)

        list_frame = self.componentes.criar_frame(row=1, column=0, sticky="nsew", padding=10)
        self.root.grid_rowconfigure(1, weight=1)

        filter_frame = self.componentes.criar_frame(row=0, column=0, parent=list_frame)
        self.componentes.criar_button("Todas", lambda: self.carregar_tarefas("todas"), row=0, column=0, parent=filter_frame)
        self.componentes.criar_button("Pendentes", lambda: self.carregar_tarefas("pendentes"), row=0, column=1, parent=filter_frame)
        self.componentes.criar_button("Concluídas", lambda: self.carregar_tarefas("concluidas"), row=0, column=2, parent=filter_frame)

        self.tree = self.componentes.criar_treeview(
            ["ID", "Título", "Descrição", "Prioridade", "Data", "Concluída"],
            row=1, column=0, parent=list_frame
        )
        self.tree.bind("<Double-1>", self.on_item_double_click)

        action_button_frame = self.componentes.criar_frame(row=2, column=0, parent=list_frame)
        self.componentes.criar_button("Marcar como Concluída", self.marcar_como_concluida, row=0, column=0, parent=action_button_frame)
        self.componentes.criar_button("Excluir Tarefa", self.excluir_tarefa, row=0, column=1, parent=action_button_frame)

    def salvar_tarefa(self):
        titulo = self.titulo_entry.get().strip()
        descricao = self.descricao_text.get("1.0", tk.END).strip()
        prioridade = self.prioridade_combobox.get()
        data_str = self.data_entry.get().strip()

        if not titulo or not data_str:
            messagebox.showwarning("Atenção", "Título e Data são campos obrigatórios.")
            return

        try:
            data_tarefa = datetime.strptime(data_str, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Atenção", "Formato de data inválido. Use YYYY-MM-DD.")
            return

        tarefa = Tarefa(
            id=self.tarefa_editando_id,
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            data_tarefa=data_tarefa
        )

        if self.tarefa_editando_id:
            sucesso, mensagem = self.tarefa_service.editar_tarefa(tarefa)
            msg_sucesso = "Tarefa editada com sucesso!"
        else:
            sucesso, mensagem = self.tarefa_service.criar_tarefa(tarefa)
            msg_sucesso = "Tarefa adicionada com sucesso!"

        if sucesso:
            messagebox.showinfo("Sucesso", msg_sucesso)
            self.limpar_campos()
            self.carregar_tarefas()
        else:
            messagebox.showerror("Erro", f"Não foi possível salvar a tarefa.\n\nDetalhes: {mensagem}")

    def carregar_tarefas(self, filtro="todas"):
        for i in self.tree.get_children():
            self.tree.delete(i)

        tarefas = self.tarefa_service.listar_tarefas(filtro=None if filtro == "todas" else filtro)

        for tarefa in tarefas:
            self.tree.insert("", "end", values=(
                tarefa.id,
                tarefa.titulo,
                tarefa.descricao,
                tarefa.prioridade,
                tarefa.data_tarefa,
                "Sim" if tarefa.concluida else "Não"
            ))

    def marcar_como_concluida(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione uma tarefa para marcar como concluída.")
            return

        tarefa_id = self.tree.item(selected_item)["values"][0]
        if messagebox.askyesno("Confirmar", f"Deseja marcar a tarefa {tarefa_id} como concluída?"):
            if self.tarefa_service.marcar_como_concluida(tarefa_id):
                messagebox.showinfo("Sucesso", "Tarefa marcada como concluída!")
                self.carregar_tarefas()
            else:
                messagebox.showerror("Erro", "Não foi possível marcar a tarefa como concluída.")

    def excluir_tarefa(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Atenção", "Selecione uma tarefa para excluir.")
            return

        tarefa_id = self.tree.item(selected_item)["values"][0]
        if messagebox.askyesno("Confirmar", f"Deseja realmente excluir a tarefa {tarefa_id}?"):
            if self.tarefa_service.excluir_tarefa(tarefa_id):
                messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")
                self.carregar_tarefas()
            else:
                messagebox.showerror("Erro", "Não foi possível excluir a tarefa.")

    def limpar_campos(self):
        self.titulo_entry.delete(0, tk.END)
        self.descricao_text.delete("1.0", tk.END)
        self.prioridade_combobox.set("Média")
        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.tarefa_editando_id = None
        self.btn_salvar.config(text="Adicionar Tarefa")

    def on_item_double_click(self, event):
        selected_item = self.tree.focus()
        if not selected_item:
            return

        valores = self.tree.item(selected_item)["values"]
        self.tarefa_editando_id = valores[0]

        # Preenche o formulário com os dados da tarefa selecionada
        self.titulo_entry.delete(0, tk.END)
        self.titulo_entry.insert(0, valores[1])

        self.descricao_text.delete("1.0", tk.END)
        self.descricao_text.insert("1.0", valores[2] or "")

        self.prioridade_combobox.set(valores[3])

        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(0, str(valores[4]))

        self.btn_salvar.config(text="Salvar Edição")


if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
