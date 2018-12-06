from ftplib import FTP

ftp = FTP()
ftp.connect('207.148.15.49', '21')
ftp.login('root', 'Jieshenziai')
with 