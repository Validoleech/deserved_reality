label dr_day1_intro_old:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ sch_newday(sch_dayNo=1)
    $ name_sch('Я')
    # НАЧАЛО НЕ СООТВЕТСТВУЕТ
    scene anim prolog_2
    show yellowish:
        alpha 0.5
    with fade
    "Я чувствовал себя утопленником."
    "Тьма. Отсутствие гравитации, непонятная тяжесть по всему телу и отсутствие воздуха."
    "Здесь отказывали все органы восприятия человека, и только какое-то чутьё намекало на возможность выхода."
    play ambience ambience_ext_road_day fadein 10
    "Пустота и боль на месте шва сменилась ощущением нахождения на жестком автобусном сидении, в глаза начал бить яркий желтоватый свет."
    show blink
    pause(1.0)
    scene expression Sepia('bg int_bus') behind unblink
    show unblink
    pause(1.5)
    scene bg int_bus with flash
    "И глаза я открыл уже в другом месте - меня не окружал мой город или перрон безымянного города, окружённый холодными оттенками розового заката."
    "Сиденья цвета кофе с молоком, жестяной рифлёный пол, красные вельветовые шторы - потолок казался неоправданно высоким для автобуса и создавал уютную атмосферу в тёплых тонах."
    "Я сразу же отметил довольно жесткие сидения и стерильную пустоту в салоне, и только множество значков с разными городами и неизвестными мне фирмами указывали на то, что автобус всё же кто-то водил."
    iv "И вообще похоже на какой-то советский автобус, если честно."
    iv "Надо бы Олегу Степа…"
    iv "Какой к чёрту Икарус?! Кто такой Олег Степанович? Что со мной было?"
    iv "Помнится мне, что когда я садился в него, он выглядел другим."
    ivan "А-апчхи!"
    "А ещё тут было довольно пыльно."
    show prologue_dream with dissolve
    "Я напряг виски и пытался вспомнить."
    "Первым вопросом на повестке дня была совсем не фраза \"где я?\", хотя и она довольно быстро всплыла во всё ещё неадаптировавшемся к резко изменившимся условиям мозгу."
    iv "Кто я?"
    "В голове был сплошной белый шум да непонятная девочка в оборваном коричневом платьице, которое так уместно подчёркивало её фигуру и совсем не скрывало части тела."
    "Сначала было довольно трудно вспомнить даже имя, но за ним потом нашлось и отчество - вместе они звучали, как у героя одного советского фильма, пересматриваемого мною в детстве."
    $ name_sch("Ваня")
    "Дразнилки в первом классе и шутки про фамилию и то, что я меняю профессию."
    "Кадры начали набирать обороты - и в считанные секунды мимо меня пронеслась вся жизнь."
    "Аметист, операция над глазами, и чёртова девочка - она не покидала меня ни на одном кадре моего существования."
    "Она была активным участником всего - но при этом её никто не замечал. Будто её и не было никогда."
    "А вот одно из относительно недавних воспоминаний - я пишу о том, что меня посетила тульпа и я на всякий случай пишу завещание. Мне, кажется, лет двадцать. Завещать было по сути и нечего, но важно то, как я это делал:"
    "Обычными чёрно-синими, искрящимися через прозрачный корпус авторучки, чернилами на бумаге, которой в наши дни пользуются разве что параноики да художники, не осознавшие ценность дешевейшего полимера, стилус для которого почти не стирается и заменяет всевозможные фломастеры и карандаши всех видов."
    play music premonition fadein 10
    ai "Вы желаете открыть историю запросов за этот период?"
    iv "Нет, спасибо."
    "И операционка моих линз, которую зовут просто и со вкусом - Искин - тоже был частью моей памяти."
    "Я смотрелся, наверное, очень глупо - стоит человек с еле переливающейся, как поляризованные линзы, радужкой глаза, смотрит в никуда и у него наворачиваются ностальгические слёзы."
    "Наконец память начала отчеканивать последний день жизни \"до\" - дальше голова просто не могла ничего найти в своих закромах."
    hide prologue_dream
    scene bg int_bus
    with flash_red
    "Воспоминания кончились и при попытке что-то вспомнить дальше я лишь слышал своё же едва ли сбитое дыхание."
    ivan "Я жив... Я обманул смерть! Обманул, слышите!"
    "По большему счёту мне стало плевать, где я, ведь лишь одна мысль о том, что я не остался в этом мире очередным надгробием, радовала меня до дрожи."
    "Вскоре эйфория прошла и я начал задумываться о своём местонахождении."
    iv "Я на поезде ехал на экспедицию. Так какого чёрта меня забыли? И где тогда моя экипировка?"
    "Я решил проверить себя на удачу и обнаружил в карманах несколько интересных вещей - одной из них был смартфон чуть ли не десятилетней давности, ещё на Андроиде, а так же чехольчик с наушниками неизвестной компании, но с наклеечкой \"Hi-Fi\", высеченой на корпусе рядом с надписью \"Assembled in China\"."
    iv "Ну да, кто бы сомневался. Если бы мне такое подарили в 2020-м, я бы, быть может, и радовался, как ребёнок. Сейчас же мне эта операционка напиоминает только о попытке оживить свой старый Самсунг прямо во время похода, без доступа к ноутбуку и интернету."
    iv "Тем не менее, алюминиево-стеклянный брусок казался довольно полезной вещью в legacy-жизни. Сто процентов зарядки, относительно новый аккумулятор, способный прожить денька три, если играть без перерывов - что ещё нужно для человека, пользующегося только соц. сетями и читалкой?"
    "Я легким движением руки достал наушники, вставил их в миниджек, и включил первую попавшуюся песню - звук оправдывал свою золотую наклейку, потому я отправил это всё обратно в карманы, решив, что лучше будет сконцентрироваться на попытке понять, где я."
    "Чем дольше я находился в автобусе, тем жарче становилось в салоне, а пропотеть, сидя в салоне и рассмартирвая шторы, не особо сильно хотелось."
    scene bg int_bus:
        pause 0.2
        xalign 0.5 yalign 0.5
        ease 0.5 zoom 1.5
    scene bg ext_bus with dissolve
    ivan "Чёрт возьми, да это же реально Икарус!"
    scene bg ext_bus:
        xalign 0.5 yalign 0.5
        ease 1.5 zoom 2.0 xalign 0.15
        ease 7.0 xalign 0.85
    "Казалось, что он только что совершил одну из своих первых поездок - автобус казался абсолютно новым, и единственное, что показывало небольшой стаж машины - дорожная пыль на дверях и нижней части корпуса."
    "На решётке радиатора красовался номер модели - 256, а чуть повыше - название автобуса."
    "Видеть такие, ездящие по дорогам Москвы, мне не удавалось - родился я поздновато для них. В моё время уже ездили Мерседесы, Рено и прочие звери иностранного автопрома для рейсов."
    iv "Настоящий Икарус. Куда меня занесло?"
    scene bg_ext_bus with dissolve
    "Я насмотрелся на чудо венгерской мысли и отошёл, чтобы поглядеть на ту дорогу, по которой приехал."
    scene bg ext_road_day with dissolve
    "И только успел зайти за автобус, как..."
    $ renpy.music.set_volume(0.2, 1.0)
    ivan "Господи, какая красота..."
    "Поле, бесконечный горизонт, извивающаяся змеёй дорога и лес. Густой, ярко-зелёный, почти что кислотный пейзаж. Будто кто-то впервые за всю жизнь взял и протёр глаза вельветовой тряпочкой, убрал лишнее, освободил мозг для мыслей, и отвёл к этой дороге."
    "Я понимал, что могу смотреть на это часами. К чёрту горы Алтая, к чёрту природные ландашфты - все эти воспоминания выветрелись, чтобы как можно точнее запомнить каждую травинку и трещинку в асфальте."
    "Ещё несколько минут я искал свою челюсть, но на место удовольствия вновь пришла тревога."
    iv "Я не знаю, где я. Да, это, безусловно, красивый вид, но я не помню, чтобы меня трясло во время дороги, да и в Икарус я ни разу не садился! Тем более на последние места - на них меня всегда укачивало, и сидеть с пакетом под рукой было не особо приятно."
    "Я вспомнил свою единственную поездку на последнем ряду автобуса и невольно поёжился, вспоминая далеко не самые приятные ощущения, включащие тошноту, духоту и адскую тряску."
    "Но это всё в детстве. Мне тогда было дай бог лет шестнадцать. Сейчас, через десяток лет и несколько операций, кроме невосприимчивости к Драмине я получил практически идеальный вестибулярный аппарат и неплохое телосложение."
    "Кстати, о нём. Чувствовал я себя довольно странно, будто одежда на мне стала на пару размеров больше."
    "Один ремень на джинсах я подтянул почти сразу же, как очнулся."
    "Надо бы посмотреть, как я выгляжу хоть."
    scene bg ext_no_bus with dissolve
    $ renpy.music.set_volume(1.0, 1.0)
    ivan "Что?!"
    iv "Автобус, что ещё несколько минут назад стоял здесь, без лишнего шума просто исчез у меня из-под носа!"
    "Ни гула двигателя, ни шагов водителя - в такое развитие событий я просто не верю!"
    "Только если там двигатель от электромобиля и местная трава не издаёт шума, когда прогибается."
    play sound sfx_mystery_movement # лажа, звук не тот
    "Я поводил ногой по обочине и закономерно услышал шелест и почти что звонкий хруст растений."
    "Пришло время воспользоваться высокими технологиями!"
    "Я сначала было потянулся к смартфону, но вспомнил о новенькой аугментации, которую мне впаяли в мозг и глаза только вчера!"
    "В теории, абсолютно вся связь проходит через сеть компании, которая мне этот девайс выдала. Для сбора статистики, не иначе."
    "Какое же было моё удивление, когда висящая в углу с самого момента включения линз иконка подключения к серверам \"Востока\" показала крестик, грустный смайлик и растворилась в фоне интерфейса."
    iv "Рано я списал свой телефон со счетов."
    "От сенсорного экрана я ещё не отвык, так что шторка и совсем не устаревший за десять лет интерфейс подарили мне не только ностальгические нотки, но и нотки ангста и отчаяния."
    "Ни вайфая, ни блютуза, ни мобильного интернета. Ни-че-го."
    "Ситуация ухудушалась радиомолчанием - во всех смыслах. Ни FM, ни смежные частоты не подавали каких-либо признаков жизни, кроме разве что вечных выяснений, у кого вышка больше."
    "Хорошую новость я нашёл только в том, что у меня, судя по солнцу, правильно показывается время. Только вот с датой какая-то лажа. 01.01.1970. Опять слетела. Я же не пользуюсь чёртовой Нокией из 2009, чтобы после вытаскивания аккумулятора всё пропадало!"
    ivan "Да где я, чёрт возьми?"
    "Ладно, на сколько бы я не пытался отложить поворот головы назад, мне придётся посмотреть на то, где я находился."
    "Я же всё-таки не играю в какой-нибудь квест! Хотя моя рекогнисцировка проявила огромную неэффективность. Я лишь понял, что нахожусь в чертовски красивой глуши, где даже связи нет."
    "Чёрный ящик открывается, и мы оказываемся в..."
    scene bg ext_camp_entrance_day with dissolve
    iv"В пионерлагере?!"
    ivan "Что, простите? Это какая-то шутка?"
    "Несмотря на внезапное появление в автобусе, который также внезапно исчез, я всё ещё пытался найти происходящему хоть какое-то объяснение."
    "Я пригляделся получше."
    scene bg ext_camp_entrance_day:
        xalign 0.5 yalign 0.5
        ease 1.5 zoom 2.0 xalign 0.3 yalign 0.95
        ease 5.0 xalign 0.7
    "Нет, я не ошибся. На больших жестяных воротах, еле приоткрытых и достаточно старых, чтобы с них начала слезать краска, красовалась надпись русскими буквами: \"пионерлагерь\"."
    iv "Видимо, я попал в какой-то заброшененый лагерь. На Икарусе. С телефоном десятилетней давности, наушниками пятилетей, и это всё после падения с небоскрёба под подначивания моей шизофрении."
    iv "Да, абсолютно правдоподобно. Я в это верю."
    play sound sfx_inhale
    $ renpy.pause(1, hard=True)
    scene bg ext_camp_entrance_day with dissolve
    ivan "Нет, чёрт возьми, я в это не верю! Ну не мог я просто так уснуть в койке, потом выписаться, решить взять с собой древнюю электронику и поехать в заброшенный лагерь, перед этим украв Икарус 256 прямиком из автомузея, приехать, уснуть, и ничего из этого не вспомнить!"
    iv "Меня определённо сюда переместили, если так можно сказать."
    "Я любил научную фантастику и перечитал разные истории про подеселенцев, перемещающихся в разные миры, но чтобы таким образом, да на своём примере - это для меня совершенно новый опыт."
    iv "Может, я попал на какой-нибудь фест или реконструкцию? Да ну, бред-идея, особенно после той нечисти, что тут происходит."
    "Оставался только один вариант - и он не предполагал очень хорошего исхода."
    iv "Я сейчас попал в настоящий Советский Союз где-то в семидесятых-восьмидесятых до начала распада, ибо автобус выглядит слишком новым, да и не похоже, что лагерь заброшен - кто-то же поддерживает в чистоте эти две статуи пионеров, одна из которых..."
    scene bg ext_camp_entrance_day:
        xalign 0.5 yalign 0.5
        ease 1.5 zoom 2.0 xalign 1.0 yalign 0.6
    ivan "Пьёт водку? Серьёзно? Это какая-то шутка пионеров-скульпторов, которую не заметили?"
    "Скульптуры-пионеры же были гипсовые и почти не имели царапин, что забивало последние гвозди в крышку гроба, в котором покоилась моя уверенность в какой-либо рекреации или несмешной шутке."
    scene bg ext_camp_entrance_day:
        zoom 2.0 xalign 1.0 yalign 0.6
        ease 0.5 xalign 0.5 yalign 0.5 zoom 1.0
    show sl smile pioneer far with dissolve

    # А ОТСЮДА УЖЕ НОРМ
    iv "Ладно, хватит смотреть на произведения искусства. Я не очень хочу тут задерживаться."
    "И только я хотел подумать о заброщенности лагеря, как ворота заскрипели и из них выскочил человек, чей пол я не смог определить из-за яркого палящего солнца."
    show sl mile pioneer normal with dissolve
    "Я смог её рассмотреть только тогда, когда она приблизилась. Передо мной стояла девушка. Она была чуть ниже меня ростом, имела блондинистые, до золотого блеска яркие волосы, сплетённые в две длинные косы, большие и глубокие {i}ледяные{/i} глаза и большая добрая улыбка."
    "Одета она была в нечто странное и непривычное для меня в такой ситуации - белая открахмаленная блузка с шевроном на левом рукаве и повязаным на шее красным кумачовым галстуком, бледно-синяя короткая юбка и туфли, надетые на белые носочки."
    "К тому моменту, как я составил картину её внешности, она приблизилась ко мне и ещё сильнее улыбнулась."
    sl "Привет. Ты новенький?"
    ivan "Привет. Н-ну да, наверное."
    sl "Я Славя. Полное имя Славяна, но вообще все зовут меня Славей, так что и ты не стесняйся так называть."
    ivan "Ладно, договорились."
    "Она распологала к себе с первых секунд не только манерой речи, но и мягким голосом, как будто со мной говорит моя старшая сестра."
    sl "А тебя как зовут?"
    "На некоторое время я растерялся от вопроса в мою сторону, но быстро вернул равновесие и спокойно ответил."
    ivan "Меня? Я Иван."
    sl "Можно я тебя буду Ваней называть?"
    ivan "Мне без разницы."
    "Из-за ворот раздался горн и девушка оживилась и была готова убежать в ту же секунду без прощания."
    sl "Ладно, Ваня. Мне пора, ещё увидимся! Сейчас тихий час, так что не шуми!"
    ivan "Постой! А куда мне идти-то?"
    show sl shy pioneer with Dissolve(0.25)
    show sl smile2 pioneer with Dissolve(0.25)
    show sl shy pioneer with Dissolve(0.25)
    "Девушка на секунду засмутилась от моего вопроса, потом улыбнулась и ещё раз засмутилась."
    iv "Стесняется что-то сказать? Или не хочет?"
    show sl smile2 pioneer with dissolve
    "Наконец, оцепенение слетело с неё и она начала тараторить."
    sl "Тебе сейчас надо к Ольге Дмитриевне..."
    "Она увидела моё недопонимание и дополнила:"
    show sl smile pioneer with dspr
    sl "К вожатой. Она тебя отправит на склад, где я тебе выдам форму, но ты не торопись, ладно?"
    sl "К её домику путь такой - идёшь сейчас прямо, сворачиваешь на площадь - она у нас одна, не пропустишь. Проходишь её насквозь и идёшь в ряды домиков к крайнему справа. Он семнадцатый на карте. Всё запомнил?"
    menu:
        "Хорошо, пока.":
            sl "Если что, спросишь у других. Всё, мне пора, пока Ещё увидимся!"
            hide sl with dissolve
            "Девушка ещё раз быстро улыбнулась и скрылась за воротами лагеря."
        "А ты можешь мне карту дать?":
            $ sch_day1_sl_together = True
            $ pt_ka -=10
            sl "Ой, карта!"
            show sl angry pioneer with Dissolve(0.25)
            show sl shy pioneer with Dissolve(0.25)
            "Славя, видимо, не ожидала от себя забывчивости, потому прохлопав немногочисленные карманы, цокнула каблуком, чем напугала меня, и продолжила теребить косу."
            sl "Не могу."
            ivan "Забыла?"
            sl "Угу."
            "Она ещё немного подумала и, судя по выражению лица, наконец пришла к стоящей мысли."
            sl "Давай я тебя проведу к вожатой?"
            ivan "Ты? А у тебя время есть?"
            "Я был настроен довольно скептически и потому на предложение Слави посмотрел довольно холодно."
            sl "Если будем идти быстро, то всё успеем."
            ivan "Ну веди тогда."
            "Славя собиралась схватить меня за руку, видимо, чтобы я не потерялся, однако я также быстро одёрнул её."
            iv "Если тут настоящие пионеры, то дети быстро сплетни разведут."
            scene bg ext_clubs_day with dissolve
            "Златовласка, похоже, не очень сильно обиделась и впустила меня за ворота, сразу прикрыв за мной."
    return

label sch_day1_camp:
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_clubs_day
    if sch_day1_sl_together:
        show sl normal pioneer
    with fade
    "Изнутри лагерь совсем не казался заброшенным или старым."
    "Асфальт с проросшей травой сменился каменной плиткой, кое-где неровной, но всё ещё не потрескавшейся, а стены первого попавшегося мне здания хоть и просвечивали материалом, из которого были построены, были абсолютно целыми."
    "Из здания пахло палёным деревом и сварочного аэрозоля, потому я в одноэтажном строении сразу признал жилище инженеров."
    "Мои опасения подтвердились, когда рядом с дверью на зеленоватом куске бетона висела картонная табличка с надписью \"Клубы\" и расписанием кружков на ней."
    sl "Это здание клубов. Им заведует Серёжа Сыроежкин, он из нашего отряда, вы ещё увидитесь с ним."
    show sl serious pioneer at left
    show us grin sport at left:
        yalign -1.5
        ease 0.5 yalign 0.5
    with vpunch
    if sch_day1_sl_together:
        "Внезапно из-за кустов выскочил ещё один ребёнок и встал между мной и Славей."
    else:
        "Внезапно из-за кустов передо мной выскочил ещё один ребёнок."
    "Она была намного ниже меня и на вид ей можно было дать не больше четырандцати, однако энергии у неё было на несколько ГЭС, и огненно-красные волосы, быстро собранные в две больших копны, и бегающие глаза только доказывали её недобрые намерения и исключительно большую энергичность."
    us "Привет! Ты кто такой?"
    "Желания говорить с ней у меня было ещё меньше, чем со Славей в первую минуту."
    iv "Не на того напала."
    ivan "Я? Я Никто."
    us "Никто? Тогда добро пожаловать!"
    show cricket:
        align(0.5, 0.5)
        easein 0.25 zoom 1.5
    with Shake(None, 1.0, dist=5) # может неверно?
    play sound surprise
    show us grin sport at left:
        ease 0.5 xalign 0.5
    "Она разжала кулак и показала мне кузнечика, который почти сразу же прыгнул в мою сторону, только очутившись на свободе!"
    ivan "А{w=.1}-а{w=.1}-а!"
    "Я неслыханно испугался из-за эффекта неожиданности и моей сильной усталости, которая совсем не помогала мне реагировать на происходящее быстро и трезво."
    if sch_day1_sl_together:
        show sl laugh pioneer with Dissolve(0.25)
        show sl serious pioneer with Dissolve(0.25)
        "Славе стало смешно от того, как мне стало страшно, и она на секунду рассмеялась, ещё быстрее восстановив серьёзную мину."
        sl "Ульяна!"
        $ sch_meet('us', 'Ульяна')
        us "Чего изволите, старший помощник вожатой?"
        "Славя никак не отреагировала на дразнилку, и снова повторила имя рыжей."
        sl "Ульяна!"
        show us dontlike pioneer:
            xalign 0.5
            ease 0.5 xalign 0.33 # поправить
        us "Ну что-о-о?"
        "Мелкая сморщилась и злобно посмотрела на мою проводницу, собираясь скорее уже дать дёру."
    else:
        show us dontlike pioneer:
            xalign 0.5
            ease 0.5 xalign 0.33
        "Немного оклемавшись, я чуть не стукнул мелкую по голове, но, к счастью для неё, она отпрыгнула."
    show sh normal pioneer at right with dissolve
    "Вскоре, кто-то в клубах услышал нашу словесную перепалку и вышел."
    sh "Что за шум, а драки нет?"
    "Из клубов вышел именно тот человек, которого я ожидал бы увидеть в клубе пающего очередную микросхему."
    "Русые волосы, очки, сдавившие переносицу так, что она явно покраснела, и недоумевающий вид - набор сумасшедшего гения готов!"
    "Парень осмотрел нас и отвёл взгляд на рыжую."
    # Итоговая картина - Славя слева, Ульяна в центре, Шурик справа # Исправить!!!!!!!!!!!!!!!!!!!!!!!!
    sh "Ульяна! Ты чего опять удумала?"
    $ sch_meet('us', 'Ульяна')
    




label dr_day1_afterod:
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_house_of_mt_day with dissolve
    "Стоило мне переступить порог домика вожатой и прикрыть за собой дверь, как я чуть ли не сразу повалился с лестницы и прыгнул в лежак, так удобно лежащий около входа."
    "Славя по настоянию Ольги Дмитриевны уже убежала на склад, чтобы я по прибытию не тратил время попусту."
    "Проблема была в том, что карту мне так и не выдали, и оставили с чутьём городского жителя искатьц нужное мне место самому."
    "Нет, топографическим кретинизмом я не страдал, однако же мне нужно хотя бы примерное направление движения."
    "Ещё несколько минут я валял дурака, но моя весенняя одежда не особо помогала насладиться летним солнцем, и мне пришлось подняться."
    iv "Надо бы спросить у кого-нибудь дорогу."
    scene bg ext_square_day with dissolve
    "Ведомый этой мыслью, я пошёл на самое людное место - на площадь."
    "Смотреть на неё со стороны было поначалу странно, однако развернувшись лицом к Генде, всё встало на свои места - я снова не знаю, куда мне идти, и только мессия подскажет путь в Асгард."
    "На моё неудивление, в тихий час площадь была абсолютно пустой."
    show dv normal pioneer2 far:
        xalign 1.5
        ease 0.75 xalign 0.5
    "Поэтому Двачевскую, немного согнувшуюся и идующую быстрым шагом, я остановил почти сразу же, как заметил."
    ivan "Рыжая!"
    if sch_ginger_lie: # изи путь в библиотеку
        show dv angry pioneer2 far with dspr
        dv "Что надо?"
        "Видимо, она злилась на меня за то, что я соврал по поводу местоположения Ульяны."
        ivan "Да не дуйся ты! Я думал, ты поймёшь шутку!"
        dv "За такие шутки..."
        ivan "Всё-всё, понял. И вообще, у меня к тебе дело есть."
        dv "И с чего это я буду тебе помогать?"
        ivan "Да ну, пионер всегда должен помочь ближнему своему! Нужно всего лишь указать направление!"
        "Алиса преобразилась и уже была готова отправить меня по грибы."
        dv "А, ты не знаешь, куда тебе идти? Так я тебе скажу, куда!"
        ivan "Скажи лучше, в какую сторону склад."
        show dv normal pioneer2 far with dissolve
        dv "И что мне будет за это?"
        ivan "Двачевская, давай без этого!"
        dv "Склад - там."
        "Она пальцем показала куда-то правее массива домиков, из которого я только что унёс ноги."
        ivan "Спасибо..."
        "Но не успел я окончить фразу, как рыжая куда-то убежала."
        iv "Ну и ладно."
    else: # изи путь в музклуб
        dv "Что надо?"
        "Она определённо куда-то торопилась, так что в моих интересах было как можно быстрее выпытать нужную мне информацию."
        ivan "Не подскажешь, в какой стороне склад?"
        dv "Тебе налево."
        ivan "Что?"
        show dv angry pioneer2 far with dspr
        "Алиса посмотрела на меня, как на идиота."
        dv "Ты тормоз?"
        ivan "Эй, я тут вообще-то впервые!"
        show dv girn pioneer2 far with dspr
        dv "А, то есть тебя не учили, где право и где лево?"
        ivan "Скажи, относительно чего мне налево идти-то."
