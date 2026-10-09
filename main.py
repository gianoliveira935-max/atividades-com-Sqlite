"""Ponto de entrada do Dashboard EAM."""

import tkinter as tk

from controler.dashboard_controller import DashboardController
from model.eam import AtivoModel
from view.dashboard_view import DashboardView


def main() -> None:
    banco = AtivoModel()
    janela = tk.Tk()
    tela = DashboardView(janela)
    controller = DashboardController(banco, tela)
    controller.atualizar()
    janela.mainloop()


if __name__ == "__main__":
    main()
