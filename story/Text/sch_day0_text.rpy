label sch_day0_prehistory_part_1:
    $ persistent.sprite_time = 'night'
    $ prolog_time()
    $ name_sch('Я')
    $ sch_chapter(0, "Жить в твоей голове.")

    scene black
    stop music fadeout 1
    play music track_01 fadein 3
    $ volume('music', 0.3)
    # фон снега
    #play sound grochot
    $ volume('music', 0.5)
    pause(0.1)
    $ volume('music', 0.6)
    pause(0.1)
    $ volume('music', 0.7)
    pause(0.1)
    $ volume('music', 0.8)
    pause(0.1)
    $ volume('music', 1.0)


    scene bg speaker_room
    show cg uvao_d0
    with dissolve

    uv "Ради меня. Я прошу тебя. Ты должен поехать…"

    pause(0.5)

    iv "Ну... {w=0.5}началось. Каждый день повторяется с самого начала, копирует предыдущий и делится надвое, как клетки в любом живом организме. Мои сны – нечёткая зашакаленная гифка. Мои мысли – на вечном реверсе. И нет выхода из Лабиринта Фавна."
    iv "Забавно."
    uv "Бесполезно игнорировать меня. Я буду с тобой до тех пор, пока все не вернется на свои места, пока не будет так, как прежде. Прошу, ты должен меня услышать. Не бросай меня, ты мне нужен. Сейчас - и навсегда."
    "В тихом омуте без света,\nВ заповеднике миров,\nТы найдешь исток ответа\nСвоих страшных черных {w}Снов."
    stop music fadeout 1
    play music track_02 fadein 3

    uv "Ради меня, прошу, не бросай."
    iv "Да вы издеваетесь."
    "Люблю-Ненавижу, от томного я до сладкого ты, от симпатии до ненависти, от жизни до смерти… Черное-Белое. Полутона. Что за детские игры. Так говорят только в драматических фильмах. В дешевых мелодрамах, вся глубокая мораль и смысл которых заключены исключительно в пафосном названии киноленты."
    iv "Мда."
    with fade
    "Один раз я случайно посмотрел такой фильм. Спасибо, мне хватило. Жанр кино для меня с того момента мертв. По крайней мере мелодрамы – это не искусство. Не для гурманов и истинных ценителей \"прекрасного-вечного-великого\"."
    "Эти фильмы для веганов. В них нет мяса и особого, сочного вкуса, которым пропитаны работы Тарантино или Тарковского."
    "И, естественно, каждому своё. Вегану - мясо, мясоеду - салат."

    stop music fadeout 1
    play music track_03 fadein 3
    with fade

    uv "Ты слышишь меня? Это очень важно. Помни, я все равно рядом с тобой. Я – твой единственный вопрос и твой единственный ответ, который начинается там, где заканчивается полуденный путь человечества."
    "Что это? Намёк на ночную встречу или мой воспалённый мозг опять придумывает очередной аттракцион летящей во все стороны спермы?"
    uv "За синим небом лежит белый Бог. Падает с неба кометой холодных льдов. После воды и солнца, после снега и жасмина мы с тобой встретимся. И на этот раз навсегда."
    "Случайные встречи случайны навсегда. До конца времён. До тепловой смерти - чувств или вселенной?"
    "Когда температура тела у обоих влюблённых сравняется до привычных докторских тридцати шести и шести или когда молекулы отдадут всю энергию?"
    iv "Черт возьми, какая же это пошлая и избитая трагедия. Французский флер и мишура. Говорить и размышлять по-гамлетовски в XXI веке – все равно, что проходить капчу за деньги. Вроде прикольно, но бессмысленно."
    iv "Самое забавное в этом то, что каждый раз я все больше разочаровываюсь в самом себе. Говорят, что сны – это отражение скрытых подсознательных мыслей человека. Неужели все мои скрытые мысли – это тайное желание стать главным героем дешевой французской мелодрамы?"
    "Мой мозг – мой единственный враг."

    scene black with fade

    $ renpy.pause(1.5, hard=True)

    # фон
    stop music fadeout 1
    play music track_04 fadein 3

    "Как же хочется спать. Сил моих больше нет."
    "А вместе с этим нет совершенно никакого спокойствия. В очередной раз. В очередную бессонную ночь."
    "Все, что мне нужно на данный момент, так это спокойный, нормальный, восьмичасовой сон без романтических реплик и страстных откровенно эротических сцен в моей голове."
    "Честное слово."
    iv "Разве я так много прошу?"
    scene anim prolog2 with dissolve

    stop music fadeout 1
    play music track_05 fadein 3

    "Здорово, наверное, когда тебе снятся девочки в купальниках и теплый песок белого пляжа, омываемого солеными волнами лазурного моря."
    iv "Красота..."
    show blink
    stop music fadeout 1
    scene black behind blink
    hide blink
    scene bg ext_camp_entrance_day_water
    scene cg uvao_d0

     with fade

    stop music fadeout 1
    play music track_06 fadein 3

    "Но мне о таком можно только мечтать."
    "Потому что каждую ночь я ощущаю себя на краю пропасти. Я задыхаюсь, в глазах темнеет и передо мной раскрывается глубокая, белая бездна глубиной в целую вечность."
    "Надо мной стоит девочка в коричневом платье, а позади нее в размытом боке виднеются чугунные ворота пионерского лагеря. Она смотрит на меня своими пронзительно-глубокими, выразительными глазами, полными невыразимой тоски и боли."
    "Она зовет меня к себе. Протягивает мне свою руку."
    "Я пытаюсь схватиться за нее, но безуспешно. Ее неуловимый образ рассыпается, стоит мне только прикоснуться к ее ладоням."
    hide cg uvao_d0
    with Dissolve(5.0)

    scene bg anim prolog2 with dissolve
    "Люди смотрят на людей. А в глазах они видят только пустоту. И как-то больно становится от того, что Эта боль живет где-то глубоко, в области сердца. Под коркой мозга, на кончиках колючих пальцев."


    stop music fadeout 1
    play music track_07 fadein 3

    iv "Прости. Прощай."
    show uvao dontlike far with dissolve
    "Я снова все испортил. Привыкай, моя дорогая. Это мое призвание – ломать все, что мне дорого."
    "Я пойду с тобой, когда солнце взойдет на западе и сядет на востоке, когда зимой будет цвести сакура, когда Шекспира перестанут считать гением английской литературы."
    "Тридцать второго числа тринадцатого месяца мы встретимся с тобой, и этот день я никогда не забуду."
    "В этот день я буду кричать о помощи, рвать на себе волосы, сдирать с себя кожу, лезть на люстру в тщетных попытках спастись от разверзающейся под моими ногами бездны, которая открывает моему разуму сакральные тайны хрустального космоса."
    # фон площадь лагерь дождь
    "И мы устроим пир на костях. Холодная вода прольется с неба, смоет горизонты, затопит дома, выломает мачты рассохшихся кораблей, опрокинет наш Городок в Бутылке."
    # фон пропасть
    "А я буду стоять над бездной. Как режиссер, как дирижер, как великий гений последнего мира, погибающего во тьме. И буду слушать великую симфонию ломающихся мачт, трещащих канатов и соленых брызг синего моря. Симфония разрушения - это та песня, с которой Бог создавал этот безумный мир."

    stop music fadeout 1
    play music track_08 fadein 3

    "Я вижу Бар. {w}Стеклянные бутылки, щербатые глиняные стаканы, до краев наполненные соленым и пенным пивом."
    "Я вижу сонного сомелье, задремавшего в углу помещения, облокотившегося на барную стойку с дымящейся сигарой во рту."
    "Я вижу свет, отражающийся от хрустальных бокалов, преломляющийся тонкой полоской красной радуги, разливающейся из бутылки дорогого вина." # Если истина в вине, она во мне! Хоть мы и звёзды, но морские - живём на дне. Полупустой бутылки из-под каберне, полупустой бутылки из-под каберне.
    "Под потолком лениво вертится лопасть сломанного вентилятора, который, казалось, был оторванным пропейлером от кукурузника, который нашел свое последние пристанище в полях бескрайнего космоса."
    "Я говорю с усатым барменом, молодым мужчиной лет тридцати пяти, с глубоким, проницательным взглядом, в котором я вижу лица. {w}Лица мертвых людей, карты, деньги, Вегас, казино, блестящие вывески, сломанный пистолет, заряженный холостыми патронами."
    play sound vystrel
    "Выстрел."
    with vpunch
    "Побег, плащ за спиной разрывает пространство холодных улиц, свистит ветер, дождь косыми, острыми каплями режет кожу лица, а он стоит посередине дороги, весь мокрый, злой, уставший, облокотившись на фонарный столб, курит последнюю сигарету, мнет окурок, бросает его в глубокую лужу, в которой отражается одинокая луна."
    # фон?
    "Сноп искр взмывает ввысь и тут же разлетается холодным огоньком беспечных мотыльков."
    "Еще один шаг - и он увидит вечность. {w}Сигарета в пачке, окурок, выстрел, сжатые кулаки."
    "Проезжая часть. Он делает этот шаг, падает, запутываясь в полах своего плаща, поджимает воротник к лицу, закрывается от ветра."
    "Лязг тормозов, выстрел по колесам, звон разбитого стекла…"
    $ sch_name("Нуар")
    ivan "Да кто ты такой!"
    $ sch_name("Я")
    # фильтр серый
    "Пауза. Карты, деньги, два ствола."
    "Окурок в холодной луже. В маленьком океане бумажного города."
    "Вегас не верит слезам."
    "И этот человек кричит в мое лицо, хватает мои щеки своими пальцами-щупальцами, тащит к себе, ударяя мою голову об дубовую поверхность лакированного стола, проводит моей физиономией по кирпичной стене, сметая своим локтем стоящие на полках бутылки игристого, красного, полусладкого и тяжелого."
    "Его глаза дышат кровью, его ноздри нервно раздуваются в бешеном порыве. Он бросается ко мне с распростертыми объятиями и вливает в мое горло холодный, стеклянный спирт."
    # виньетирование

    show anim prolog2
    with fade
    "В глазах темнеет. Уже нет ни бармена, ни таинственного незнакомца в черном пальто."
    play sound bang
    "Звон в ушах, как вата. Сахарная. Из луна-парка."
    "Есть только я и бесконечная пропасть, которая отделяет мой разум от бесконечного путешествия длиной в целую вечность."
    stop sound
    "Мой разум - луна-парк. Подходи. Играй. Катайся. Тыркай, тюкай, закрывай, ломай, рисуй - я стерплю все."
    $ renpy.pause(3, hard=True)
    "Я тоже не верю слезам."
    scene black with fade
    "И вот бар остается позади. Низкий, разбитый, с грубой неоновой вывеской над чугунной дверью, с приглушенной шипящей музыкой за гипсокартонной стеной, с заколоченными окнами и с закрытой уборной."
    "Пропасть – не цель и даже не средство. Вся моя жизнь - падение."
    "Порой я себя ощущаю Гетте своего времени и заключенным палаты номер шесть из одноименного рассказа Чехова в одном флаконе, и все из-за того, что каждый вечер я создаю себя заново. Я зациклен, поставлен на репит, моя цель – достичь дна бездонной пропасти."
    with fade
    "Я – всего лишь помеха в песне, которая играет в космическом плеере вечности."
    iv "Самая красивая песня – твой голос."
    iv "Самая страшная ошибка сведения – Я."
    scene bg speaker_room with fade
    "Схожу ли я с ума или еще нет? Я могу с тобой поговорить, мой милый, добрый, ночной демон в ангельском обличии невинной девушки в коричневом, рваном платье?"
    "Бармен кричал на меня, но я видел его душу. Разбитое сердце за километры видно."
    "В глазах я отчетливо вижу, как взрываются снаряды, гранаты и мины. В глазах каждого человека - история личной битвы."
    with fade
    "Но кто же ты?"
    with fade
    "Ты стала моим голосом. Ты живешь в моей голове. Ты - Мой главный ночной кошмар."

    scene bg semen_room_night with dissolve

    $ set_mode_nvl()
    "Сколько пальцев я показываю. Шесть? Н-нет, десять…"
    "Или шесть?"
    "Трудно определиться с выбором, ограничивая свои действия исключительно определенными рамками и шаблонами."
    "Выбор - показатель свободы? Я думаю, да. Точнее нет. Или да?"
    "Только не в моем случае. Для меня выбор – это ответственность. Ответственность, которая меня когда-нибудь погубит."
    nvl clear
    scene bg speaker_room room with dissolve # потенциально другой

    "Яркий коридор, освещенной хрустальной вспышкой дневного света, длинной тусклой линией заплетался между проемами белых дверей и упирался в огромное панорамное окно с розовыми витражами."
    "Через него открывался невероятный вид на Москву и на огромное, распахнутое копченое небо закрытых уродливых крыш панельных домов, на которых влюбленные подростки так любят пить вино и мечтать о счастливой и беззаботной жизни."
    "Люди наблюдают за людьми, мечтают о любви, о свободе, о вечном лете, а сверху за ними наблюдает уставший бог."
    "Я лежал в его грубых руках, сгорбившись на кожаных сиденьях, под толщей огромного сиреневого аквариума с розовыми витражами под потолком."
    "Я был на вершине мира."
    "Машины-муравьи среди домов-спящих великанов быстро передвигались по тонким венам автомагистралей, деревья-ветки торчали в лужицах маленьких скверов и парков, панельки-спичечные коробки тяжелым нагромождением наваливались на горбатые спины свисающих проводов, а я все смотрел, смотрел и прислушивался к шепоту, доносившемуся из всех закрытых дверей, и ждал."
    nvl clear
    "Долго.{w} Томительно.{w} Тяжело."
    "Под моими ногами дышал город. Крупный мегаполис в бешеном ритме перегонял в себе потоки воздуха, дыма, криков, слез и смеха."
    "Гигантское сердце погибающего человечества."
    "Я не донор и даже не гений своей группы крови."
    "Я просто прохожий, которому посчастливилось оказаться на вершине мира."
    "Я бы с радостью отдал кровь, умер за светлое будущее наших детей, спас из пожара белую кошку."
    "Вот только тут есть одна проблема: я – это и есть та самая гнилая кровь. Эритроцит в кровяной системе столичного города."
    "Под моими ногами вспыхивали и гасли фонари, бежали люди, запутанные в цепях собственных проблем и предрассудков, летели машины, обгоняя черные клинья улетающих в небо огромных птиц, а я стоял посередине этого театрального действа, на краю реальности и воображения, и не знал, что делать дальше."
    iv "Выход есть, но я не знаю, где мне выйти. Нужно найти свой выход."
    nvl clear
    "Драконы двадцать первого века – величественные ястребы над крышами бизнес-центра. Я – добыча для коршунов."
    "Ешьте меня. Я - Падаль. Гнилая плоть."
    "Я такой вкусный и питательный."
    nvl clear
    "Индустрия интернациональных корпораций съедает каждого своего сотрудника изнутри. Медленно, осторожно, смакуя каждый кусочек попавшейся жертвы."
    "Я тоже попался."
    "Ну и к черту. Попытка – не пытка. Главное, чтобы пир на костях не превратился в кровавую бойню."
    nvl clear
    "Розовые облака плыли так высоко и так величественно в вишневом небе, словно воздушные кусочки сахарной ваты из приезжего луна-парка, с уродливыми клоунами, которые созывают людей покататься на американских горках."
    "Я ловил взглядом проплывающие небесные корабли и завидовал черным птицам, которые кружат над столицей в поисках сдавшейся жертвы."
    "Три всадника апокалипсиса – птицы-дроны, патрулирующие улицы, огромные экраны, заменяющие древние билборды с бумажными плакатами, транслирующие бесконечную, бессмысленную рекламу и дома-инкубаторы, в которых человек засыпает вечным, беспробудным сном с целью проснуться в 2100 году, в эпоху «экономического» благополучия."
    nvl clear
    "Угораздило же правительство додуматься до того, чтобы внедрить камеры в глаза каждой птицы."
    "Была развернута целая программа, на которую была потрачена добрая часть федерального бюджета. Поймать всех птиц Москвы и МО, внедрить им в глаза крошечные камеры, разбить птиц на отряды и подключить к мировой системе спутников, задать им определенный маршрут и разбить весь город на сектора."
    "Кроме того, что идея звучит смешно, её реально претворили в жизнь!"
    "К тому же наблюдение должно было осуществляться из специальных центров обработки данных, что создавало дополнительные затраты на их строительство и обслуживание."
    "На каждый сектор приходится около 1500 имплантированных птиц-живых камер наблюдения. Информация о каждом объекте хранится на специальных серверах, и, когда птица-дрон умирает, его функциональная способность и опыт, сохраненный маршрут и вся информация внедряется следующей кибер-птице."
    nvl clear
    "Безопасность превыше всего."
    "Вот каким девизом прикрывалась эта правительственная программа, которая была развернута: «С целью обеспечения безопасности граждан на улицах и поддержания порядка во время проведения митингов и массовых мероприятий»."
    nvl clear
    "Но ведь на самом деле все было иначе…"
    nvl clear
    "Птицы следят за людьми. У стен есть уши. Невозможно уйти в оффлайн, закрыться от мира, спрятаться от наблюдения, сбежать от самого себя."
    "Добро пожаловать в 2027 год. Москва. Столица кибербезопасности."
    "Год \"Благополучия\" и преодоления \"Экологического кризиса\"."
    nvl clear
    "Недавно в СМИ я видел статью про задержание «Особо-опасного преступника», который долгое время отстреливал птиц-шпионов из окна своей съемной квартиры."
    "И вроде бы квартира не принадлежала ему на правах приватизации и собственности, вроде бы и личность была установлена и идентифицированна, вот только одно в этой истории отсается странным: как он смог достать оружие в мирное время?"
    "Когда каждый пистолет, каждая граната и танк хранится глубоко под землей, в замороженом состоянии, и каждому орудию смерти присвоен свой личный серийный номер после того, как правительство свернула все военные программы и прекратила разработки."
    nvl clear
    "Не мы такие. Жизнь такая. Золотые руки, смекалка и немного металлолома творят чудеса - и вот, готово ружье."
    "Складывайте ножи в кучу, поджигайте киросином, плавьте металл, перекуйте свинец на железные дороги."
    "Вот только нет огня в жилах, нет сил улыбаться в камеры."
    chat "Я не на шоу Линча, черт возьми. Я тоже человек. {w}Я жить хочу."
    "Таковыми были последние слова единственного охотника за птицами-дронами в Москве 2027."
    "А после - белый шум новостных каналов."
    nvl clear

    $ set_mode_adv()

    pause(1)
    scene anim prolog2 with fade
    "Через толстое стекло преломлялся свет, отбрасывая на стены неровный отблеск мятой радуги, который смешивался с белым фасадом закрашенных кирпичей."
    "Я ждал. Долго и томительно. Не помню уже, сколько я сидел в этой янтарно-малиновой, воздушной комнате со стеклянными потолками и наблюдал за мерным покачиванием листьев-корзинок одинокой латании, стоящей в углу."
    "Кажется, я задремал."
    "И я слышал крики, шепот, срежет и стенания людей. Я видел, как огромный человек-ворон с металлическими цепями в руках бьет заключенных за решетками тюрем строгого режима, как раненая птица падает на асфальт, словно солнце-окурок, тлеющий за гаражами."
    "Я видел свет, а в этом свете я видел каждого человека, который попал в лапы «Безопасного» города."
    "Конечно, глупо отрицать тот факт, что мы живем в тот исторический период, когда правительство сумело сократить преступность до критически низкой отметки, когда на улицах спокойно и чисто, когда экология находится на достойном уровне, что дышать на улицах можно полной грудью, не боясь проглотить вместе с кислородом вредные испарения и колючую пыль."
    "Но все равно становится как-то не по себе, когда на огромных, цветных билбордах вспыхивает изображение очередного бесполезного товара в красивой упаковке, которую так и хочется разорвать на куски."
    "Мы стали теми, кого не понимали в детстве."
    pause(1)
    "Сам себе демон,{w=1} сам себе бог. Свой рай,{w=1} свой Лимб."
    "Своя судьба."
    scene black with fade
    $ renpy.pause(3, hard=True)
    # фон?
    "Я очнулся от резкого, грубого оклика. Тяжелая белая дверь с мутным, щербатым стеклом гулко ухнула и впустила меня в пространство просторного кабинета."
    "За столом сидел мой личный доктор и, по совместительству, мой единственный собеседник и друг на ближайшие сутки."
    "В накрахмаленном белом халате, застегнутом на все пуговицы, с округлыми очками в серебряной оправе, с каштановыми завитыми волосами, она, скорее, напоминала старую-добрую медсестру времен Советского Союза, чем настоящего солдата медицины, в арсенале которого есть самые последние научные разработки в областе микрохирургии и ринопластики."
    "Женщина жестом пригласила меня подойти к столу."
    "Я повиновался и, опустившись на мягкую кожу, нервно вжался в подлокотники глубокого, жилистого кресла."
    "Где-то внутри я пытался подавить свою тихую панику."
    "То ли размеры кабинета давили на меня своими стеклянными артериями, то ли головокружительная высота и блики солнца по фасаду соседних зданий расфокусировали мой взгляд и избавили от существования бдительность,"
    "Но одно я знал наверняка: в руках этой женщины лежит вся моя жизнь."
    "Я доверяю свое будущее незнакомому мне человеку."
    "И угораздило же меня попасться под руку своего руководства в тот день, когда я решил ненадолго задержаться на работе после окончания смены в Московском Геологическом Университете…"
    # фон института
    iv "Чёртовы ключи! Куда же я их мог положить!"
    "Я облокотился на спинку стула и беспомощно посмотрел на потолок."
    # фон свет
    "Белый, мигающий, больничный свет привел мое сонное лицо в чувство, и я резко выпрямился, больно ударившись об угол стола."
    "Посмотрел на часы: 00.39. Время позднее."
    "Я бы с радостью ушел домой пораньше, если бы только знал, куда я положил свои ключи от квартиры."
    "Я достал с полки очередной ящик с документами и нервно перебрал пальцами стопку бумаг."
    iv "К чёрту!"
    "В проеме показалось лицо Олега Степановича, руководителя научной кафедры, заслуженного доктора Геологических наук, ветерана многочисленных геологических экспедиций, бога местного клоповника, владельца чашки \"Boss\", нашего брата, отца, деда и так далее по списку."
    os "Вань, залетишь ко мне, как соберёшься уходить?"
    "Олег улыбнулся и сверкнул своими засаленными волосами. В руках он сжимал свою любимую, вечно грязную кружку, из-за которой он получил своё прозвище, которая хранила в себе аромат застоявшегося кофе."
    ivan "Без проблем, {w=0.5}Босс."
    "Я протянул шипящую в конце."
    "И, отсалютовав, подумал, что сейчас стоит быть подружелюбнее."
    "Перспектива заночевать на рабочем месте меня не очень радовала, а лишние беседы в этот час вызывали раздражение."
    iv "Я просто хочу отдохнуть."
    with fade # фон?
    "Длинный коридор засыпающего института казался непроходимым лабиринтом. В темноте мир представляется совсем другим. Вещи приобретают новые свойства, характеристику и возможности."
    "Дай волю своему воображению – и вот ты уже не в стенах института, а на космическом корабле, захваченном пришельцами. С шатающейся непонятно что делающей в 2027 галогеновой лампой с неприятным холодным бело-синим свечением."
    "Ну а желтый свет, вытекающий из проема двери, обозначил для меня контур кабинета Олега Степановича."
    # бо$$ рум
    "Дверь скрипнула, и я переступил высокий порог, отделяющий личное пространство кабинета научного руководителя от шумной автомагистрали коридоров."
    ivan "Вызывали, бос{w=0.17}с?"
    "Ехидно спросил я, прекрасно осознавая всю абсурдность этого вопроса."
    os "Да садись уже. Чем тебе моя кружка не угодила?"
    ivan "Просто у меня такой же нет. Вот и завидую. Видите, какой зелёный. И вряд ли это из-за той шаурмы..."
    "Олег Степанович кашлянул и внимательно посмотрел на меня."
    os "А теперь нам нужно с тобой серьезно поговорить."
    iv "Неужели выкинут? Хотя, учитывая то, какой фигнёй я маялся последний месяц, я даже не удивлён."
    os "Ты ценный сотрудник. Дело свое знаешь, географию любишь, геологию уважаешь, историю учишь и понимаешь. Такие люди в нашем деле самые незаменимые, как считаешь?"
    iv "Какие лестные слова! Ну что, сокращение или слёзные прощания с зарплатой?"
    "На самом деле я язвил только из-за того, что нервничаю, и на его вопрос лишь пожал плечами."
    os "Конечно незаменимые, не скромничай. {w=1}Ну, так вот. {w=0.5}Давай ближе к делу. Ты был выбран мной в качестве подопечного в одном важном…{w=0.35} эксперименте."
    "Олег Степанович замялся и сжал вспотевшие пальцы в замок."
    os "Ты знаешь, что современные технологии играют важную роль в жизни человека. Наука не стоит на месте, проводятся глубокие исследования в различных областях гуманитарного и технического цикла, открываются новые законы и закономерности."
    "Как будто начал лекцию, заговорил мой босс."
    ivan "И… А я-то тут причём? Моё дело – уезжать в экспедиции на хренову тучу дней да первокурсников пугать своим видом между пар."
    os "Вот именно!"
    "Да, я умею пугать студентов настолько хорошо, что меня за это хвалит сам Высший."
    "Олег Степанович соскочил со своего места и торжественно положил руку на моё плечо."
    iv "Похоже, намекнул на то, что мне пора валить из института подальше."
    os "Ты будешь первым, кто опробует последнюю научную разработку!"
    ivan "Очередная бесполезная разработка?"
    os "Никак нет!" # NINE! NOPE! NONE.
    os "Это чудо инженерной мысли – бесконтактные умные линзы!"
    #iv "Ы?"
    os "Google Glass помнишь?"
    ivan "Очки из 2014, которые пришли в никуда?"
    os "А эти приведут тебя к успеху! Могут заменить тебе компьютер, телефон и даже саму Википедию. Более того, ты сам станешь ходячей энциклопедией и сможешь вывести нашу работу на совершенно новый уровень."
    iv "Да ну. Скажите, что это ещё бесплатно и поставляется в подарочной упаковке?"
    "Я с удивлением посмотрел на своего научного руководителя."
    ivan "Вы, должно быть, шутите?"
    "Нервно спросил я, подозревая, к чему может привести подобные «Технологии»."
    ivan "Мне бы не хотелось, чтобы какой-нибудь программист хакнул мои глаза. Это же живой орган тела, черт возьми, а с кибербезопасностью шутки плохи."
    os "- Не волнуйся. Все по стандарту. S-класс. К тому же процедура бесплатная. Они ищут волонтеров от разных профессий для альфа-тестирования этогопроекта. Вот ты им и станешь. Без разговоров. Это не обсуждается!"
    "Резко отрезал Олег Степанович."
    ivan "Но... {nw=2}"
    os "Никаких \"но\". Ты только представь, какие возможности нам откроет этот модный, высокотехнологичный девайс."
    os "Наша научная работа будет упрощена в несколько раз, а ты станешь самым незаменимым участником всех экспедиций. Все. Решено. Ты станешь волонтером от нашего Института."
    with fade
    stop music fadeout 1
    "Больше я ничего не помню. Олег Степанович эмоционально жестикулировал руками, кричал, бранился, улыбался, а я просто сидел в кресле и клевал носом…"
    show blink
    pause(1)
    scene black behind blink with dissolve
    "Веки отяжелели. Дыхание успокоилось. Кровь остыла."
    "И я заснул беспробудным сном в кабинете своего начальника."
    # больница
    chat "Вы подтверждаете ваше решение и обязуетесь соблюдать условия договора? Поставьте подпись юридического лица здесь, и соглашение вступает в силу незамедлительно."
    "Врач посмотрела на меня с выражением скрытого страха и волнения."
    "Я взял ручку и машинально поставил свою подпись."
    iv "Делайте, что хотите. Вы мне дарите орлиное зрение, а я не подаю на вас в европейский суд по правам человека – все просто, как дважды два."
    iv "Скоро буду обновлять ленту ВК, не доставая телефон из порфеля."
    "До чего дошел прогресс."
    with fade
    "Доктор взял со стола документ, убрал его в тяжелый сейф и кивнул мне головой."
    chat "ТЫ ПОЙДЁШЬ СО МНОЙ?"
    ivan "Ч..Что?"
    "Меня ударило током."
    uv "Ради меня, я прошу тебя, ты должен поехать. Это очень важно."
    ivan "Какого…"
    "Я не успел закончить ругательство - девушка в халате зажала мне рот и надела на меня маску."
    scene black with fade
    "Я снова выпал из реальности."
    scene white2 with flash
    play sound_loop sfx_head_heartbeat
    "Мысли бешено стучали в голове, кровь массировала мои вспотевшие виски. Я резко рванул из цепких рук доктора, схватил вазу со стола и швырнул в стену. Яростный крик и звон разбитого стекла привел меня в чувство."\
    stop sound fadeout 0.5
    iv "Так ты нашла меня. Ты следила за мной все это время. Я знал это…"
    with fade
    "Я оказался привязанным к каталке. Я рвался, кричал, но ремни крепко сжимали мое тело."
    "Вот и все. Девочка-демон. Я знал, что ты существуешь."
    "Когда-нибудь мы с тобой встретимся еще раз, и это будет худшим днем в твоей жизни."
    scene bg night_sky with fade
    "Над моей головой рассыпались созвездия. Огромные светящиеся квадраты под потолком мелькали в глазах, заполняя мои зрачки резким светом."
    uv "Совсем скоро все изменится. Все будет по-другому. Но я прошу тебя, ты не должен бояться. Верь мне.{w} Ты пойдешь со мной?"
    "Она посмотрела на меня своими грустными, проницательными глазами, и я снова нырнул в холодный омут. На этот раз я видел ее перед собой, ощущал ее дыхание, чувствовал ее прикосновения."
    "Она настоящая."
    "Я ЗНАЛ. Я знал это."
    show cg uvao_d0 with dissolve
    "Океанами глаз твоих можно устроить потоп."
    ivan "А разве у меня есть выбор?"
    "Я беспомощно улыбнулся, как улыбается человек, находящийся на пороге смерти, и посмотрел на своего ангела-хранителя."
    uv "Два пути есть на свете: один ведет в пропасть вечной пустоты и холода, другой же путь ведет к солнцу. Ты сам выбираешь свой путь. Конец дороги – это только начало."
    ivan "Тогда я пойду с тобой. И останусь."
    uv "Навсегда?"
    uv "Навсегда."
    "А что я мог сделать? Выцарапать ей глаза, броситься в окно, разбить свои кулаки об стеклянную стену из стекла такой прочности, что сейчас ты можешь уронить телефон двадцати метров и он только отскочит, не деформировавшись и не треснув?"
    with fade
    "Надо мною, кроме твоего взгляда, не властно лезвие ни одного ножа."
    # фон
    "Я попал в стерильную комнату с едким запахом хлора. Огромный прибор над потолком, отдаленно напоминающий лазер, давил на меня своей громадой."
    show blink
    scene black behind blink with dissolve
    "Я закрыл глаза. Вы даете мне зрение орла, а я не подаю на вас в суд. Все просто."
    uv "А теперь… спи."
    with fade
    # сверху не Юля?
    scene speaker_room
    show cg uvao_d0
    with flash
    play sound whisper
    uv "Ты все испортил."
    "Я все испортил. Не отрицаю."
    $ set_mode_nvl()
    nvl clear
    "Моя голова – кинотеатр страшных историй, транслирующий уникальную хронику моих личных поражений, провалов и неудач."
    "Такие фильмы не крутят после полуночи в местном кинотеатре, даже если твой паспорт подтверждает достижение восемнадцатилетнего возраста."
    "Такие фильмы сам дьявол показывает в наказание тем, кто заключил с ним сделку."
    "Самую страшную, самую важную, самую мрачную сделку."
    nvl clear
    "Я – творец своей реальности. Я заслужил это."
    ". Ну что ж, раз такое дело, присаживайтесь поудобнее, запасайтесь шипучей колой, поп-корном и сахарной ватой. Выключайте мобильные телефоны и приготовьтесь. Копирование материалов и несанкционированная съемка преследуется по закону."
    with flash
    nvl clear
    "Хотя кого это волнует?"
    "Сам себе критик, сам себе режиссер."
    nvl clear
    "Девять месяцев назад ушла она. Самая нежная, мягкая и добрая девушка, которую я когда-либо встречал в своей жизни."
    "Она мне всегда говорила, что в недрах земли спрятан таинственный город, населенный древними существами, которые живут в мире и спокойствии."
    "Без вмешательства человека."
    nvl clear
    "Я всегда посмеивался над ее глупыми фантазиями, а сам в глубине души свято верил, что в одну из своих экспедиций я обязательно найду пещеру, ведущую к центру земли, чтобы подарить ей на день рождения ее выдуманный мир, который окажется правдой."
    "Я мечтал исполнять ее желания. Но, по всей видимости, чудес не бывает. Я не волшебник, да и научиться этому у меня никогда не получится."
    "Она всегда готовила горький кофе, по воскресениям пекла тыквенный пирог со сливками и никогда не умела выбирать платя. Звонко смеялась, когда ловила мой заспанный взгляд по утрам. А я стоял, такой глупый, взлохмаченный, такой сердитый, и смотрел, как она ловким движением руки уносит мой рабочий халат в ванную, чтобы освежить его перед моей институтской практикой."
    "По вечерам она нежно рисовала своей белой кистью спутанные узоры на грунтованном холсте, А потом долго стояла на балконе, считая тусклые звезды городского неба, запертого в паутину проводов, столбов и грязно-желтых фонарей."
    nvl clear
    "Девять месяцев назад я был дома."
    "Когда простой геолог влюбляется в художника, то рождается…{w=1} скульптор?"
    "Возможно." # But not in mine case
    "Но теперь я никогда уже не привезу ей с Ключевой Сопки осколок обсидиана для того, чтобы она поставила его на полку к своим «особенным» вещам: к старым часам с газовым циферблатом под стать антуражу давно ушедшей эпохи великого Союза Социалистических республик, к пыльному пленочному фотоаппарату «Зенит» и к паре банок с серебряной краской. "
    "Она никогда больше не будет ждать меня. Не спустится ко мне на чай, не поправит мою заросшую челку, не нарисует на холсте свой воображаемый подземный мир, который она ласково именовала: Иваново царство."
    nvl clear
    "Девять месяцев назад я засыпал в своей свежей постели, предварительно повесив свой белый, выглаженный лабораторный халат на спинку резного стула."
    "Просыпался под шум разговорчивого чайника, который питался адскими температурами крутого кипятка."
    "Обнимал этот нежный, теперь уже туманный и разбитый образ моего личного художника, ловко орудующего сковородкой на нашей совместной, теплой кухне с желтыми занавесками."
    nvl clear
    "Иногда по вечерам сквозь эти занавески пробивалось солнце."
    scene bg semen_room_sunset with dissolve
    "Яркое, желтое, лимонно-сахарное, оно растекалось по нашей кухне, заполняя белые стены оранжевой, густой краской."
    "Малиновый закат стекает по стене."
    nvl clear
    "В тех ломаных лучах я насквозь и вокруг тебя рассмотрел, только ты ничего не знала обо мне."
    "Черт возьми, Старина Корж. Ты как всегда оказался прав."
    "Но только это я не знал ее. И, видимо, даже не пытался ее понять."
    " "
    "Это моя вина."
    nvl clear
    "Она никогда не говорила мне, что хочет на самом деле."
    "Я жил с ней в счастливом неведении и никогда бы не подумал, какие тайны может скрывать за собой женский разум."
    "Она мечтала о море, но я этого не знал. Она мечтала о памятной прогулке по набережной с бутылкой красного-полусладкого, но я все время не находил времени для нее."
    nvl clear
    "Она терпела меня. Ждала. Верила. Надеялась… Надеялась, что когда-нибудь я вернусь домой в восемь, и, взяв ее за руку, уведу на крышу дома считать звезды."
    nvl clear
    "Она ждала."
    "Не долждалась."
    nvl clear
    "Она ушла к реалисту. Говорят, любовь не приходит одна. С ней приходит надежда, счастье и… разочарование? Но вот только уходит она как-то тихо, по-английски, не прощаясь."
    nvl clear
    "Любовь ранит сильнее, чем острый нож, пущенный в спину, но не было минуты страшнее, чем тот дождливый день, когда мои желтые занавески приобрели нездоровый зеленоватый оттенок."
    #*вспышка. Фотографии кухни, рука, выспышка, шепот становится все сильнее
    with flash
    nvl clear
    $ set_mode_adv()
    # фон дома
    ami "Ты правда собираешься на Алтай?"
    "Амина улыбнулась своей лукавой улыбкой и посмотрела через мольберт на мое сосредоточенное лицо."
    ivan "Дорогая, ты же знаешь, как это важно для меня. Через полгода я буду защищать работу на звание профессора кафедры геологии. Материал для исследований почти собран. Экспедиция всего лишь на неделю. Возьмем все самое необходимое. У нас отличная, подготовленная команда. Разве может что-то случиться? Нужно только спички обернуть в целлофан, да карту местности найти самую свежую. Я обещаю, что скоро мы опять будем вместе."
    ami "А я так не думаю."
    "Амина вздохнула и погрузила кисть в баночку с водой."
    ami "Мы больще не вместе, Вань. Прости. Ты вечно в работе, в делах, спишь в институте, приходишь поздно. Ты живешь походами и костром, а я живу домом и масляными красками."
    $ set_mode_nvl()
    "А потом пошли бесконечные люблю, ненавижу, прости, понимаешь, клянусь. Это можно было продолжать вечно. Ругаться – это так просто, черт возьми."
    "Ломать – не строить."
    ivan "Прости, прощай."
    nvl clear
    "И нет больше Амины. Нет свежего халата, мольбертов и морских пейзажей, нет больше старых книг с иллюстрациями на пожелтевших страницах. Нет больше света за окном. И пряного запаха свежего хлеба со специями."
    "Прости.{w} Прощай.{w} Я убиваю все, что люблю."