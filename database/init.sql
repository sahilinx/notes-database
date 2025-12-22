CREATE DATABASE notesdb;

CREATE USER 'notesuser'@'%' IDENTIFIED BY 'notespwd';
GRANT ALL PRIVILEGES ON notesdb.* TO 'notesuser'@'%';
FLUSH PRIVILEGES;
