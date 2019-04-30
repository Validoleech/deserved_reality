label dr_day1_intro:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ sch_newday(sch_dayNo=1)
    $ name_sch('Я')
    scene anim prolog_2
    show yellowish:
        alpha 0.5
    with fade
    "Я чувствовал себя утопленником."
    "Тьма. Отсутствие гравитации, непонятная тяжесть по всему телу и отсутствие воздуха."
    "Здесь отказывали все органы восприятия человека, и только какое-то чутьё намекало на возможность выхода."
    play ambience ambience_ext_road_day fadein 10
    "Пустота и боль на месте шва сменилась ощущением нахождения на жестком автобусном сидении, в глаза начал бить яркий желтоватый свет."
    scene expression Sepia('bg int_bus') behind unblink
    show unblink with Dissolve(0.1)
    pause(1.5)
    scene bg int_bus with flash
    "И глаза я открыл уже в другом месте - меня не окружал мой город, окружённый холодными оттенками розового заката."
    hide unblink
    "Сиденья цвета кофе с молоком, жестяной рифлёный пол, подлокотники у передних кресел подняты, красные вельветовые шторы - казалось, что потолок ниже и прижимает салон всем своим весом."
    iv "Довольно жёсткие тут сидячие места, однако."
    ivan "А-апчхи!"
    "А ещё тут было довольно пыльно."
    iv "И ни черта из окон не видно."
    iv "И вообще похоже на какой-то Икарус, если честно."
    iv "Олег Степа…"
    iv "Какой к чёрту Икарус?! Кто такой Олег Степанович?"
    iv "Что со мной было?"
    show prologue_dream with dissolve
    "Я напряг виски и пытался вспомнить."
    "Первым вопросом на повестке дня была совсем не фраза \"где я?\", хотя и она довольно быстро всплыла во всё ещё неадаптировавшемся к резко изменившимся условиям мозгу."
    "Интересовало меня другое."
    iv "Кто я?"
    "В голове был сплошной белый шум да непонятная девочка в оборваном коричневом платьице."
    "Сначала было довольно трудно вспомнить даже имя, но за ним потом нашлось и отчество - вместе они звучали, как у героя одного советского фильма, который влетел в мой мозг следующим воспоминанием из детства."
    $ name_sch("Ваня")
    "Дразнилки в первом классе и шутки про то, что я меняю профессию."
    "Кадры начали набирать обороты - и в считанные секунды мимо меня пронеслась вся моя жизнь."
    "Аметист, операция над глазами, и чёртова девочка - она не покидала меня ни на одном кадре моего существования."
    "Она была активным участником всего - но при этом её никто не замечал. Будто её и не было никогда."
    "А вот одно из недавних воспоминаний - я пишу о том, что меня посетила тульпа и я на всякий случай пишу завещание. На неэлектронной бумаге. Обычной ручкой."
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
    "Тревожные мысли усиливались воспоминанием о совершённом за момент до появления здесь."
    iv "Я вступил в бездну. По сути я просто покончил с собой. И всё ради свободы мысли."
    iv "Но как я сейчас жив? Или, быть может, я сейчас в коме и всё - иллюзия угасающего сознания?"
    iv "В любом случае, мне придётся так или иначе осмотреться."
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
    "В пионерлагере?!"
    iv "Что, простите? Это какая-то шутка?"
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
    iv "Ладно, хватит смотреть на произведения искусства. Я не очень хочу тут задерживаться."
    "Я уже собирался зайти за ворота, как они приоткрылись, и из них вышла девушка. Красивая."
    show sl smile pioneer far with dissolve
    "Красивая девушка была одета в типичную пионерскую форму - тёмно-синяя юбка, туфли, блузка и главный символ пионерии и процветающего марксизма-ленинизма - яркий, красный до кончиков треугольной ткани пионерский галстук."
    "Среди особенностей самой девушки можно было ответить очень длинные косы из блондинистых, почти золотых волос, а также яркие голубые глаза."
    # Если я вдруг спрошу себя, почему сценарий находится за комментариями, то ответ меня из прошлого будет прост - РАНЬШЕ БЫЛО ЗАДУМАННО ИМЕННО ТАК
    #"Но несмотря на всю её привлекательность, общаться с ней совсем не хотелось."
    #"Она была представителем райских людей, которые использовали свою внешность, чтобы получить что-то за бесплатно."
    #"Ох, и сколько моих друзей делали таким небожительницам бесплатные услуги - всё ради \"спасибо\", смайлика-сердечка в личных сообщениях и чёрному списку через неделю игнорирования."
    #"В реальности это работает немного иначе, но общий концепт не меняется - тебя оставляют ни с чем."
    #"Омрачённый плохими воспоминаниями, я собирался просто обойти её, однако она заняла прочную позицию прямо напротив входа и игнорировать её было бы моветоном."
    show sl surprised pioneer far with dissolve
    sl "Что-то не так?"
    "Погружённый в мысли, я на некоторое время впал в ступор, услышав её голос."
    ivan "А, что? Нет, извини... те."
    sl "Можно и на ты. Ты ведь новенький? Я Славяна, но все зовут меня Славей."
    "Девушка располагала к себе с первых секунд - неплохое достижение для человека с отточенным до автоматизма приветствием".
    #TODO




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
