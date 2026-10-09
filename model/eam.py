"""Model de persistência e consultas para o dashboard EAM."""

from __future__ import annotations

import sqlite3
from datetime import date, timedelta
from pathlib import Path
from typing import Any


class AtivoModel:
    """Cria e consulta o banco SQLite dos ativos."""

    def __init__(self, db_path: str | Path | None = None) -> None:
        self.db_path = Path(db_path) if db_path else Path(__file__).with_name(
            "eam_mvc_ativos.db"
        )
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._criar_banco()

    def _conectar(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path, timeout=10)
        connection.row_factory = sqlite3.Row
        return connection

    def _criar_banco(self) -> None:
        with self._conectar() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS ativos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT NOT NULL UNIQUE,
                    nome TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    localizacao TEXT NOT NULL,
                    status TEXT NOT NULL CHECK (
                        status IN ('Operacional', 'Em manutenção', 'Parado')
                    ),
                    criticidade TEXT NOT NULL CHECK (
                        criticidade IN ('Baixa', 'Média', 'Alta')
                    ),
                    ultima_manutencao TEXT NOT NULL,
                    proxima_manutencao TEXT NOT NULL
                )
                """
            )
            total = connection.execute(
                "SELECT COUNT(*) FROM ativos"
            ).fetchone()[0]
            if total == 0:
                self._inserir_dados_iniciais(connection)

    @staticmethod
    def _inserir_dados_iniciais(connection: sqlite3.Connection) -> None:
        hoje = date.today()
        registros = [
            ("ATV-001", "Bomba hidráulica P-101", "Bomba", "Setor A", "Operacional", "Alta", 18, 42),
            ("ATV-002", "Compressor de ar C-04", "Compressor", "Setor B", "Em manutenção", "Alta", 35, -2),
            ("ATV-003", "Esteira transportadora E-12", "Esteira", "Linha 1", "Operacional", "Média", 12, 18),
            ("ATV-004", "Motor elétrico M-208", "Motor", "Setor A", "Parado", "Alta", 74, -8),
            ("ATV-005", "Gerador de emergência G-02", "Gerador", "Utilidades", "Operacional", "Alta", 21, 60),
            ("ATV-006", "Empilhadeira EP-07", "Movimentação", "Armazém", "Operacional", "Média", 9, 25),
            ("ATV-007", "Caldeira industrial CL-01", "Caldeira", "Utilidades", "Em manutenção", "Alta", 46, 3),
            ("ATV-008", "Ventilador industrial V-33", "Ventilação", "Setor C", "Operacional", "Baixa", 15, 90),
            ("ATV-009", "Bomba centrífuga P-205", "Bomba", "Setor B", "Operacional", "Média", 28, 12),
            ("ATV-010", "Redutor de velocidade R-16", "Redutor", "Linha 2", "Parado", "Média", 63, -1),
        ]
        connection.executemany(
            """
            INSERT INTO ativos (
                codigo, nome, categoria, localizacao, status, criticidade,
                ultima_manutencao, proxima_manutencao
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    codigo,
                    nome,
                    categoria,
                    localizacao,
                    status,
                    criticidade,
                    (hoje - timedelta(days=dias_ultima)).isoformat(),
                    (hoje + timedelta(days=dias_proxima)).isoformat(),
                )
                for (
                    codigo,
                    nome,
                    categoria,
                    localizacao,
                    status,
                    criticidade,
                    dias_ultima,
                    dias_proxima,
                ) in registros
            ],
        )

    def get_kpis(self) -> dict[str, Any]:
        """Retorna as contagens agregadas usadas nos cartões do dashboard."""
        with self._conectar() as connection:
            resultado = connection.execute(
                """
                SELECT
                    COUNT(*) AS total,
                    COALESCE(SUM(status = 'Operacional'), 0) AS operacionais,
                    COALESCE(SUM(status = 'Em manutenção'), 0) AS manutencao,
                    COALESCE(SUM(status = 'Parado'), 0) AS parados,
                    COALESCE(SUM(criticidade = 'Alta'), 0) AS alta_criticidade,
                    COALESCE(SUM(proxima_manutencao < ?), 0) AS manutencao_atrasada
                FROM ativos
                """,
                (date.today().isoformat(),),
            ).fetchone()

        total = resultado["total"]
        return {
            **dict(resultado),
            "disponibilidade": (
                resultado["operacionais"] / total * 100 if total else 0.0
            ),
        }

    def get_ativos(self) -> list[dict[str, Any]]:
        """Retorna ativos ordenados para destacar primeiro os que precisam de atenção."""
        with self._conectar() as connection:
            registros = connection.execute(
                """
                SELECT codigo, nome, categoria, localizacao, status, criticidade,
                       proxima_manutencao
                FROM ativos
                ORDER BY
                    CASE status
                        WHEN 'Parado' THEN 0
                        WHEN 'Em manutenção' THEN 1
                        ELSE 2
                    END,
                    CASE criticidade
                        WHEN 'Alta' THEN 0
                        WHEN 'Média' THEN 1
                        ELSE 2
                    END,
                    nome
                """
            ).fetchall()
        return [dict(registro) for registro in registros]
