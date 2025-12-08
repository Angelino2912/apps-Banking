
-- Tabel: datauser

CREATE TABLE datauser (
    id INT PRIMARY KEY AUTO_INCREMENT,
    no_rek VARCHAR(20) UNIQUE,
    username_us VARCHAR(255) NOT NULL UNIQUE,
    password_us VARCHAR(255) NOT NULL,
    balance INT DEFAULT 0,
    role_us VARCHAR(50)
);



-- Tabel: transaksi

CREATE TABLE IF NOT EXISTS history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username_us VARCHAR(30),
    description TEXT,
    amount DOUBLE,
    timestamp DATETIME
);