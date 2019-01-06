
label sch_day1_arrival:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ sch_chapter(1, "Предсмертное тепло.")
    play ambience ambience_ext_road_day
    scene black
    "Холод стал сменятся наступающим теплом, а вес моего походного рюкзака перестал ощущаться."
    "Вскоре в глаза хлынул невыносимо яркий жёлтоватый свет, а в воздухе начал витать запах пыли и травы."
    "Хочется лишь зажмуриться и поскорее принять смерть."
    iv "Стоп. Я же сижу!"

    show unblink
    hide black

    $ double_vision_on(bg int_bus)

    "Я жив?!"
    "Губы высохли и совершенно не хотели разлипаться, однако в ноздри попало достаточно пыли, чтобы я отчихался и смог открыть рот, чтобы набрать воздуха."
    ivan "Я - жив?!"

    $ double_vision_off()

    scene bg int_bus
    with flash_red

    "Больно!"
    ivan "Я жив!"
    iv "Видимо, та девочка всё же выполнила своё обещание."
    "Пытаясь встать, я почувствовал, как упираюсь во что-то твёрдое ногой."
    ivan "А вот и рюкзак."
    "Молния легко поддалась и мой вечный спутник показал всё содержимое - от смартфона и плеера, проигрывающего через наушники какой-то старый трек про надежду, до сменной обуви и запасного аккумулятора."
    ivan "Это же... Это же..."
    ivan "Мой рюкзак, когда я был в инситуте!"
    "На мне же было привычное и потёртое худи, казавшееся непривычно большим и такие же широкие джинсы, из-за чего мне пришлось проковырять дополнительную дыру в ремне."
    with fade
    "Наконец-то я решился поднять свою голову выше уровня священного места и подробнее осмотреть салон автобуса."
    ivan "Стоп. Икарус? Рейсовый? В 2027? Шутите?"
    "Заглянув в окно, вопросов стало только больше."
    iv "Лето?!"
    with flash_red
    iv "Нет, я вроде всё ещё не умер. Или уже в раю? Если да, то явно в коммунистическом. И если нет, то... в том же месте в любом случае."
    "Сиденья были абсолютно пустыми и чистыми, а на приборной панели водительского сиденья лежали какие-то резинки с бумажками разных размеров и видов содержания - от каких-то рисунков до текста, больше похожего на дневник."
    iv "Лушче ничего трогать, а выйти из этой душной металлической коробки наконец!"

    scene bg ext_bus with dissolve

    "Решив, что лучше не медлить с этим, я быстро спустился по небольшой жестяной лестнице у входной двери в автобус и оказался на староватом асфальте, в трещинах которого виднелась земля и даже трава."
    iv "Воздух!"
    "Прохладный и свежий, проходящий сквозь мои пальцы и обволакивающий моё лицо ветер позволил мне немного освежиться."
    "Первым делом я достал смартфон и сразу же попытался открыть приложение карт."
    iv "Нет интернета? Чёрт!"
    iv "Ай-ай, Илон, а говорил, что покрытие даже избыточное."
    iv "GPS? Fail."
    iv "Wi-fi. Не знаю зачем, но с нынешними стандартами связи и за пару километров может что-то, да найти."
    iv "FM? Ни одного известного мне канала!"
    ivan "Где я, чёрт возьми?!"

    scene bg ext_road_day with dissolve

    "Хотя бы красиво."
    "Может, вернуться в автобус и поискать что-то у водителя? Или подождать его хотя бы."

    scene bg ext_no_bus with dissolve

    ivan "Какого..."

    play sound sfx_body_bump
    stop ambience

    with fade

    play sound sfx_head_heartbeat

    scene cg d1_uv2 with dissolve

    dreamgirl "Спокойно, спокойно. Слышишь? Всё будет хорошо."

    "Опять приятный голос успокаивает меня."

    ivan "Ты... {nw}Кто?"

    dreamgirl "Неважно. А теперь моргни!"

    show blink
    pause(1)
    scene bg int_bus behind blink
    hide blink
    show unblink

    "Я снова оказался в чёртовом автобусе. И снова у моих ног рюкзак. И снова я непойми как себя чувствую."

    play sound sfx_face_slap

    with flash_red

    "Так лучше. Болезненно, зато работает."

    iv "К чёрту автобус! Быстрее из него!"

    show bg ext_camp_entrance_day with dissolve

    "Повторить мой путь \"проверить связь - оглянуться - не увидеть автобус - потерять сознание\" помогло новое действующее лицо."

    $ renpy.pause(2, hard=True)

    return

label sch_day1_p1_sl_1:
    $ sch_chapter(1, new_day=True)
    $ persistent.sprite_time = "day"
    $ day_time()

    scene bg ext_camp_entrance_day
    show sl normal pioneer
    with dissolve


    "На моём пути, чуть ли не у самых дверей Икаруса, стояла какая-то девушка. Лет восемнадцать, не больше - золотые волосы, по-детски гладкое лицо, яркие голубые глаза и смесь недовольства и заботы одновременно. И это всё в оболочке из синей юбки и белой рубашки с галстуком, как у пионеров."
    iv "Пионерский галстук? Я серьёзно попал в СССР третьего (лишь бы не второго!) миллениума?"
    "Девушка немного удивилась моему внезапному прыжку прямиком из салона, и потому лишь стояла, ожидая от меня хоть слова."

    menu:
        "Поздороваться":
            if sch_hard:
                pass
            else:
                $ pt_sl +=1
            $ pt_ka +=10
            $ list_sch_ch_known.append('sl')
            ivan "Привет."
            sl "Всё-же заговорил! Привет, меня зовут Славя, полное имя Славяна, но все меня называют по короткому имени, и ты тоже так зови."
            $ meet(sl, 'Славя')
            "Девочка, похоже, нервничала, но своё приветствие произнесла чётко, будто ей это не в первой."
            show sl smile pioneer with dspr
            sl "Добро пожаловать в пионерлагерь \"Совёнок!\""
            "Появилась какая-то пауза."
            sl "А как тебя зовут?"
            ivan "Ваня."
            sl "Очень приятно."
            ivan "Взаимно."

        "Да что тебе?":
            if sch_hard:
                $ pt_sl -=1
            else:
                pass
            $ pt_ka -=10
            show sl surprise pioneer with dspr
            sl "Что-то не так?"
            ivan "Нет-нет. Всё просто прекрасно."
            show sl smile pioneer with dspr
            sl "В любом случае меня зовут Славяна, а ты приехал в пионерлагерь \"Совёнок!\""
            $ meet(sl, 'Славя')
            sl "А какое у тебя имя?"
            ivan "Иван."
            sl "Можно я тебя буду Ваней называть?"
            ivan "Мне-то какая разница?"
            sl "Вдруг тебе не нравится."
            ivan "Нет, всё нравится. Тогда тебя я буду звать Славей."
            sl "Договорились."

    ivan "Если ты меня встретила, значит, что ты должна меня куда-то провести."
    sl "Ой, извини, совсем забыла. Видишь ли, ты приехал на смену на две недели позже, поэтому у тебя осталась всего одна неделя, так что тебе придётся быстро войти в темп жизни лагеря, чтобы потратить максимум времени с пользой."
    ivan "Тратить время? Это мы умеем. Так куда идти?"
    sl "Тебе сейчас надо к вожатой - она тебя определит в домик и скажет, что делать, пока ты только приехал. Вот тебе карта."

    show maps_sch('maps/map_avaliable.jpg')
    show maps_sch('/overlays/map_default.png')

    show sl smile2 pioneer:
        xalign 0.5
        easein 0.5 xalign 0.25


    with dissolve

    sl "Смотри. Сейчас заходишь, идёшь прямо, потом с площади поворачиваешь налево и идёшь к дальнему ряду домиков. Дом у вожатой треугольный."

    scene bg ext_camp_entrance_day
    show sl smile pioneer:
        xalign 0.25
        easein 0.5 xalign 0.5

    with dissolve


    menu:
        "Это всё?":
            sl "Да. Теперь ты свободен. Извини, мне нужно бежать. Ещё увидимся!"
            hide sl with dissolve
            iv "Отлично. Наконец-то она меня оставила одного."
            iv "Карта, конечно, странная, но осмотреть стоит."

            show maps_sch('maps/map_avaliable.jpg')
            show maps_sch('/overlays/map_default.png'):

            with dissolve

            with right_lower_zoom #TODO подкорректировать в sch_transform

            iv "Стоп, что?!"
            with flash_red
            iv "Держаться-держаться, не терять сознание!"
            iv "Карта тысяча девятьсот восемьдесят... какого года?"
            "Последняя цифра была размыта так, будто кто-то пролил на край воду."
            iv "Убить бы их за такое обращение!"
            iv "Да и лучше от того, что я знаю, какой примерно на дворе год, мне не стало."
            iv "Даже не двухтысячный! Да я со своими технологичными игрушками и линзами выйду вылетым агентом иностранных спец. служб! И ничего не знаю из истории к тому же."
            ivan "Окей, Гугл. Полная автономия для всех устройств."
            dreamgirl "Принятно, Иван."
            "А между тем всё ещё не очень похожий на человеческий голос для меня незаменим."
            ivan "Окей, Гугл. Режим энергосбережения для всех устройств."
            dreamgirl "Приятно, Иван."
            if not sch_hard:
                "Только пару функций оставить надо - сохранение диалогов"
                if persistent.sch_widget:
                    extend "и показатель отношений людей ко мне."
                    iv "Правда, пока что я ни с кем, кроме Слави, не знаком."
                    # активация виджета
                else:
                    extend "."
            else:
                "Только субтитры к диалогам в линзах. Больше ничего."


        "Какой номер домика у вожатой?":
            $ list_sch_day1_together.append('sl')
            $ pt_pi +=10
            sl "А, извини. У неё домик под номером 17."
            ivan "Хорошо, спасибо."
            sl "Може быть, я сама тебя проведу? К тому же Ольга Дмитриевна сказала, чтобы ты побыстрее добрался до неё."
            $ meet(mt, 'Ольга Дмитриевна')
            ivan "А, ну окей. Я не против."
            sl "Тогда пойдём."
    return

label sch_day1_p1_sl_2:
    # ГГ и Славя доходят до здания клубов, Славе нужно что-то отдать кибернетикам, дело на 5 минут
    menu:
        "Согласиться подождать":
            # ГГ стоит и копает носком асфальт, пока Славя что-то делает в клубах, пото Славя возвращается, и прыжок на sl_3
        "Отказаться":
            # ГГ говорит что не собирается ждать, идёт один, идёт на mi_1

label sch_day1_p1_sl_3:
    # Славя и герой идут по лагерю, ГГ может задать вопросы про то, какие события будут на этой неделе
    # Они доходят до домика вожатой без происшествий
    return


label sch_day1_p1_un_1:
    # ГЛАВУ СЮДА
    #Герой заходит в лагерь сам, первые ахуевания от идеальности ландашафта и (по его мнению) закоса под СССР, видит Клубы
    #Встречает Лену на пути
    menu:
        "Поздороваться":
            $ pt_un +=1
            $ list_sch_ch_known.append('un')
            # Герой здоровается с Леной, Лена уходит в режим патризана, однако говорит ему своё имя
            menu:
                "Продолжить разговор":
                    # Герой продолжает разговор, говорит, что не знает, куда ему идти (хотя у него есть карта), Лена соглашается
                    $ list_sch_day1_together.append('un')

                "Попрощаться":
                    if sch_hard:
                        $ pt_un -=1
                    #Герой прощается с Леной, но как только отойдёт дальше, его Ульянка пугает до усрачки и потери сознания

        "Идти дальше":
            if sch_day1_sl_runaway:
                pass
            else:
                $ pt_pi +=10
                $ pt_ka -=10
            # Герой проходит мимо, по пути просто сказав "привет"

    return

label sch_day1_p1_un_2:
    # Герой разговаривает Лену, она согласилась отвести к вожатой, по пути они могут поболтать около 3-5 минут
    return

label sch_day1_med:
    $ sch_day1_aidpost = True
    # Герой просыпается в медпункте, его встечает Виола
    # Вроде я уже написал этот момент, но твою версию тоже неплохо было бы увидеть
    # Виолетта Церновна просит называть её Виолой
    menu:
        "Виола":
            # Виолка улыбается
            $ pt_pi -=10
            $ pt_ka +=10

        "Виолетта Церновна":
            # Виолка говорит что чувствует себя старой
            $ pt_pi +=10
            $ pt_ka -=10
    #ГГ спрашивает, как он тут вообще оказался, Виолка отвечает, что Лена и Славя
    # Славя стоит на улице, т. к. ей важно знать, как себя чувствует новенький (сама доброта)
    # Лена сидит в медпункте в углу, так как помогает Виолке на пол ставки
    # Виоле нужно рассказать о случившемся вожатой, сам пойти не может, так как кружится голова (пройдёт через час), кто останется с больным?
    jump sch_day1_med_chose

label sch_day1_med_chose:

    menu:
        "А одному нельзя?" if not sch_day1_med_asked_alone:
            $ sch_day1_med_asked_alone = True
            # Виола как раз говорит, что его одного оставлять нельзя, возврат к меню выбора
            jump sch_day1_med_chose

        "Славяну":
            $ pt_sl +=1
            # Оправдывает выбор тем что нужно поблагодарить её
            # заходит Славя, спрашивает, как себя чувствует герой
            # пытается пожалеть, но ГГ оказался суровым мудаком (неожиданно), к тому же он не знаком с ней

            menu:
                "Назвать своё имя":
                    $ pt_sl +=1
                    $ pt_ka +=10
                    # ГГ лично знакомится со Славей, всё норм

                "Отвернуться":
                    $ pt_ka -=10
                    $ pt_wi +=10
                    # ГГ молча отворачивает голову к стене

        "Лену":
            $ pt_un +=1
            # Оправдывает выбор тем что она знает что делать если ему станет хуже
            menu:
                "Отвернуться":
                    # ГГ отворачивается к стене, ничего не происходит
                "Позвать Лену":
                    # ГГ зовёт Лену, чтобы та села на место Виолы, под предлогом того, что он не успел толком поговорить с ней
                    # Спрашивает, как всё было, кто тащил, кто напугал
                    # ГГ просит об одолжении...
                    menu:
                        "Сменить тему":
                            $ pt_ka -=10
                            $ pt_un -=1
                            # Герой "жидко срётся", так как стесняется

                        "Предложить прогулку по лагерю":
                            $ pt_un +=1
                            $ sch_un_walk = 1
                            # Герой таки договаривает, что хочет завтра погулять с ней
                            # Лена говорит, что ей нужно подумать
        #В медпункт входит Виолка и вожатая
        #Ольга Дмитриевна представляется ГГ, говорит что сделает из него пионера, на что получает порцию сарказма
        #ГГ не понимает что происходит, ему выдают зеркало и он ахуевает ещё раз
        #Его будит нашатырь, Виола говорит что акклиматизация и вообще скоро ужин там нужно сказать "Виолетта рассказала, что мне дать"
        return




label sch_day1_p1_mi_1:
    # ГЛАВУ СЮДА
    #Герой прошёл мимо Лены, встречает Мику на площади, она сразу с ним говорит причём так что тот не сразу адаптируется под скорость
    #Мику жалобно просит помощи в уборе колонок в подсобку сцены, а всякой электроники и микрофонии - к ней в клуб
    menu:
        "Согласиться помочь":
            $ pt_mi +=1
            $ pt_pi +=10
            $ pt+ka +=10
            # Герой соглашается, Мику радуется (то что они делали дальше напишешь в другом блоке)

        "Отказаться":
            if not sch_hard:
                pass
            else:
                $ pt_ka -=10
            $ pt_mi -=1
            # ГГ отказывается под предлогом того, что ОД наверняка его ждёт и вообще

    return

label sch_day1_p1_mi_2:
    # Они идут на сцену, ГГ помогает с колонками, Мику просит отнести микрофон в музклуб
    menu:
        "Отнести":
            $ pt_mi +=2
            $ list_sch_day1_together.append('mi')
            # ГГ соглашается ещё раз, относит микрофон, Мику отводит ГГ к вожатой

        "Предложить сходить к вожатой":
            $ list_sch_day1_together.append('mi_alone')
            # ГГ говорит, что итак потратил некоторое время на всё это, вожатая будет ругаться
            # Мику огорчена, но согласна, уходит в музклуб одна, ГГ идёт к вожатой один

label sch_day1_p1_dv:
    # ГЛАВУ СЮДА
    # Если герой отказался помочь Мику или пошёл по лагерю без Слави
    # Приходит Алиса, предлагает ему ахуеть от того, что сейчас ему устроят тёплый приём (варанты штрафного на тебе - любые исхищрения, схема заточена под то, чтобы герой был весь мокрый - будь то просьбы "подождать" под палящим солнцем или облить его водой)
    if persistent.dv_good_sch or persistent.true_sch:
        $ pt_dv +=1
        # игрок получил хорошую или тру концовку, следовательно, этот момент он вспоминает, и обхитряет рыжих, а Алису так и вообще по имени называет, хоть она и не говорила, как её зовут
    elif persistent.dv_reject_sch or persistent.dv_neutral_sch or persistent.dv_transit_good_sch or persistent.dv_bad_sch:
        # игрок получил любую из концовок Алисы, вспоминает ситуацию и обхитряет рыжих
    else:
        # игрок в первый раз играет в игру или не прошёл рут Алисы, следовательно получает по заслугам
        menu:
            "Догнать засранок":
                # герой бежит за Алисой
                if pt_ka >=0:
                    $ pt_dv +=1
                    $ list_sch_day1_together.append('dv')
                    # догоняет Алису прямо у домика вожатой, что делает сам думай

                else:
                    $ list_sch_day1_together.append('dv_alone')
                    # герой выдыхается, Алиса убегает, он щас умрёт нахуй, первый звонок какова хуя у него такая слабая дыхалка внезапно
                    # оказывается внезапно прямо у домика вожатой, к счастью карта осталась цела

            "Оставить их":
                #герой мокнет, обидно-грустно, его встречает Славя, чуть ли не за руку отводит к Вожатой
                $ list_sch_day1_together.append('dv_sl')
    return

label sch_day1_od:
    # ГЛАВУ СЮДА
    # ГГ подходит к домику ОД
    # Общая концепция одинакова - ОД представляется, говорит, что нужно будет его разспределить в домик, а после ужина он зайдёт к вожатой, а затем за постельным бельём и формой на склад
    if 'un' in list_sch_day1_together:
        # Лена прощается с ГГ, ГГ заходит один
    elif 'sl' in list_sch_day1_together:
        # Герой заходит вместе со Славей
    elif 'mi' in list_sch_day1_together:
        # Герой заходит вместе с Мику, вожатая злая так как ГГ пришёл довольно поздно, Мику извиняется, так как это её вина
    elif 'mi_alone' in list_sch_day1_together:
        # Герой заходит один, небольшое опоздание оправдывает тем что помог Мику с колонками
    elif 'dv' in list_sch_day1_together:
        #После акта мести над рыжей, герой говорит, что были некоторые рыжие проблемы по пути
    elif 'dv_sl' in list_sch_day1_together:
        #Славя отводит новичка чуть ли не за руку, события схожи с простым 'sl'
    elif 'dv_alone' in list_sch_day1_together:
        #Уставший герой заходит к вожатой, говорит, что были рыжие проблемы

    # Героя выпсукают, говорят, что есть ещё время до ужина, пусть познакомится с лагерем
    #Вступление к карте

    return

# ДАЛЬШЕ ИДУТ ИВЕНТЫ КАРТЫ

label sch_day1_event_square:
    #герой приходит на площадь, там прибирается Cлавя
    if 'sl' in list_sch_ch_known:
        menu:
            "Уйти":
                if sch_hard:
                    $ pt_sl -=1
                $ pt_ka -=10
                # ГГ уходит

            "Предложить помощь":
                $ pt_sl +=1
                $ pt_ka +=10
                $ sch_day1_mp +=1
                $ sch_day1_sl_cleanuphelp = True
                # ГГ подходит к Славе, предлагает свою помощь
    else:
        # герой видит какую-то прибирающуюся пионерку, уходит
        $ pt_ka -=10

    return

label sch_day1_event_square_visited:
    if sch_day1_sl_cleanuphelp:
        # Площадь чистая, что аж ходить приятно, а Славя куда-то успела уйти, оставив метлы подпирать Генду
    else:
        if 'sl' in list_sch_ch_known:
            $ pt_ka +=10
            "Славя всё ещё убирается. Как-то даже неудобно, что она тут работает, а я просто смотрю."
            # Предлагает Славе помощь, та вежливо отказывается под предлогом что сама почти всё сделала
        else:
            #Девочка всё ещё работает, ГГ уходит
    return

label sch_day1_event_music_club:
    if 'mi' in list_sch_day1_together:
        $ pt_mi +=2
        # Заходит в клуб, болтает с Мику до ужина
    else:
        $ pt_dv +=1
        if 'dv' in list_sch_day1_together:
            # Алиса злая, но потом успокаивается
        elif 'dv_alone' in list_sch_day1_together:
            # Алиса смеётся
        elif 'dv_sl' in list_sch_day1_together:
            # Алиса говорит что Славя уже пригрела его
        # Алиса говорит что Мику скорее всего на сцене
        # Алиса говорит, что Мику нет, на вопрос что Алиса забыла у Мику, отвечает, что профукала струны на гитаре, герой ахуевает
        return

label sch_day1_event_music_club_visited:
    # Никого нет, пора обратно
    return

label sch_day1_event_boat_station:
    # Потенциально подумать
    return

label sch_day1_event_boat_station_visited:
    # Ничего не поменялось, пора уходить
    return

label sch_day1_event_estrade:
    if 'mc' in list_sch_day1_map_1_visited:
        # Герой находит Мику, которая складывает аппаратуру
        menu:
            "Помочь Мику":
                $ pt_mi +=1
                #Предлагает помощь, в итоге он работает, а Мику болтает
            "Уйти":
                $ pt_mi -=1
                $ pt_pi -=10
                $ pt_ka -=10
                # ГГ отказывается
    else:
        # На сцене оказывается пусто, ГГ уходит
    return

label sch_day1_event_square_visited:
    # Эта часть сценария возможна только если герой НЕ помогал
    # Никого нет, пора уходить
    return

label sch_day1_event_library:
    $ list_sch_ch_known.append('mz')
    # Герой заходит в библиотеку, видит Женю, которая спит, потом видит, как Лена выбирает книгу, помогает выбрать
    $ pt_un +=1
    if pt_un >=2:
        $ sch_day1_un_walk = 1
        # предлагает погулять завтра, Лена просит дать подумать
    else:
        # прощается, по пути назад встречает Женю
    return

label sch_day1_event_library_visited:
    # Он тут был, пора валить
    return

label sch_day1_event_clubs:
    if not sch_day1_sl_runaway:
        # Ему сегодня даже внешнего вида клубов хватит, пора валить
    else:
        $ list_sch_ch_known.append('sh')
        # Интересно, кто там
        # Встреча с Шуриком
    return

label sch_day1_event_clubs_visited:
    if not sch_day1_sl_runaway:
        # ТЕМ БОЛЕЕ ХВАТИТ
    else:
        # Не, хватит
    return

label sch_day1_event_beach:
    #Ходит по берегу реки, думает, что за река такая, догадывается насчёт Волги
    # Видит Улю на краю берега
    if pt_sl >=2:
        #Отказывается
    elif not 'us' in list_sch_ch_known:
        #Отказывается, но по-другому
    else:
        #Уля говорит что нужно делать будет
        menu:
            "Согласиться":
                $ pt_us +=1
                $ sch_sabotage = 1
                # Уля рада

            "Отказаться":
                $ pt_us -=1
                $ pt_ka +=10
                $ sch_sabotage = -1
                # Уля показывает язык

            "Пригрозить вожатой":
                $ pt_pi +=10
                $ pt_us -=1
                $ pt_ka -=10
                $ sch_sabotage = -1
                # Уля злая и вообще, ТЫ, АНОН, killjoy!

    return

label sch_day1_event_dining:
    # Герой подходит, говорит, что скоро ужин
    # Видит как за Элом бежит Алиса
    if pt_wi >=20:
        menu:
            "Бежать за Электроником":
                $ pt_wi -=10
                # Побег, в итоге встреча с Элом, и проход к столовой путём ныкания
            "Остаться стоять":
                $ pt_dv +=1
                # Герой продолжает стоять, Алиса злая но не из-за ГГ
            "Уйти в сторону и подождать горн":
                # ГГ отходит, видит, как Алисхен выдаёт живительные пиздюли

    return


# КОНЕЦ ДОВОЖАТЬЯ


label sch_day1_dinner:
    if sch_day1_aidpost:
        "Горн на ужин прозвучал уже трижды, и, к счастью, Виола дала помыть мне руки у неё в медпункте, так что я быстро оказался в переполненной народом столовой, около которой, похоже, ночуют."
    else:
        iv "Спасибо вожатой, что хоть сказала, что надо руки мыть."
        iv "Лично проверит. Целый один раз."
        "Около входа в столовую стояла целая толпа, ожидающая, пока кто-то откроет дверь в Храм ЧревоугодияTM, спонсируемый самим Дьяволом."
        "Мне кое-как удалось протиснуться вперед младших отрядов и начать высматривать себе пластковую табуретку и стол на ближайшие пять-десять минут."
    ivan "Класс. Хороших мест нет, свободных - тем более."
    iv "Похоже, что мне ещё повезло - часть старшиъ отрядов ждёт свою порцию на улице."
    # Я тут немного поработал, но забил - суть ты понял - столовая забита, вариантов сесть  несколько:
    # Свободны были только несколько мест у первого и второго отряда (первый самый малочисленный, а со вторым повезло)
    menu:
        "Сесть с Ульяной" if 'us' in list_sch_ch_known:
            # Садится с Ульяной, она по классике жанра пиздит котлетос
                menu:
                    "Потребовать котлету" if pt_wi >=20: # Только если у героя есть хоть немного очков Воли
                        $ pt_us +=1
                        $ pt_wi +=10
                        $ pt_ka +=10
                        #ГГ требует котлету
                    "Смириться":
                        $ pt_wi -=10
                        # ГГ мечтает разобраться с ней после ужина
                    "Пожелать добра":
                        $ pt_pi -=10
                        $ pt_ka -=10
                        $ pt_us -=5
                        $ sch_day1_hungry = True
                        if sch_sabotage == 1:
                            $ sch_sabotage = -20
                        # ГГ желает ей "добра" в самой матерной форме, возмонжо, завуалировано, и уходит из столовой под ахеревание и возможно шок из-за такого словарного запаса ГГ, хз, там может и ОД прийти спросить что произошло, главное - герой уходит
                        return
                # Ульянка говорит герою не грустить (если тот не пожелал ей смерти) и приносит новую тарелку по классике жанра со сколопендрой, герой в ахуе
                # Уля убегает
                menu:
                    "Оставить её":
                        $ pt_sl +=1
                        if not sch_hard:
                            $ pt_pi +=10
                        # Герой оставляет Улю, хочет сходить заменить порцию, но места предательски занимают и он решает уйти, но тут приходит help со стороны Слави, которая кормит ГГ
                    "Сбежит!":
                        $ sch_day1_hungry = True
                        # Герой включает режим флеша и бежит её догонять
                        # Чёто тело другое и Ульянка не особо догоняется, зато в поле зрения появляется отличный бросаемый элемент - камень
                        # Ну что, играть в блинчики с живыми людьми будем?
                        menu:
                            "Кинуть камень":
                                $ sch_sabotage = -2
                                # Удар в яблочко меж рёбер, Уля наворачивается на красивую землю
                            "Не бросать":
                                # Герой не бросает камень
                                if sch_sabotage == 1:
                                    # Уля кричит в след, что герой принят к саботажу
                                    $ sch_sabotage = 2
                                else:
                                    # Уля убегает показывая язык



        "Сесть с Рыжей" if not 'us' in list_sch_ch_known:
            # Садится с Рыжей, она его особо не бесит, так как только догадывается, что он новенький

        "Сесть одному":
            # Герой садится один, всё просто и быстро должно

        "Сесть с Мику" if 'mi' in list_sch_ch_known:
            $ pt_mi +=1
            $ list_sch_day1_supper.append('mi')
            # ГГ садится к Мику, та его заговаривает, благодарит за помощь, предлагает заглянуть на причал после ужина

        "Сесть с Алисой" if 'dv' in list_sch_ch_known and pt_wi >=20 and pt_dv >=2:
            $ pt_dv +=1
            if persistent.dv_reject_sch or persistent.dv_neutral_sch or persistent.dv_transit_good_sch or persistent.dv_bad_sch or persistent.dv_good_sch or persistent.true_sch:
                # Алиса спрашивает, как он узнал, а ГГ говорит с ней как с старой знакомой
            else:
                # ГГ садится к Алисе с опаской, но та лишь шутит над ним один раз и всё

        "Сесть с Леной" if 'un' in list_sch_ch_known:
            $ pt_un +=1
            $ list_sch_day1_supper.append('un')
            # ГГ спокойно ужинает с Леной, та может что-то о себе рассказать из небольших фактов, она любит сидеть на скамейке на площади по вечерам


        return

    # Герой выходит из столовой, снова карта


label sch_day1_aftersupper:
    # Фон столовая вечером
    if sch_day1_hungry and sch_sabotage != 2 or sch_sabotage != 20:
        "К чёрту мелкую."
        if sch_sabotage == -2:
            "Противный ребёнок, который считает, что ему всё можно - а камешком промеж рёбер не хочешь?"

        else:
            "Противный ребёнок, который считает, что ему всё можно - да пошла бы она."


    elif sch_day1_hungry:
        "С мелкой, конечно, может быть и интересно, но ведёт она себя крайне опасно. С ней нужно тысячу раз быть осторожнее, ибо что случись - на меня вину свалит, прямо вижу."

    else:
        iv "Не считая того, что столовая просто не успевает обслужить 80 голодных душ, еда тут вполне сносная."

    "Я посмотрел на часы."
    iv "Ещё часа так три до отбоя, а вожатая мне сказала, чтобы я постельное бельё принёс к ней в дом, пока она меня не определила."
    iv "Добро пожаловать в инновационную Life-Action RPG \"Пионерия\". Лимитированная версия 1980-х для людей и кошек старше 14-и лет."
    iv "Не то, чтобы я был против, однако нести придётся дважды, сначала в домик вожатой, потом в свой."
    # фон склада
    ""
