

TEXMFDIST		=/usr/share/texmf-dist
TEXMFDIST 		- Дерево, где находятся практически все файлы дистрибутива: конфигурационные файлы, шрифты, скрипты, пакеты и т.д. (основное исключение — зависящие от архитектуры программы, которые находятся в директории bin/.)


TEXMFLOCAL		=/usr/local/share/texmf:/usr/share/texmf
TEXMFLOCAL		- Дерево, которое может быть использовано администраторами системы для дополнительных пакетов, шрифтов и т.д.


TEXMFSYSVAR		=/var/lib/texmf
TEXMFSYSVAR		- Это дерево используется утилитами texconfig-sys, updmap-sys, fmtutil-sys, а так-же tlmgr для хранения создаваемых автоматически файлов: форматов, карт шрифтов, — общих для всех пользователей.


TEXMFSYSCONFIG	=/etc/texmf
TEXMFSYSCONFIG 	- Это дерево используется утилитами texconfig-sys, updmap-sys и fmtutil-sys для хранения модифицированных файлов конфигурации, общих для всех пользователей.


TEXMFHOME	=/home/dyuzha/texmf
TEXMFHOME	- Дерево, которое пользователи могут использовать для установки собственных пакетов, шрифтов и т.д., или для обновлённых версий системных пакетов. Эта переменная указывает на дерево в домашней директории, своей для каждого пользователя.


TEXMFVAR	=/home/dyuzha/.texlive/texmf-var
TEXMFVAR	- Это дерево используется утилитами texconfig, updmap-user и fmtutil-user для хранения создаваемых автоматически файлов: форматов, карт шрифтов.


TEXMFCONFIG=/home/dyuzha/.texlive/texmf-config
TEXMFCONFIG Это дерево используется утилитами texconfig, updmap-sys и fmtutil-sys для хранения модифицированных файлов конфигурации (своих для каждого пользователя)


TEXMFCACHE Это дерево используется программами ConTEXt MkIV и LuaLATEX для хранения файлов, создаваемых автоматически при работе программ. По умолчанию совпадает с TEXMFSYSVAR, или, если эта директория закрыта для записи, TEXMFVAR.


ENCFONTS=.:{{}/home/dyuzha/.texlive/texmf-config,/home/dyuzha/.texlive/texmf-var,/home/dyuzha/texmf,!!/usr/local/share/texmf:/usr/share/texmf,!!/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf-dist}/fonts/enc//


SYSTEXMF=/var/lib/texmf:/usr/local/share/texmf:/usr/share/texmf:/usr/share/texmf-dist


TEXCONFIG={{}/home/dyuzha/.texlive/texmf-config,/home/dyuzha/.texlive/texmf-var,/home/dyuzha/texmf,!!/usr/local/share/texmf:/usr/share/texmf,!!/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf-dist}/dvips//


TEXFONTMAPS=.:{{}/home/dyuzha/.texlive/texmf-config,/home/dyuzha/.texlive/texmf-var,/home/dyuzha/texmf,!!/usr/local/share/texmf:/usr/share/texmf,!!/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf-dist}/fonts/map/{kpsewhich,pdftex,dvips,}//

TEXMF={{}/home/dyuzha/.texlive/texmf-config,/home/dyuzha/.texlive/texmf-var,/home/dyuzha/texmf,!!/usr/local/share/texmf:/usr/share/texmf,!!/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf-dist}

TEXMFDBS={!!/usr/local/share/texmf:/usr/share/texmf,!!/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf-dist}

TEXMFMAIN=/usr/share/texmf-dist


TEXPSHEADERS=.:{{}/home/dyuzha/.texlive/texmf-config,/home/dyuzha/.texlive/texmf-var,/home/dyuzha/texmf,!!/usr/local/share/texmf:/usr/share/texmf,!!/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf-dist}/{dvips,fonts/{enc,type1,type42,type3}}//

VARTEXFONTS=/home/dyuzha/.texlive/texmf-var/fonts

WEB2C={{}/home/dyuzha/.texlive/texmf-config,/home/dyuzha/.texlive/texmf-var,/home/dyuzha/texmf,!!/usr/local/share/texmf:/usr/share/texmf,!!/etc/texmf,!!/var/lib/texmf,!!/usr/share/texmf-dist}/web2c
==== kpathsea variables from environment only (ok if no output here) ====
