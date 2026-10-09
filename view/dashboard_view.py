"""Interface gráfica Tkinter do dashboard EAM."""

from __future__ import annotations

import tkinter as tk
from datetime import datetime
from tkinter import ttk
from typing import Any, Callable


class DashboardView:
    """Monta a janela, os cartões de KPI e a tabela de ativos."""

    BG = "#0f172a"
    PANEL = "#1e293b"
    PANEL_LIGHT = "#263449"
    TEXT = "#f1f5f9"
    MUTED = "#94a3b8"
    CORES_KPI = {
        "total": "#38bdf8",
        "operacionais": "#34d399",
        "manutencao": "#fbbf24",
        "parados": "#fb7185",
        "disponibilidade": "#a78bfa",
    }

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("EAM | Monitoramento de Ativos")
        self.root.configure(bg=self.BG)
        self.root.geometry("1180x720")
        self.root.minsize(850, 580)
        self._configurar_estilos()
        self._montar_tela()

    def _configurar_estilos(self) -> None:
        estilo = ttk.Style(self.root)
        estilo.theme_use("clam")
        estilo.configure(
            "Ativos.Treeview",
            background=self.PANEL,
            fieldbackground=self.PANEL,
            foreground=self.TEXT,
            rowheight=34,
            borderwidth=0,
            font=("Segoe UI", 10),
        )
        estilo.configure(
            "Ativos.Treeview.Heading",
            background=self.PANEL_LIGHT,
            foreground=self.MUTED,
            relief="flat",
            font=("Segoe UI", 9, "bold"),
            padding=(8, 10),
        )
        estilo.map(
            "Ativos.Treeview",
            background=[("selected", "#334155")],
            foreground=[("selected", self.TEXT)],
        )
        estilo.map(
            "Ativos.Treeview.Heading",
            background=[("active", self.PANEL_LIGHT)],
        )

    def _montar_tela(self) -> None:
        principal = tk.Frame(self.root, bg=self.BG, padx=28, pady=22)
        principal.pack(fill="both", expand=True)
        principal.grid_columnconfigure(0, weight=1)
        principal.grid_rowconfigure(3, weight=1)

        cabecalho = tk.Frame(principal, bg=self.BG)
        cabecalho.grid(row=0, column=0, sticky="ew", pady=(0, 22))
        textos = tk.Frame(cabecalho, bg=self.BG)
        textos.pack(side="left", fill="x", expand=True)
        tk.Label(
            textos,
            text="Monitoramento de Ativos",
            bg=self.BG,
            fg=self.TEXT,
            font=("Segoe UI", 23, "bold"),
        ).pack(anchor="w")
        tk.Label(
            textos,
            text="Visão geral da operação e da saúde dos equipamentos",
            bg=self.BG,
            fg=self.MUTED,
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(4, 0))
        self.botao_atualizar = tk.Button(
            cabecalho,
            text="⟳  Atualizar",
            bg="#2563eb",
            fg="#ffffff",
            activebackground="#1d4ed8",
            activeforeground="#ffffff",
            relief="flat",
            cursor="hand2",
            padx=16,
            pady=10,
            font=("Segoe UI", 10, "bold"),
        )
        self.botao_atualizar.pack(side="right")

        area_kpis = tk.Frame(principal, bg=self.BG)
        area_kpis.grid(row=1, column=0, sticky="ew", pady=(0, 18))
        for coluna in range(5):
            area_kpis.grid_columnconfigure(coluna, weight=1, uniform="kpi")

        self.valores_kpi: dict[str, tk.Label] = {}
        indicadores = (
            ("total", "TOTAL DE ATIVOS", "—"),
            ("operacionais", "OPERACIONAIS", "—"),
            ("manutencao", "EM MANUTENÇÃO", "—"),
            ("parados", "PARADOS", "—"),
            ("disponibilidade", "DISPONIBILIDADE", "—%"),
        )
        for coluna, (chave, titulo, inicial) in enumerate(indicadores):
            cartao = tk.Frame(area_kpis, bg=self.PANEL, padx=15, pady=14)
            cartao.grid(
                row=0,
                column=coluna,
                sticky="nsew",
                padx=(0 if coluna == 0 else 9, 0),
            )
            tk.Label(
                cartao,
                text=titulo,
                bg=self.PANEL,
                fg=self.MUTED,
                font=("Segoe UI", 8, "bold"),
            ).pack(anchor="w")
            valor = tk.Label(
                cartao,
                text=inicial,
                bg=self.PANEL,
                fg=self.CORES_KPI[chave],
                font=("Segoe UI", 24, "bold"),
            )
            valor.pack(anchor="w", pady=(7, 0))
            self.valores_kpi[chave] = valor

        painel_alertas = tk.Frame(principal, bg=self.PANEL, padx=15, pady=12)
        painel_alertas.grid(row=2, column=0, sticky="ew", pady=(0, 14))
        self.texto_alertas = tk.Label(
            painel_alertas,
            text="Carregando alertas de manutenção...",
            bg=self.PANEL,
            fg=self.MUTED,
            font=("Segoe UI", 10),
        )
        self.texto_alertas.pack(anchor="w")

        painel_tabela = tk.Frame(principal, bg=self.PANEL, padx=14, pady=14)
        painel_tabela.grid(row=3, column=0, sticky="nsew")
        painel_tabela.grid_columnconfigure(0, weight=1)
        painel_tabela.grid_rowconfigure(1, weight=1)
        tk.Label(
            painel_tabela,
            text="Ativos monitorados",
            bg=self.PANEL,
            fg=self.TEXT,
            font=("Segoe UI", 12, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 12))

        colunas = (
            "codigo",
            "nome",
            "categoria",
            "localizacao",
            "status",
            "criticidade",
            "proxima_manutencao",
        )
        self.tabela_ativos = ttk.Treeview(
            painel_tabela,
            columns=colunas,
            show="headings",
            style="Ativos.Treeview",
        )
        cabecalhos = {
            "codigo": ("CÓDIGO", 90),
            "nome": ("EQUIPAMENTO", 230),
            "categoria": ("CATEGORIA", 115),
            "localizacao": ("LOCAL", 105),
            "status": ("STATUS", 130),
            "criticidade": ("CRITICIDADE", 100),
            "proxima_manutencao": ("PRÓX. MANUTENÇÃO", 135),
        }
        for coluna, (texto, largura) in cabecalhos.items():
            self.tabela_ativos.heading(coluna, text=texto)
            self.tabela_ativos.column(
                coluna, width=largura, minwidth=75, anchor="w"
            )
        self.tabela_ativos.tag_configure("Parado", foreground="#fda4af")
        self.tabela_ativos.tag_configure("Em manutenção", foreground="#fcd34d")
        self.tabela_ativos.tag_configure("Operacional", foreground="#6ee7b7")
        self.tabela_ativos.grid(row=1, column=0, sticky="nsew")
        barra_rolagem = ttk.Scrollbar(
            painel_tabela,
            orient="vertical",
            command=self.tabela_ativos.yview,
        )
        self.tabela_ativos.configure(yscrollcommand=barra_rolagem.set)
        barra_rolagem.grid(row=1, column=1, sticky="ns")

        rodape = tk.Frame(principal, bg=self.BG)
        rodape.grid(row=4, column=0, sticky="ew", pady=(12, 0))
        self.status = tk.Label(
            rodape,
            text="Conectando ao banco de dados...",
            bg=self.BG,
            fg=self.MUTED,
            font=("Segoe UI", 9),
        )
        self.status.pack(side="left")
        tk.Label(
            rodape,
            text="EAM  •  Gestão de ativos",
            bg=self.BG,
            fg="#64748b",
            font=("Segoe UI", 9),
        ).pack(side="right")

    def configurar_atualizacao(self, comando: Callable[[], None]) -> None:
        self.botao_atualizar.configure(command=comando)

    def atualizar_dashboard(
        self, kpis: dict[str, Any], ativos: list[dict[str, Any]]
    ) -> None:
        valores = {
            "total": str(kpis["total"]),
            "operacionais": str(kpis["operacionais"]),
            "manutencao": str(kpis["manutencao"]),
            "parados": str(kpis["parados"]),
            "disponibilidade": f'{kpis["disponibilidade"]:.1f}%',
        }
        for chave, texto in valores.items():
            self.valores_kpi[chave].configure(text=texto)

        atrasados = kpis["manutencao_atrasada"]
        criticidade_alta = kpis["alta_criticidade"]
        if atrasados or kpis["parados"]:
            mensagem = (
                f"⚠  Atenção: {kpis['parados']} ativo(s) parado(s)  •  "
                f"{atrasados} manutenção(ões) vencida(s)  •  "
                f"{criticidade_alta} ativo(s) de alta criticidade"
            )
            cor = "#fbbf24"
        else:
            mensagem = (
                "✓  Operação estável  •  "
                f"{criticidade_alta} ativo(s) de alta criticidade monitorado(s)"
            )
            cor = "#34d399"
        self.texto_alertas.configure(text=mensagem, fg=cor)

        for item in self.tabela_ativos.get_children():
            self.tabela_ativos.delete(item)
        for ativo in ativos:
            self.tabela_ativos.insert(
                "",
                "end",
                values=(
                    ativo["codigo"],
                    ativo["nome"],
                    ativo["categoria"],
                    ativo["localizacao"],
                    ativo["status"],
                    ativo["criticidade"],
                    ativo["proxima_manutencao"],
                ),
                tags=(ativo["status"],),
            )
        self.status.configure(
            text=(
                f"Dados atualizados às {datetime.now().strftime('%H:%M:%S')}  •  "
                f'{kpis["total"]} ativo(s) no banco SQLite'
            ),
            fg=self.MUTED,
        )

    def mostrar_erro(self, erro: Exception) -> None:
        self.status.configure(
            text=f"Falha ao consultar o banco de dados: {erro}",
            fg="#f87171",
        )
