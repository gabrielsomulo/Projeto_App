-- Rode este script uma vez no seu banco PostgreSQL antes de usar o projeto.
-- Exemplo: psql -U postgres -d cadastro_db -f schema.sql

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    criado_em TIMESTAMP NOT NULL DEFAULT NOW()
);
