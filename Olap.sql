CREATE EXTENSION IF NOT EXISTS cube;

CREATE EXTENSION IF NOT EXISTS tablefunc;

CREATE INDEX IF NOT EXISTS idx_fact_waktu
ON fact_market(id_waktu);

CREATE INDEX IF NOT EXISTS idx_dim_waktu
ON dim_waktu(id_waktu);

CREATE MATERIALIZED VIEW mv_market_summary AS
SELECT
    d.kuartal,
    d.is_weekend,
    ROUND(AVG(f.btc_close)::numeric,2) AS rata_rata_btc,
    ROUND(AVG(f.fed_rate)::numeric,2) AS rata_rata_fed
FROM fact_market f
JOIN dim_waktu d
ON f.id_waktu = d.id_waktu
GROUP BY d.kuartal, d.is_weekend;
