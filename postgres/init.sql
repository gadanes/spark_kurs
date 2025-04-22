CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary NUMERIC
);

INSERT INTO employees (name, position, salary) VALUES
('Alice', 'Data Scientist', 90000),
('Bob', 'Data Engineer', 85000),
('Carol', 'Analyst', 70000);
