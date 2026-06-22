import tkinter as tk
from tkinter import ttk

class Componentes:
    def __init__(self, parent):
        self.parent = parent

    def criar_label(
        self,
        texto,
        row,
        column,
        columnspan=1,
        sticky="w",
        font=("Arial", 10),
        parent=None
    ):
        label = ttk.Label(parent or self.parent, text=texto, font=font)
        label.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            sticky=sticky,
            padx=5,
            pady=2
        )
        return label

    def criar_entry(
        self,
        row,
        column,
        columnspan=1,
        sticky="we",
        parent=None
    ):
        entry = ttk.Entry(parent or self.parent)
        entry.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            sticky=sticky,
            padx=5,
            pady=2
        )
        return entry

    def criar_text(
        self,
        row,
        column,
        columnspan=1,
        rowspan=1,
        sticky="we",
        parent=None
    ):
        text_widget = tk.Text(parent or self.parent, height=4, width=30)
        text_widget.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            rowspan=rowspan,
            sticky=sticky,
            padx=5,
            pady=2
        )
        return text_widget

    def criar_button(
        self,
        texto,
        comando,
        row,
        column,
        columnspan=1,
        sticky="we",
        style=None,
        parent=None
    ):
        button = ttk.Button(
            parent or self.parent,
            text=texto,
            command=comando,
            style=style
        )

        button.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            sticky=sticky,
            padx=5,
            pady=5
        )

        return button

    def criar_combobox(
        self,
        valores,
        row,
        column,
        columnspan=1,
        sticky="we",
        parent=None
    ):
        combobox = ttk.Combobox(
            parent or self.parent,
            values=valores,
            state="readonly"
        )

        combobox.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            sticky=sticky,
            padx=5,
            pady=2
        )

        combobox.set(valores[0] if valores else "")
        return combobox

    def criar_checkbox(
        self,
        texto,
        variavel,
        row,
        column,
        columnspan=1,
        sticky="w",
        parent=None
    ):
        checkbox = ttk.Checkbutton(
            parent or self.parent,
            text=texto,
            variable=variavel
        )

        checkbox.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            sticky=sticky,
            padx=5,
            pady=2
        )

        return checkbox

    def criar_treeview(
        self,
        colunas,
        row,
        column,
        columnspan=1,
        rowspan=1,
        sticky="nsew",
        parent=None
    ):
        tree = ttk.Treeview(
            parent or self.parent,
            columns=colunas,
            show="headings"
        )

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        tree.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            rowspan=rowspan,
            sticky=sticky,
            padx=5,
            pady=5
        )

        scrollbar = ttk.Scrollbar(
            parent or self.parent,
            orient="vertical",
            command=tree.yview
        )

        scrollbar.grid(
            row=row,
            column=column + columnspan,
            rowspan=rowspan,
            sticky="ns"
        )

        tree.configure(yscrollcommand=scrollbar.set)

        return tree

    def criar_frame(
        self,
        row,
        column,
        columnspan=1,
        rowspan=1,
        sticky="nsew",
        padding=5,
        parent=None
    ):
        frame = ttk.Frame(parent or self.parent, padding=padding)

        frame.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            rowspan=rowspan,
            sticky=sticky
        )

        return frame