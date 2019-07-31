label dr_day1_map_1_1_event_clubs:
    scene ext_clubs_day with dissolve
    "К \"Клубам\" я пошёл из чистейшей скуки. Всё-таки из-за неприятного инцидента днём мне не удалось насладиться шумом статического электричества и рассмотреть трещины на ступеньках, ещё несколько часов назад закрытыми двумя противоборствующими парами обуви."
    "Оттуда вышел парень моего возраста и роста, и я приметил сразу килотонны энтузиазма в его глазах, которого, казалось, ему не занимать."
    show el normal pioneer with dissolve

    ivan "Эм… Привет."
    "В растерянности сказал я первое, что пришло в голову."

    show el smile pioneer with dspr

    dr_el "О, привет! Ты, наверное, новенький!"
    "Выпалил блондин с кудрями и ну очень гладким лицом. Сразу видно - не гуманитарий. Мой знакомый назвал бы его продавцом мороженного."
    dr_el "Меня Серёжей зовут! Но лучше называй Электроником или Сыроежкой, мне так привычнее."
    "Сразу он выпалил и приветствие, и имя, и уже перешёл на дружескую ногу."
    th "Стесняется, что-ли?"
    menu:
        ivan "Ладно, "
        "Сыроежка":
            $ dr_meet('el', "Сыроежка")
            extend "Сыроежка."
        "Электроник":
            $ dr_meet('el', 'Электроник')
            extend "Эл. Можно Элом?"
            dr_el "Да, конечно! Так даже лучше!"
            ivan "Отлично."
        "Серёжа":
            $ dr_meet('el', 'Электроник')
            show el upset pioneer with dspr
            dr_el "Лучше Электроником всё же."
            ivan "Как хочешь. Будешь Элом."
    ivan "Я Ваня. Можешь называть Ваней, можешь Иваном, можешь Ванькой."
    "Вернул ему шпильку я."
    show el upset pioneer with dspr
    dr_el "Хорошо, Вань."
    "Тут он задумался и, похоже, выдал своё лучшее предложение. One-time offer!"
    dr_el "Хочешь, я тебя к вожатой проведу? А то Алиска с Улей не дремлют, а со мной они тебя штрафовать не будут."
    ivan "Это ещё кто кого оштрафует. Но за предупреждение спасибо."
    show el normal pioneer with dissolve
    dr_el "Да не за что. Ну я пошёл? Мне ещё с Шуриком робота собирать."
    "Сам пристал ко мне ведь, а теперь разрешения спрашивает."
    ivan "Угу. Пока."
    "Местный инженер спрятался за дверьми клуба, откуда начали доноситься звуки перфоратора."
    dr_th "Немного рассеянный, но, похоже, довольно толковый. Если что, буду знать, к кому со схемами лезть. Хоть он и человек девяностых, но простую зарядку придумать поможет."
    "Заключил я."
    dr_th "Вряд ли я тут кого-то ещё встречу, если ко мне паломничество не откроют."
    "С этой мыслью я побрёл к предпологаемому местонахождению склада."
    scene bg ext_warehouse_day_dr with dissolve
    "Дверь была открыта."
    return


label dr_day1_map_1_1_event_square:
    scene ext_square_day with dissolve
    dr_th "А теперь можно выдохнуть и вспомнить, что меня переполняют гормоны."
    dr_th "А потому ничего более эффективного, кроме сублимации мыслей, я придумать не смог и начал пытаться складировать имеющуюся информацию."
    dr_th "Лучше от того, что я знаю, какой примерно на дворе год, мне не стало."
    dr_th "Даже не двухтысячный! Да я со своими технологичными игрушками и линзами выйду вылитым агентом иностранных спец. служб!"
    dr_th "Потом ещё не мой мир."
    dr_th "А он не мой хотя бы из-за пионерии в 18!"
    dr_th "Что бы ещё добавить в копилку странностей? Ну, генсек мне явно незнаком, я нахожусь во времени незадолго до распада СССР - хотя перестройкой здесь и не пахнет - всё цветёт и радуется и напевает гимн Союза."
    dr_th "Ну, в значке ВЛКСМ я разницы не увидел - ромб и ромб, у пионерок дядюшка Ленин тот же. Хотя, мне казалось, что он смотрит не вправо, а влево."
    dr_th "Ладно, и это с натяжкой с котёл мыслей закинем."
    show blink
    pause(2)
    "Итак. Что мы имеем? Я, вроде как ещё Иван, сел в рейсовый Рено, чтобы проснуться омолодевшим (!) в рейсовом Икарусе (!) летом ближе к концу XX (!) века и быть окружённым совершеннолетними (!!!) пионерками."
    "Восклицательные знаки кончились быстрее, чем я мог предпологать, и выделять увеличивающееся количество несосытковок с учебниками по истории я не мог."
    dr_th "Кстати, о книгах. Здесь же библиотека есть! Может, сходить? {w=1.0} Нет, не стоит."
    dr_th "За полчаса я вряд ли успею много начитать, а если библиотека настоящая, то мне придётся встретиться с библиотекарем и сортировать марксистко-коммунистские пособия по превращению капиталистического ада в рай в железном шалаше."
    dr_th "Да и времени, по ощущениям, прошло немало."
    hide blink
    show unblink
    "Тяжёлые веки после недолгого сна поднимались неохотно."
    "Вернув к себе все свои рецепторы и органы ощущения окружающей Вселенной, я почувствовал движение мелкого насекомого прямо у меня на ноге."
    "Этим насекомым оказался кузнечик, которого я аккуратно и спроводил на скамейку, сразу почувствовав недовольный взгляд, протыкающий мне спину."
    show us grin sport with dissolve
    "Обладателя этого взгляда звать не пришлось: не опять, а снова представительница женского пола размеров поменьше остальных обитателей выбежала сразу и встала передо мной."
    "Первое отличие, кроме, естественно, роста - это другая одежда. Спортивная, каждодневная, удобная - вот моё описание из трёх слов. Футболка с надписью \"СССР\" в цвета флага, короткие шорты и сандалии с носками."
    "Мелкая рыжая, как я её сразу же окрестил в своей голове, имела совершенно неественно яркие {i}красные{/i} волосы и синие бегающие во все стороны наглые глаза."
    "Эти же глаза таращились на меня, как на представителя иного мира, и это было настолько точно, что мой ответный взгляд был почти полностью равнодушным."
    dr_th "Наверное, из младших отрядов девочка. Почему так на меня смотрит только?"
    show us surp1 sport with dspr
    dr_us "Ты не испугался?"
    "Спросила она с таким удивлением, будто у неё перед глазами пронеслось йети."
    ivan "Не испугался чего?"
    dr_us "Кузнечика!"
    "Протараторила она."
    ivan "А с чего бы мне его пугаться?"
    dr_us "Ну так тиша визжит при одном их виде, а ты просто смахнул так, будто..."
    ivan "Будто что?"
    dr_us "Будто соринку!"
    show us smile sport with dspr
    us "Будем дружить? Меня Ульяна зовут!"
    $ meet('dr_us', 'Ульяна')
    ivan "А по какой такой причине дружить? Я дружбой не разбрасываюсь."
    "Ответ мой был ответом не мальчика, а мужчины!"
    us "А просто так!"
    ivan "Ах, ну просто так. Тогда согласен."
    show us surp1 sport with dspr
    us "Правда?"
    ivan "Конечно! Только трудовой договор подпиши о назначении в должность друга."
    us "Договор? Так ещё и трудиться? Какой классный из тебя друг... А как тебя зовут?"
    ivan "Никто."
    show surp2 sport with dspr
    us "Если ты никто, то и звать тебя Никак! Очень приятно, Никак! Давай без договора дружить!"
    ivan "Никак не будет дружить без договора, ему это не выгодно."
    show us laugh2 sport with dspr
    us "Ну и вредина!"
    "Характер у мелкой был отходчивый - обижаться она совсем не..."
    hide us with flash_red
    ivan "Ай-й-й!"
    "Когда я поднялся, вокруг не было ни души."
    dr_th "И ведь, зараза, знает, куда бить!"
    "И, прихрамывая первый десяток шагов, я отправился к складу."
    scene bg ext_warehouse_day_dr with dissolve
    "Дверь была открыта."
    return

label dr_day1_map_1_1_event_musclub:
    scene bg ext_musclub_day with dissolve # Точно это название?
    play ambience ambience_camp_center_day fadein 1
    "Меня с самого первого момента интересовал музыкальный клуб."
    "Раз ему выделено целое здание на отшибе, то он должен ведь чем-то выделяться, да?"
    "И, буду честен, оно выделялось!"
    "Огромные окна, завешанные лёгкими шторами, терраса, отъедающая целый скат крыши и новая краска."
    "Дом был новым и за ним явно присматривали всё время - явно в обмен на игнорирование всего остального лагеря."
    "Некая достопримечательность."
    dr_th "Интересно, а Лена тут часто бывает?"
    "Имя фиолетововолосой девочки всплыло сразу - так же далеко от основного мира, и тоже дом для творчества."
    # здесь мелодия
    $ volume('music', 0.4)
    scene bg ext_musclub_day:
        ease 1.0 zoom 1.2 xalign 0.6 yalign 0.5
    "Я неспешно поднялся на террасу и сразу же услышал какую-то мелодию на {w=0.2}клавишных - различать фортепьяны, пианины и прочие бобины я так и не научился. Хотя и не горел никогда желанием. Играет - играет. Красиво - красиво. И всё."
    menu:
        "Зайти внутрь":
            dr_th "Вряд ли кто-то переодевается в музыкальном клубе, играя на фортепиано, поэтому, думаю, никто не разозлится, если я аккуратно открою дверь и посмотрю на игру со стороны."
            scene bg int_musclub_day with dissolve
            stop ambience fadeout 3
            play ambience ambience_music_club_day fadein 3
            $ volume('music', 1.0)
            if not dr_tmp_d1_sl_after:
                "В этот раз дверь закрылась очень тихо и щелчка механизма было совсем не слышно."
            else:
                "Дверь я закрыл с особой осторожностью, чтобы не отвлечь музыканта."
            "Войдя внутрь, у меня сложилось впечатление, что чертежи комнат и самого дома были вдохновлены золотым сечением."
            "От кажущегося простора меня ожидала только одна комната - ровно {i}половина второй половины крыши{/i} - но и она, освещённая ярким солнцем, выглядела прекрасно."
            "Стены были завешаны картинами композиторов, чьи имена я бы не вспомнил и под угрозой расправы. На полке лежало несколько книг, названия которых я прочитать не смог - кто-то как будто специально старался прикрыть название."
            "Никакой пыли на горизонтальных поверхностях замечено не было, паркет сиял, а общая живость вида была образована не только сидящей за массивным чёрным лакированным монстром девушкой, но и свежими следами влажной тряпки на доске и нарисованным на ней же нотным станом."
            "Остальная тонна инструментов была на видном месте - но убрана куда-то в угол, подальше, и стояла небрежно - одна из гитар вообще имела единственную опору в виде хлипкой тумбочки со скользким краем, с которого бедный инструмент так и норовил соскользнуть."
            "Мешала ему колонка - отставленная от второго собрата в совершенно другой угол, да так, что я не сразу заметил пару."
            "Тромбон здесь был изгоем в квадрате - он лежал на одном из барабанов в полуразобранном состоянии и ощутимыми вмятинами."
            dr_th "Как на таких инструментах вообще играют?"
            # тут апплодисменты из одного человека
            "Я наслаждался игрой ещё добрые несколько минут и, когда были нажаты последние ноты, заапплодировал."
            stop music fadeout 3
            ivan "Отлично сыграла!"
            show mi shy pioneer with dissolve
            "Наконец, девушка поднялась, встала передо мной и начала пристально смотреть на меня."
            dr_mi "Спасибо. А как долго ты тут находишься?"
            ivan "Буквально только что зашёл. Извини, если потревожил."
            show mi surprise pioneer with dspr
            dr_mi "Нет-нет, что ты, бака! Я всегда рада, когда кто-то ко мне в клуб приходит."
            dr_th "\"Бака\". Значит, мне не просто так показалось, что у неё лицо не европейское."
            show mi sad pioneer with dspr
            ivan "А к тебе редко приходят? С виду кажется, что тут очень даже большие перспективы провести получше время."
            dr_mi "Вообще, да. Ты первый, кроме Ольги Дмитриевны-сан , кто пришёл ко мне за последние три дня. И то, только потому что только прибыл."
            ivan "Тут ты права, да. Но мне никто не будет запрещать приходить сюда позже."
            show mi grin pioneer with dissolve
            dr_mi "А ты будешь?"
            "Лицо японки мгновенно преобразилось."
            ivan "Буду, как только узнаю, как тебя зовут. Меня, вот, Ваней прозвали."
            dr_mi "А меня Мику зовут! Правда-правда! У меня мама - японка, а папа - русский инженер! Многие сначала не верили мне, но потом я привыкла к тому, что тут все такие подозрительные. Ульянка вот до сих пор думает, что я притворяюсь. А я всегда говорю правду, честно-честно!" # По предкам - Ничо не поделать, так оригинальная игра сказала
            $ dr_meet('dr_mi', 'Мику')
            dr_th "После второго предложения ничего не разобрал. Однако говорить про отцовскую профессию с {i}такой{/i} интонацией - дорогого стоит."
            ivan "Очень приятно. Будем знакомы. А ты, видимо, любишь своего отца."
            dr_mi "Конечно, люблю! Если бы не он, я бы так и жила в Японии и говорила бы на японском! А тут, видишь, в Союзе живу, в лагерь попала! Настоящая пионерка! С галстуком!"
            dr_ivan "Гайдзинам не понять, да?"
            show mi surprise pioneer with dspr
            "Циановая девочка удивилась слову из знакомого с рождения языка - и только сейчас я понял, что у неё волосы самого настоящего бирюзового цвета, настолько они хорошо вливались в общий образ."
            dr_mi "Ой, а ты японский знаешь?"
            ivan "Два с половиной слова, если честно."
            dr_th "Из интрнета всего понемногу."
            show mi grin pioneer with dspr
            dr_mi "Классно! А какие ещё?"
            dr_th "Хентай, эччи, ксо, омае ва моу шиндеру и нани, но тебе лучше не знать об этом."
            ivan "Ну, если не ошибаюсь, то ты - хафу."
            dr_mi "Да, верно! Значит, что-то да знаешь!"
            show mi upset pioneer with dspr
            "Разговор совершенно неожиданно и для меня, и для Мику, пришёл в тупик."
            ivan "А можно вопрос?"
            show mi normal pioneer with dspr
            dr_mi "Конечно, задавай."
            ivan "А кто эти композиторы на картинах?"
            dr_mi "Какие?"
            ivan "Ну, прямо над... этим вот. Боюсь соврать, что это. Пианино?"
            show mi laugh pioneer with dspr
            "Мику засмеялась. Ну и ладно - больно то хотелось знать."
            dr_mi "Это рояль, если что. Ты обиделся? Я не над тобой смеюсь, а над ситуацией!"
            show mi grin pioneer with dspr
            extend "Ты, кстати, первый, кто спросил, что это за инструмент."
            ivan "Остальные ошибались?"
            dr_mi "Нет, говорили правильно."
            dr_th "Меня унизили? Определённо. Но есть подозрение, что она даже не поняла этого."
            "Мику наконец посмотрела на произведения искусства, потом задумалась, ещё раз посмотрела и повернула голову обратно ко мне, где-то успев обзавестись красной краской."
            show mi shy pioneer with dspr
            dr_mi "А я... Я не знаю, если честно. Они тут висели, когда я приехала в лагерь и даже не смотрела на них. Мне куда интереснее на инструменты смотреть, а ещё лучше - играть на них."
            ivan "Ну хоть моя душа чиста."
            show mi smile pioneer with dspr
            dr_mi "Кстати, об инструментах. А ты умеешь на чём-нибудь играть? Только не стесняйся!"
            menu:
                "Когда-то давно":
                    $ dr_mi_op +=1
                    $ dr_ka +=10
                    dr_mi "Правда? А хочешь в мой клуб записаться? Сможешь приходить и играть, когда захочешь!"
                "Не умею":
                    dr_mi "А хочешь, научу? Могу на чём угодно научить играть! Хочешь, на рояле? Или на гитаре?"
            ivan "А я могу подумать?" # Какой удачный ответ
            dr_mi "До завтра точно! С обходным листом придёшь ко мне, я ждать буду!"
            ivan "Хорошо. Договорились. Зайду завтра."
            "И настенные часы, отскипевшие переход на новую минуту, напомнили, что в музклуб пришёл, чтобы скоротать намного меньшее количество времени.. Прошло почти полчаса и, представляя педантичность Слави, могу предположить, что она уже ждёт меня там."
            ivan "Ой, Мику, мне бежать надо, меня Славя на складе ждёт!"
            dr_mi "Хорошо. Придёшь ещё? Я сегодня буду после ужина играть. А ещё Лена придёт, если тебе интересно. Ты бы знал, как она красиво рисует! Прямо очень-очень! Но она мне почему-то сегодня так ничего и не показала, и потому я предложила ей поиграть, чтобы придать ей вдохновения."
            ivan "Приду, приду. Всё, пока!"
            "Я наконец её перебил и смог попрощаться."
            $ dr_day1_mi_musclub_promise = True
            scene bg ext_musclub_day with dissolve
            "Мисс-музклуб, оказывается, личность крайне интересная, но тараторит так, что переговорить её невозможно, а перебивать - обязательно."
        "Не мешать музыканту":
            $ dr_day1_mi_musclub_leave = True
            "Я послушал ещё несколько минут, пока мелодия не пришла к своему завершению и, подумав, что делать здесь больше нечего, встал с перил, оттряхнулся и вернулся на дорожку."
            scene bg ext_musclub_day with dissolve
    "Я пошёл прочь от музклуба и поторопился к складу"
    scene bg ext_houses_day with dissolve
    extend "через домики, "
    scene bg ext_square_day with dissolve
    extend "пересёк площадь "
    scene bg ext_warehouse_day_dr with dissolve
    extend "и наконец добрался до склада. Дверь была открыта."
    return
