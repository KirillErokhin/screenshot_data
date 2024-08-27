BOS = '<|begin_of_text|><|start_header_id|>system<|end_header_id|>'
EOS = '<|eot_id|><|start_header_id|>assistant<|end_header_id|>'

class DataTimeExtract:

    SYSTEM_PROMPT = f"""{BOS}Задание: На вход тебе подается текст в котором тебе нужно выделить дату и время. В ответе тебе нужно вывести ТОЛЬКО дату и время из этого текста в формате [ДД.ММ.ГГГГ ЧЧ:ММ]. В случае отсутствия даты и времени вывод должен быть [none].

Пример 1 - ///// Edil
View
Naiigate
Ccae
Refactar
Run
Ioals
VCS
Шindа :
Help
pithonftajecl
R;
PythonProjcct
8 p
Current File
pinins ay
1ay
5.a9
6_2 pу
7_1py
7_2ay
8Fу
9-1Py
9_2py
I0py
:
pythonPr  19
пи
turtle
penup
8
Python Turtle Graphics
1py
turtle gatola; 0)
2py
turtle
pendownt)
5p
6_2PУ
5
1
turtle.goto(x
9 2 Pу
10Pу
manr
Шfor
in raпge(iDВ);
pipliis
radlus
randam . randin
Extemal
caLor
(randami
гaшubli
13-25
Hi
( Ц) d
РУС
30.11.2023 /////
Твой ответ: 30.11.2023 13:25

Пример 2 - ///// asddd
11222
up here
Aaen /////
Твой ответ: None

Пример 3 - ///// 7_1-Fy 16
for angle
In range (361):
7 2py
9 33
aa~
10.11.2021
math cos(math
8 py
9_1Рy 18
math sin(math /////
Твой ответ: 10.11.2021 9:33

Теперь закончи следующий пример -
Вход: ///// """
    RESPONSE_TEMPLATE = f' ///// \nТвой ответ:{EOS}'


class DataTimeExtractDouble:

    SYSTEM_PROMPT = f"""{BOS}Задание: На вход тебе идут два текста от разных моделей OCR_1 и OCR_2. Твоя задача выделить дату и время в обоих текстах. Далее объединить их между собой для получения точных даты и времени. В качестве ответа тебе нужно вывести ТОЛЬКО дату и время из этих текстов в формате ДД.ММ.ГГГГ ЧЧ:ММ. В случае отсутствия даты и времени вывод должен быть none.

Пример 1 - ///// OCR_1: ///
4
crapt
1T
AHAEKC:
3
VICKYCCTBEHH
HTE
D
655d831321878png
9
crapr
C
McKyce
9
Hapncyi
Hapir
X
9
Hapucyre
annunc
C
noMOuIbIO
Turtle
Mypc
Python3
npoer
HaF
Python
Bo
Crpanna
nepenegemar
Ha
pyccKh
ryuions
Mecnerylire
Hawe
coobujecrmor
FKOR
nepeeecrw
ece
KapTHHKM
Nokasatb
opurman
-
import
package
dyHe
turleseth@sPython
import
ef
are
dyHKust
turtleresetou
Python
for
1
in
Fanget)
MemsAtuntleupoaPychon
twa
ares
turtle.cirele
(rad,
90)
turtle
eirele
(rad//2.30)
MeTOAR
Python-
45
turtle.
seth
(-45)
dyapen
turtlepen)sPython
calling
draw
method
drav(100)
dyHKIER
turtietito
Python
dyH
turtieshapetranstommos:
dyHKuist
turledgesdaPytion
turtle.DyHs
shearfactor0iPyhon
Mur
MCnoraTyewG
Gain
cooke,
wrodwo
cbecneur
BMH
awryauràe
onuT
mpocvorpa
wawero
webcahta
Mcnonaya
wauc
cait,
aun
naarmepwanete,
wompourran
noicanw
kauy!
DsostmxawassA
ahnorcookis
lonTsy
oMRaeawanecI
Nloman!
655de31321-
1TSprint
Ko3.
CnMCOK
C
KOO
x
10:57
p
4T,30
HOP
/// OCR_2: /// 
~тарг
(нленс;
ИЕктЕсТЕенннтат
съэган1 J21
prg
матол Емtаг
nana lart 
= ]а
Цнншцячtшtlesaeenshel)
Fuhaг
ы1: Чо
9h]
да7а:: 
т17>
вez1
фнит штелтп|
ТлhEп
eilnq
H 
Fothэе
5ъа2|нн
ФмнишJшешП 
Ftc
Фуници; Iutle shaactan-оппl| ₽ Рутлаn
Выцод
nitlэnnnmaml m Evthur
Нерисуйе paмt Uяилнуа сюрму € поuaLha Turtle
EmuahaнPithoji
trtlqбницн-пзас InaUm Eithor
Fthon
tunla Метол sreen l) setn 
фупицял tutlesetllanElel] 4 Руthan
Фнннцлtлlеdетгав5l] ввуТлал
turtle фницичshei-hctorl) ₽ Fyrhon
WuLbailon_ЗефовJaзмs ~гоооззаеильсуиайпияl]Jоп_л Бссклра]amllepLtcйn
Наолыишашанаыплтиссалвше
~лшпра_иа
1ашп]
Mmnunm
Пимви
655de31321
[TSprint Коз 
EЛИСЬК
KOD
10.57
ЧТ; 30 ноЯ /////
Твой ответ: 30.11.2023 10:57

Пример 2 - ///// OCR_1: ///
asddd
11222
up here
Aaen
/// OCR_2: /// 
Фнннцлtлlеdетгав5l] ввуТлал
Пимви
ффффаааа
220000000000
Пятьдесят /////
Твой ответ: none

Теперь закончи следующий пример -
Вход: ///// """
    RESPONSE_TEMPLATE = f' ///// \nТвой ответ:{EOS}'

class DataTimeExtractNew:

    SYSTEM_PROMPT = f"""{BOS}Твоя задача найти в тексте значения даты и времени. В качестве ответа тебе нужно вывести ТОЛЬКО дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ. В случае отсутствия даты и времени вывод должен быть none.

Пример 1 - ///// + +
compiler
аэ
 A    Ц1  (Ш
Run
Dehug
Stap
Share
14:41
H Sawe
Beautif
12.012005
Languаge /////
Порассуждаем и выведем только ответ: в тексте есть время - [14:41], и также дата - [12.012005].
Твой ответ: 12.01.2005 14:41

Пример 2 - ///// asddd
11222
up here
Aaen /////
Порассуждаем и выведем только ответ: в тексте нет времени и даты.
Твой ответ: None

Пример 3 - ///// 7_1-Fy 16
for angle
In range (361):
7 2py
9 33
aa~
10.11.2021
math cos(math
8 py
9_1Рy 18
math sin(math /////
Твой ответ: 10.11.2021 9:33

Теперь закончи следующий пример -
Вход: ///// """
    RESPONSE_TEMPLATE = f' ///// \nТвой ответ:{EOS}'