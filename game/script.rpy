﻿# Определение персонажей игры.
define oleg = Character('Олег', color = "#8280ff")
define oleg_thoughts = Character('Олег', color = "#2a28be")
define boss = Character('Иван Михайлович', color = "#beffbe")
define clown = Character('Толя', color = "#befff1")
define rat = Character('Сергей', color = "#befff1")
define worker = Character('Геннадий', color = "#befff1")
define active = Character('Екатерина', color = "#befff1")
define shelb = Character('shelby', color = "#befff1")

# "Гифки"
image bossx:
    "boss.png"
    0.5
    "boss_rot.png"
    0.5
    repeat
image clownx:
    "boss.png"
    0.5
    "boss_rot.png"
    0.5
    repeat
image ratx:
    "boss.png"
    0.5
    "boss_rot.png"
    0.5
    repeat
image activex:
    "boss.png"
    0.5
    "boss_rot.png"
    0.5
    repeat
image workerx:
    "boss.png"
    0.5
    "boss_rot.png"
    0.5
    repeat

# Игра начинается здесь:
label start:

    # Очки отношений
    $ active_points = 0
    $ rat_points = 0
    $ worker_points = 0
    stop music
    play music pechat
    centered "Вы ведущий специалист информационной безопасности в крупной фирме, специализирующейся на перевозке грузов. Сегодня к вам обратилось руководство с поручением выявить виновного в утечке важных данных."
    centered "Вас, под видом обычного сотрудника, внедряют в отдел, где работает подозреваемый. Вы должны, полагаясь на дедуктивный метод, выявить причастного к сливу данных."
    centered "От вас зависит дальнейшая судьба всей компании. Приступайте к расследованию."
    stop music
    play sound pechatdate
    centered "{size=+20}{color=#00ff00}Барнаул, Алтайский край{/size}{/color}"
    play sound pechatdate
    centered "{size=+20}{color=#00ff00} 11 сентября 2002 года, 8:00{/size}{/color}"

    jump first_day

label first_day:

    ###
    # DAY 1
    ###

    ### Boss office scene

    play music huefon
    scene boss_office with fade

    show boss at center with dissolve

    boss "Доброе утро, Олег Евгеньевич."
    boss "Меня зовут Иван Михайлович, и я являюсь руководителем этого отдела. Полагаю, Вас уже примерно ввели в курс дела?"

    oleg "Здравствуйте, Иван Михайлович. Да, меня посвятили в происходящее."
    oleg "Однако перед тем, как приступить к работе, мне хотелось бы узнать побольше об этом месте и работающих здесь людях."

    boss "Да, конечно. Данный отдел занимается логистикой. Как Вы понимаете, информация, к которой есть доступ у моих сотрудников, крайне важна для компании."
    boss "Именно поэтому Вам необходимо найти виновного в утечке в ближайшее время."
    boss "Всего в этом отделе работает 5 человек, у которых есть доступ к слитой информации. Думаю, стоит описать Вам каждого из них."

    show boss at left with move

    show clown at right with dissolve
    boss "Первым в списке подозреваемых находится Анатолий. Довольно веселый и жизнерадостный человек, легок в общении."
    hide clown

    show rat at right with dissolve
    boss "Вторым подозреваемым является Сергей. Имеет весьма неприятный характер, честно говоря."
    boss "Пытается выслужиться любыми возможными способами передо мной, часто жалуется на своих коллег."
    hide rat

    show worker at right with dissolve
    boss "Третьим будет Геннадий. Пожалуй, лучший работник в этом отделе. Крайне продуктивен и трудолюбив."
    hide worker

    show active at right with dissolve
    boss "Далее по списку у нас Екатерина. Её можно назвать самым энергичным и социально активным сотрудником."
    boss "Она ответственна за большинство мероприятий по тимбилдингу. Именно благодаря ей, коллектив у нас, за некоторым исключением, довольно дружный."
    hide active

    show boss at center with fade

    boss "Что же, вроде рассказал Вам, Олег Евгеньевич, все, что знал."
    boss "Я руковожу этим отделом не так давно, и поэтому не настолько хорошо знаю своих людей, чтобы делать какие-то выводы самому."
    boss "Но все же, если будут какие-то вопросы, - обращайтесь."
    boss "Прошу также держать меня в курсе событий."
    boss "Однако не стоит бегать ко мне по каждому поводу, иначе Вы вызовете подозрения. Просто заходите ко мне время от времени, чтобы доложить обстановку"
    boss "И не забывайте, Олег Евгеньевич: Вас направили сюда, потому что Вы отлично зарекомендовали себя ранее, и высшее руководство рассчитывает на Вас."
    boss "От Вас зависит не только Ваша собственная репутация, но и репутация всей компании. Если вы выдадите себя, второй попытки уже не будет."
    boss "Поэтому я искренне желаю Вам удачи."

    oleg "Понял, спасибо за наводки, Иван Михайлович. Я понимаю, что время поджимает, поэтому приступлю к работе немедленно."

    boss "Отлично. Тогда вот Вам мой последний совет на сегодня: осмотрите весь отдел, чтобы уметь ориентироваться здесь, и познакомьтесь с каждым из подозреваемых лично."

    oleg "Вас понял, до свидания."

    scene black_screen with fade

    oleg_thoughts "(По всей видимости, это самое серьезное дело, за которое я брался)"
    oleg_thoughts "(Нужно не ударить в грязь лицом)"

    ### clown Scene

    scene office with fade

    oleg_thoughts "(Ладно, теперь надо осмотреться здесь. Пойду-ка я поищу свое рабочее мес...)"

    with vpunch
    with hpunch
    show clown at center with dissolve

    clown "Ох-ох, ну и больно! , дружище!"
    clown "Тут все-таки логистический отдел, люди занятые работают. Не чета разгильдяем из главного управления!"

    oleg "Прошу прощения, призадумался тут немного."

    clown "Ничего, бывает. Ты, похоже, тот самый новый сотрудник, о котором нам недавно говорили."
    clown "Приятно познакомиться, меня Толей звать!"

    oleg "Взаимно, Меня Олег зовут. Cегодня мой первый день. Вот, Иван Михайлович проводил мне инструктаж."

    clown "Иван Михайлович любит толкать речи. Он тот еще оратор, этого у него не отнять."
    clown "Ладно, осваивайся тут потихоньку, а мне работать надо. Еще увидимся!"

    oleg "До встречи."
    oleg_thoughts "(Похоже, это был мой первый подозреваемый. И вправду, весьма позитивный человек)"

    hide clown with dissolve

    ### rat scene

    oleg_thoughts "(Хорошо, вот и первое знакомство. Теперь уже точно мне сле...)"

    "???" "Только познакомились, а он уже на 'ты'. Какое непрофессиональное поведение. Впрочем, как обычно..."

    oleg_thoughts "(Ну, кто на этот раз?)"

    show rat at center with moveinright

    rat "Моё имя Сергей, будем знакомы."
    rat "К сожалению, большинство сотрудников здесь придерживаются подобного неформального стиля общения."

    menu:
        rat "Как по мне, это пагубно влияет на рабочую атмосферу, Вы не согласны?"
        "Полностью согласен":
            oleg "Да, конечно, это крайне непрофессионально, я полностью с Вами согласен."
            rat "Рад это слышать."
            rat "В этом месте наблюдается критическая нехватка адекватных работников."
            rat "Надеюсь, с Вашим приходом, здесь начнутся перемены."
            oleg "Не переживайте, я не подведу."
            rat "Тогда нам нужно будет как-нибудь обсудить нашу стратегию по повышению профессиональных качеств наших коллег."
            oleg_thoughts "(Только не это...)"
            $ rat_points += 1
        "Не согласен":
            oleg "На самом деле, я не думаю, что это как-то может навредить работе."
            hide rat
            show rat_angry at center
            rat "..."
            rat "Вы меня несколько разочаровали."
            rat "Смею напомнить: платить Вам будут не за пустую болтовню."
            rat "Очень жаль. Я думал, что с Вашим приходом, здесь начнутся перемены."
            oleg_thoughts "(Отлично. Первый день, и я уже успел с кем-то поссориться)"
            hide rat_angry
            show rat
            $ rat_points -= 1

    rat "Хорошо, не буду больше задерживать, у Вас сегодня много дел."
    rat "До встречи."

    hide rat
    scene black_screen
    with fade

    oleg_thoughts "(Действительно, характер Сергея не из самых приятных...)"

    play sound pechatdate
    centered "{color=#00ff00}11 сентября 2002 года, 12:00{/color}"
    stop music

    play music huefon

    ### worker scene

    scene office2 with fade
    show worker at center with fade

    worker "Да уж, ну и денек сегодня..."
    worker "О, ты тот новенький! Кажется, тебя зовут Олег, да?"
    oleg "Да, приветствую, Геннадий, начальник мне о тебе рассказывал как о самом старательном сотруднике."
    worker "Ой, да пустяки, я всего то отвечаю за разработку всего корпоративного софта в отделе."
    menu:
        oleg_thoughts "(Хм, а вот это уже становится интересно)"
        "Разузнать поподробнее о его работе":
            oleg "А что конкретно ты разрабатываешь сейчас?"
            worker "А, да ничего серьезного, думаю над расширением функциональности программы по составлению и расчёту маршрутов."

        "Спросить его об успехах":
            oleg "Как успехи?"
            worker "Да вот, понемногу дорабатываю свою программу, вот только пока ничего толкового не выходит."
            worker "Эх, как же надоела эта работа, а еще и платят мало..."
            $ worker_points += 1

        "Промолчать":
            oleg "..."
            worker "..."

    "Кофемашина" "* бип - бип *"
    worker "Ой, у меня там кофе уже приготовился, надо бы поторопиться, пока не остыл."
    worker "Приятно было пообщаться, до встречи, Олег."
    oleg "Хорошего дня."
    oleg_thoughts "(По нему видно, что ему приходится нелегко. На нем лежит немало ответственности)"

    hide worker with dissolve

    ### active scene
    with fade

    oleg_thoughts "(Так, ладно, пора за работу)"

    with vpunch
    with hpunch

    oleg_thoughts "(Стоп, а что мне, собственно говоря, надо делать?)"
    oleg_thoughts "(Кажется, Иван Михайлович забыл сказать, какое именно у меня прикрытие...)"
    oleg_thoughts "(Ладно, надо что-нибудь придумать. Не болтать же мне целый день с коллегами)"

    show active with dissolve

    active "Привет! Извини, что отвлекаю от работы."
    active "Меня зовут Катя, я менеджер-логист."

    menu:
        active "Ты, как я понимаю, наш новый программист, да?"
        "Именно":
            oleg_thoughts "(Отлично, вот и узнал, кем я работаю)"
            oleg "Да, это я. Сегодня мой первый день."
            active "Так и знала! Нам недавно сообщили о том, что к нашей команде присоединится новый человек."
            active "Жаль, я опоздала немного на работу."
            active "Мы собирались все вместе встретить тебя и отметить пополнение коллектива в столовой!"
            active "Но ты, наверно, уже со всеми успел познакомиться, так что смысла в собрании уже нет."
        "Программист?":
            oleg "Программист? Ты сейчас про кого это?"
            active "..."
            active "Ха-ха, ну ты и шутник!"
            active "Если бы ты не был новым программистом, тебя бы просто не пустили сюда."
            active "Кажется, у Толи появился соперник за звание лучшего юмориста отдела логистики!"
            $ active_points += 1

    active "Думаю, в скором времени мы точно проведем какое-нибудь мероприятие по укреплению дружественных связей между коллегами."
    oleg_thoughts "(Отличная возможность узнать всех подозреваемых поближе)"
    active "Осталось только придумать, что же это будет..."
    active "Ладно, не буду отвлекать тебя. Пока!"

    stop music

    ### home scene
    scene black_screen with fade

    play music pechat
    centered "{color=#00ff00}11 сентября 2002 года, 21:00{/color}"
    stop music

    scene home with fade

    oleg_thoughts "(Да уж, это был безумный день, но надо двигаться дальше)"
    oleg_thoughts "(Завтра предстоит поставить свою систему безопасности на все компьютеры в офисе, чтобы выявить крота)"
    oleg_thoughts "(А сейчас стоить немного отдохнуть...)"

    jump second_day

label second_day:

    ###
    # DAY 2
    ###

    ### comp scene 1

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}12 сентября 2002 года, 8:30{/color}"

    play music huefon

    scene office2 with fade
    oleg_thoughts "(Так, вот я и в офисе. Сейчас нужно быстро внедрить свою программу на компьютеры всех подозреваемых до того, как они придут на работу)"
    oleg_thoughts "(Начну с рабочих мест Екатерины и Геннадия)"

    scene black_screen with fade
    play sound comp
    "Компьютер" "* звук включения *"
    "Компьютер" "..."
    "Компьютер" "..."
    "Компьютер" "Программа успешно установлена"

    play music huefon

    scene office2 with fade
    oleg_thoughts "(Все, готово, теперь нужно установить программу на компьютеры Анатолия и Сергея)"

    ### comp scene 2

    scene office with fade

    oleg_thoughts "(Время на исходе, скоро начнется рабочий день)"

    with fade

    oleg_thoughts "(Так, остался всего один компьютер...)"
    
    with vpunch
    with hpunch

    show rat with dissolve

    rat "Что здесь происходит?"
    show rat_angry with dissolve
    rat "Что Вы делаете на моем рабочем месте? И кто дал Вам право пользоваться моим компьютером?!"

    if rat_points == 1:

        oleg "Иван Михайлович попросил меня проверить работоспособность всех компьютеров в офисе,"
        oleg "Чтобы, в случае поломки чего-либо, запросить новое оборудование."
        hide rat_angry 
        show rat with dissolve
        rat "Хм, ладно, теперь понятно. Что ж, продолжайте проверку, не буду отвлекать."
        $ rat_points += 1
        hide rat
        oleg_thoughts "(Вот это конечно пронесло)"
        oleg_thoughts "(Еще немного, и он, кажется, устроил бы скандал)"
        oleg_thoughts "(Надо постараться не конфликтовать с подозреваемыми, пока я не буду уверен в чьей-либо вине)"
        "Компьютер" "Программа успешно установлена"
    
    else:
        oleg "..."
        rat "Отвечайте!"
        "Антивирус"
        oleg "Эм, да я вот проверял просто тут это, ну, антивирус в общем..."
        rat "..."
        rat "Убирайтесь прочь."
        oleg_thoughts "(Надо успеть поставить программу!)"
        "Компьютер" "..."
        rat "Вы издеваетесь?!"
        $ rat_points -= 1
        "Компьютер" "Программа успешно установлена"
        oleg_thoughts "(Всё!)"
        oleg "Уже ухожу."
        hide rat_angry 

    ### conversation scene

    scene black_screen with fade

    play sound pechatdate
    centered "{color=#00ff00}12 сентября 2002 года, 14:00{/color}"
    stop music

    show office with fade

    show active at left with dissolve
    active "Наш коллектив нуждается в этом!"

    show worker at right with dissolve
    worker "У нас нет времени на эту чушь!"

    oleg "Всем здрасьте, что тут происходит?"
    worker "Она опять лезет ко всем со своими идиотскими идеями!"
    active "Никакие они не идиотские!"
    oleg "Что у вас произошло?"
    active "Я предлагаю всем вместе поехать на природу в эти выходные."
    active "Мы пообщаемся, узнаем друг друга получше. Короче говоря, укрепим дружеские связи и повысим моральный дух в команде!"
    oleg "Звучит не так плохо."
    worker "Ага, только у нас тут завал, ведь кое-кто, вместо того, чтобы работать, рассуждает о каких-то дружеских связях и морали."
    worker "Мой дух был бы на высоте, еслы бы мне не приходилось задерживаться и доделывать чью-то работу."
    active "Олег, посмотри на все эти унылые лица! Разве им не нужно немного развеяться?"
    menu:
        "Это пойдет на пользу":
            oleg "Не вижу ничего плохого в этом мероприятии."
            active "Вот так вот, двое против одного!"
            $ active_points += 1
            worker "Помимо нас тут работает еще куча людей. Их спросить не забыла?"
            active "Ой, точно. Пойду поговорю с остальными."
            hide active
            worker "Ну и слава Богу, наконец-то можно спокойно поработать."
            
        "Работа важнее":
            oleg "Мне кажется, стоит сначала разобраться с работой, прежде чем задумываться о какой-то сторонней деятельности."
            worker "Дело говоришь."
            active "Да это ведь только на пользу пойдет всему коллективу!"
            worker "Тебе уже два человека сказали, что это чушь. Сделай дело - гуляй смело."
            active "Понятно с вами все!"
            hide active
            $ worker_points += 1
    
    hide worker

    oleg_thoughts "(Да уж, не самая приятная беседа получилась)"
    oleg "(Ну, всякое бывает. Пожалуй, стоит пойти ""поработать"", чтобы ни у кого не было вопросов ко мне)"

    ### home scene
    scene black_screen with fade

    play music pechat
    centered "{color=#00ff00}12 сентября 2022 года, 21:00{/color}"
    stop music

    scene home with fade

    oleg_thoughts "(Денек, конечно, не из легких выдался)"
    oleg_thoughts "(Надеюсь, виновный в утечке не заставит себя долго ждать)"
    oleg_thoughts "(И кто же, интересно, сделал это? Никто их всех этих подозреваемых не тянет на злостного вора)"
    oleg_thoughts "(Ладно, пока что информации слишком мало, чтобы делать какие-то выводы. Сейчас стоит просто немного отдохнуть...)"

    jump third_day

    label third_day:

    ###
    # DAY 3
    ###

    ### boss scene

    play music pechat
    centered "{color=#00ff00}13 сентября 2002 года, 8:30{/color}"
    stop music

    play music huefon

    scene boss_office with fade

    show boss at center with dissolve

    boss "Доброе утро, Олег Евгеньевич. Я рад, что Вы все таки смогли сегодня прийти пораньше. У меня для Вас есть важная информация."
    oleg "Здравствуйте, Иван Михайлович. Как только я увидел Ваше ссобщение, я сразу направился сюда."
    boss "Отлично."
    boss "Вчера, как я понимаю, Вы установили на компьютеры всех подозреваемых программу, отслеживающую все действия по передаче данных? (# Изменить? #)"
    oleg "Так точно, проблем с этим у меня практически не возникло."
    boss "Хорошо. Тогда взгляните но это."
    
    with fade
    
    oleg "Это запись с камеры видеонаблюдения?"
    boss "Именно. Вчера в 12 ночи, судя по полученным сведениям, была произведена очередная передача данных."
    boss "И произведена она была с компьютера Сергея."
    boss "Мы решили посмотреть запись с камеры, установленной в офисе, чтобы убедиться в том, что это именно он."
    boss "Однако, как Вы можете видеть, на этой записи видно только как некто подходит к его компьютеру и начинает что-то в нем делать."
    boss "Мы не можем быть на 100 процентов уверены, что это Сергей. Вчера в это время все четверо подозреваемых находились тут из-за скопившейся работы."

    boss "Мы продолжим следить за деятельностью подозреваемых с помощью вашей программы, однака неизвестно, когда будет новая передача."
    boss "Постарайтесь разузнать что-нибудь как можно скорее. Может быть, у кого-нибудь есть алиби."
    oleg "устал писать, пойду спать"


    #outro
    show radik with fade
    show shelby with dissolve
    shelb "La commedia e finita."

    return
