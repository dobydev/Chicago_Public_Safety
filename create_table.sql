CREATE TABLE IF NOT EXISTS chicago_crimes (
    id BIGINT PRIMARY KEY,
    date TIMESTAMP,
    primary_type VARCHAR(150),
    district VARCHAR(10),
    arrest BOOLEAN NOT NULL,
    hour INTEGER,
    day_of_week VARCHAR(50),
    -- Ensure arrest_flag only contains valid binary values: 0 = no arrest, 1 = arrest
    arrest_flag INTEGER NOT NULL CHECK (arrest_flag IN (0, 1))
);