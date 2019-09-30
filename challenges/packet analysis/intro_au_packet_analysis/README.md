# Intro à l'analyse de traffic réseau

## Description

Wireshark est un outil qui sert à analyser des "packet capture" files (.pcap).
Un pcap est un fichier qui rassemble les communications qui passent sur une interface
réseau (exemple fil Ethernet, wifi).
Télécharger Wireshark: https://www.wireshark.org/
Les flags de ce challenge ne sont pas à faire en ordre nécessairement.
Le flag format est toujours **JDIS{informationDemandée}**

1. Trouvez le temps d'arrivée du 42e packet. Flag format: JDIS{posixTimestamp}.
Temps arrondi à la seconde près.

2. Combien d'octets est-ce que l'IP 192.168.142.42 a envoyé à 192.168.142.47?

3. Combien de packets UDP sont présents dans le pcap?

4. Une image a été téléchargée par une machine via un serveur Web. Cette image contient un flag!

5. Une machine a chargé un flag provenant d'une page Web!

6. Y'a des `ping` louches...?

7. Donnez la représentation hexadécimale (sans séparateur) de l'IP de destination du packet #321

8. Quelle est l'adresse MAC qui a l'IP 192.168.142.44? Format: JDIS{adresseMacEnMinusculeSéparéeParDesDeuxPoints}

9. Par combien de routages différent la réponse au packet envoyé au #2582 a-t-elle passé?


## Solution

1. Wireshark donne l'info en checkant le packet

2. Statistics->Conversations->ipv4

3. filtre: udp, checker en bas à droite

4. Wireshark export http objects

5. filtre: http

6. Exfiltration de data via ping filtre: icmp

7. regarder les raw bytes du champ IP

8. filtre: ip.src == 192.168.142.44

9. TTL request - TTL response

## Flag

1. JDIS{1534363107}
2. JDIS{4257}
3. JDIS{1519}
4. JDIS{imageExtraction}
5. JDIS{woopWoop}
6. JDIS{pingExfiltration}
7. JDIS{c0a88e01}
8. JDIS{00:0c:29:dd:e9:18}
9. JDIS{7}
