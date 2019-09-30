CREATE TABLE IF NOT EXISTS `users` (
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
);
INSERT INTO users (username, password) VALUES('admin', "13cdde4338251155eefc9bf698eeb824f2ebc9e0");


CREATE TABLE IF NOT EXISTS `access_logs` (
    `ip` VARCHAR(32) NOT NULL,
    `timestamp` DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS `s3cr%t_fl4g_is_h3re` (
    `flag` VARCHAR(255) NOT NULL
);
INSERT INTO `s3cr%t_fl4g_is_h3re` (flag) VALUES("FLAG{Proxy_to-[sqli]_Wh4t-tH3_!%&*#?}");
