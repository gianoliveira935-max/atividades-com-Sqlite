"""Controller que conecta o model à view do dashboard."""

import sqlite3

from model.eam import AtivoModel
from view.dashboard_view import DashboardView


class DashboardController:
    """Busca indicadores no banco e atualiza a interface."""

    def __init__(self, model: AtivoModel, view: DashboardView) -> None:
        self.model = model
        self.view = view
        self.view.configurar_atualizacao(self.atualizar)

    def atualizar(self) -> None:
        try:
            kpis = self.model.get_kpis()
            ativos = self.model.get_ativos()
        except sqlite3.Error as erro:
            self.view.mostrar_erro(erro)
            return
        self.view.atualizar_dashboard(kpis, ativos)
