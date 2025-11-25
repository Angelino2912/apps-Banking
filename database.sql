
-- Tabel: datauser

CREATE TABLE datauser (
    id INT PRIMARY KEY AUTO_INCREMENT,
    no_rek VARCHAR(20) UNIQUE,
    username_us VARCHAR(255) NOT NULL UNIQUE,
    password_us VARCHAR(255) NOT NULL,
    balance INT DEFAULT 0,
    role_us VARCHAR(50)
);


-- Tabel: rekening

CREATE TABLE rekening (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    nomor_rekening VARCHAR(20) NOT NULL UNIQUE,
    saldo INT DEFAULT 0,

    FOREIGN KEY (username) REFERENCES datauser(username_us)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


-- Tabel: transaksi

CREATE TABLE transaksi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipe VARCHAR(20),
    jumlah INT,
    keterangan TEXT,
    tanggal DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabel: transfer

CREATE TABLE transfer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dari_rekening VARCHAR(20),
    ke_rekening VARCHAR(20),
    jumlah INT,
    tanggal DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (dari_rekening) REFERENCES rekening(nomor_rekening)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (ke_rekening) REFERENCES rekening(nomor_rekening)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);