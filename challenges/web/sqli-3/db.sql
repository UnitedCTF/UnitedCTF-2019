.load /libsqlitemd5

CREATE TABLE IF NOT EXISTS `users` (
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES('admin', hex(md5('asdjm23128JASDJj23daksa213BFD1')));