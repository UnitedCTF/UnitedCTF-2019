.load /libsqlitemd5

CREATE TABLE IF NOT EXISTS `users` (
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES('clone1', hex(md5('p4ssw0rd')));
INSERT INTO users (username, password) VALUES('clone2', hex(md5('bad_password')));
INSERT INTO users (username, password) VALUES('clone3', hex(md5('123456789')));
INSERT INTO users (username, password) VALUES('clone4', hex(md5('apple')));
INSERT INTO users (username, password) VALUES('admin', hex(md5('2yv6sMMJ5zfHtMgw')));
INSERT INTO users (username, password) VALUES('clone5', hex(md5('ilikefood')));
INSERT INTO users (username, password) VALUES('clone6', hex(md5('stop spying')));
INSERT INTO users (username, password) VALUES('clone6', hex(md5('sqli2 ftw')));
INSERT INTO users (username, password) VALUES('clone7', hex(md5('hello world')));
INSERT INTO users (username, password) VALUES('clone8', hex(md5('987654321')));
INSERT INTO users (username, password) VALUES('clone9', hex(md5('last clone')));