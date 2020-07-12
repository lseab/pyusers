CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    lock_time TIME(0),
    login_attempts INTEGER,
    salt TEXT NOT NULL,
    password VARCHAR(50) NOT NULL);