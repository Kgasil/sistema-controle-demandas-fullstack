-- ============================================================================
-- Camada de Dados: Controle de Demandas e Custos Operacionais
-- Autor: Kaio Gabriel da Silva
-- ============================================================================

CREATE TABLE IF NOT EXISTS demandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(120) NOT NULL,
    area VARCHAR(60) NOT NULL,
    custo_estimado DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    status VARCHAR(30) NOT NULL DEFAULT 'Pendente',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO demandas (titulo, area, custo_estimado, status) VALUES
('Automação de relatório diário', 'Dados & Processos', 1200.00, 'Em Andamento'),
('Revisão de tabela de custos', 'Orçamentação', 850.00, 'Pendente'),
('Integração de planilha com API', 'Backoffice', 1500.00, 'Concluído');

-- Consulta de resumo por status e área
SELECT
    area,
    status,
    COUNT(*) AS total_demandas,
    SUM(custo_estimado) AS custo_total
FROM demandas
GROUP BY area, status
ORDER BY custo_total DESC;
