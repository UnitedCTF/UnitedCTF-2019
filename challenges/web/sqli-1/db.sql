CREATE TABLE IF NOT EXISTS `users` (
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES('admin', 'supers3cr3t');
INSERT INTO users (username, password) VALUES('guest', '123456789');