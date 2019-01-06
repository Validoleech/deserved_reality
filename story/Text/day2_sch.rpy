label sch_day2_start:

    $ persistent.sprite_time = "day"
    $ day_time()

    "Жарко, душно, голова болит неистово..."

    ivan "Где я?"

    iv "Кажется, я начинаю вспоминать..."
    "Я открыл глаза."

    ivan "А, точно."
    ivan "Поехал в экспедиию и утопился в снегу. Буквально. Брр. Холодно вспоминать даже."

    iv "Очнулся - глюки. Бэдтрип."
    "Повторил я про себя на всякий случай."
    "Непривычно-неудобная кровать своим скрипом вернула меня в суровую реальноссть. Прощай, сон. Снова расстаемся. Бог даст, еще свидимся."
    "Я ещё раз осмотрелся."

    ivan "Так-так, и что тут у нас?"

    if sch_clock:
        "Часы на столе с приятной неоновой подсветкой указывали на то, что сейчас около шести часов утра."
        "А вожатой всё еще нет."

    else:
        "Вожатой... как там её? Ольги Николаевны? Нет, Ольги Дмитриевны на кровати не было."
        "Зато на спинке кровати висел неприлично большой предмет нижнего белья. Кстати, довольно милый. Розовый, с кружевными цветочками. А под ней лежал огромный молот. У меня бы его назвали банхаммером."
        iv "Видимо, не всё выветрилось из моего извращённого интернетом мозга."

    iv "Либо она не человек, либо летучки проходят настолько рано."
    ivan "Anyway..."
    "Он говорит на расово и национально неверном языке! Захватить - и к стенке!"
    ivan "Мой мозг по утрам - самый мощный генератор пошлых мыслей и тупых идей."
    iv "А тем временем лучше бы он включил в моих глазах автофокус и нашёл новую форму."
    "Через десять секунд отыскалась и моя форма, лежащая в груде других интересных вещей."
    "Что у нас будет?"

    if 'el' or 'sh' in list_sch_ch_known:
        "Судя по одежде пионеров, меня ждёт очередное и самое привычное унижение."
        "И тугой пионерский галстук, затянутый над моей шеей мертвым и цепким узлом."

    else:
        "Пожалуйста, пусть это не будет походить на летний вариант школьной формы!"
        "..."
        iv "Кажется, я умею предсказывать будущее."

    "С другой стороны, что ещё можно было ожидать?"
    if pt_sl >=4 and sch_day1_aidpost:
        "Типичные шорты и рубашка, идеально подобранные по моему размеру, аккуратно висели на спинке стула, стоящего возле моей кровати."
        "Почему-то мне не представляется возможным, что Ольга Дмитриевна за 3 минуты знакомства со мной смогла так идеально определить мой размер одежды."
    "Типичные шорты и рубашка, идеально подобранные по размеру зорким глазом, видимо, вожатой."
    iv "\"Воротничок настолько белый и хрустящий, что даже нацисты сомневаются в чистоте своей расы.\""
    "А ещё он сшит из чистого хлопка и скрипит не меньше, чем кровать, на которой я провел самую странную ночь в моей жизни."
    "В карманах шорт я обнаружил довольно большой, но аккуратно сложенный платок."
    "Завязывать галстук по-пионерски меня ещё учила моя бабушка, хоть СССР уже давным-давно распался."
    ivan "Никогда бы не подумал, что мне пригодится навык завязывать пионерский галстук."

    if not sch_day1_aidpost:
        "Я подошёл к шкафу, в зеркале которого увидел своё обновлённое лицо второй раз в жизни."
        iv "На самом деле, сейчас я выгляжу немного лучше, чем вчера."

    else:
        "Я открыл шкаф в поисках своей одежды, но отвлёкся на небольшое зеркало, прикреплённое к выдвижной створке."
        iv "Однако, я неплохо выгляжу!"

    "Моя куртка (странно, что не спросили, откуда я приехал!) висела на деревянной вешалке, идеально выглаженная и чистая, без пятен талого снега, а содержимое моих карманов находилось тут же, на тумбочке рядом с кроватью."

    if sch_keys:
        "Славины ключи, к счастью для самой Слави, у меня не обнаружили, а потому они спокойно лежали в углу ящика."
        "И всё-таки я чувствую, что им комфортнее в соседнем кармане с моим телефоном."
        "Как камера или фонарик он ещё может пригодиться. А ключи - тем более!"

    else:
        "Вооружившись телефоном, который мог послужить лишь камерой или фонариком, и пакетиком с явным запахом мыла и прочих очистительных принадлежностей, я направился к умывальникам."

    # фон
    "Лагерь спал. Не то чтобы там было несколько сонных пионеров, нет - лагерь казался пустым и сопел из каждого домика и затягивал в такое же настроение меня."
    "Мой режим сна не пропьёшь."
    "Сейчас в лучшем случае пол седьмого, до пробуждения масс ещё полтора часа."
    ivan "Свобода, тишина, свежий воздух."
    "Старому мне она могла и приесться, но тот Ванька, в чём теле я нахожусь, явно получал тонну удовольствия от вдыхания почти идеального сочетания кислорода и азота, в котором примесям места просто не было."
    "Огранизм всё ещё не мог привыкнуть к этим условиям, поэтому голова немного кружилась."
     iv "Как сказал бы Олег Степаныч: \"тебе нужно с собой выхлопную трубу брать\"."
    "И после этого залился бы громким неостановимым смехом. Олежка, двацать девять лет."
    "Человек, который подтолкнул меня к нынешнему состоянию. Может быть, без него я бы сейчас и не попал в это райское место."


    # умывальники

    "В раздумьях я добрался до умывальников."

    ivan "Ставлю тысячу рублей на то, что вода тут будет ледяная."
    sl "Вот это ставки!"

    show sl smile2 sport at left with dissolve

    "Славя появилась из ниоткуда, то ли подкравшись со спины, то ли следуя за мной из интереса. Как кошка."
    "Я чуть ли не рефлексивно отскочил и оберунлся в её сторону."
    "Блондинка была одета в спортивную форму, похожую на фирменный Adidas - чёрно-белые ультра короткие шорты и футболка с двумя полосками по бокам."
    "Врать не буду - в пионерской форме она выглядит отлично, а в этих шортиках ещё лучше!"

    ivan "Мне кажется, или такую брендовую одежду в СССР не продают?"
    sl "Мне Мику подарила в этом году, она второй раз приехала и знала, что мне было бы неплохо сменить спортивную форму."
    ivan "Сама щедрость. А ты который раз тут?"
    sl "Где-то четвертый."
    ivan "Ты же вроде образцовая пионерка, помощница вожатой, разве тебя не должны были отправить в лагерь поприличнее?"

    show sl normal sport at left with dspr

    sl "Мне предлагали."
    ivan "И ты?"

    show sl sport laugh at left with dspr

    sl "И я взяла и уехала в Артек! Видишь, меня нет!"
    ivan "Издеваешься над невыспавшемся человеком."

    show sl normal sport at left with dspr

    sl "Кстати, с чего это ты так рано умываться идёшь? Спать не давали?"
    ivan "К тебе тот же вопрос."

    show blink

    "Она в чём-то была права - спать я себе не давал - слишком много думал."

    show unblink
    hide blink

    sl "Я привыкла просыпаться и совершать пробежку, пока все спят и Ольга Дмитриевна не начала новый день в лагере и не заняла меня."
    ivan "Это не кажется тебе экспуатацией?"
    sl "Ты что, она минуты с вами отдохнуть не может!"
    iv "Что-то мне не особо верится."
    sl "А ты?"
    ivan "Что \"я?\""
    sl "Почему так рано проснулся?"
    ivan "Режим сна, который у меня установлен, я даже снотворным не нарушу."
    sl "Ранняя пташка?"
    ivan "Можешь и так назвать."
    ivan "Может, всё же пропустишь? Я десять минут уже жду, когда одна особа перестанет блокировать проход к живительной водичке."
    show sl tender sport with dspr:
        xanchor 0.5
        pause 0.5
        easein 0.5 xanchor 0.0
    sl "Прости."
    hide sl with dissolve
    "Славя скрылась за моим полем зрения."
    ivan "Раз, два, три!"
    "Б-р-р-р!"
    "Холодная, чёрт возьми!"
    "Я, наверное, за весь свой опыт геологом такую холодную воду не встречал, тем более летом."
    ivan "One, two, three!"
    "По сути я просто подбрасывал воду к лицу, так как руки просто замерзали, и пальцы больше походили на неподвижные крючки."
    ivan "Ein, zwai... Славя!"
    "Я резко развернулся, услышав как тихие прыски в кулак превратились в смех."
    show sl smile2 sport with dissolve
    sl "Всё, ухожу, ухожу!"
    show sl tender sport with dspr:
        xanchor 0.5
        pause 0.5
        easein 0.5 xanchor 1.0
    "В этот раз я проследил, чтобы Славя ушла."
    hide sl with dissolve
    "Хоть я и не уверен, что она всё ещё следит за мной."
    "Никакой личной жизни."
    "Я достал из пакетика зубной порошок. {nw} А потом посмотрел на раковину с жидким льдом."
    iv "Если бы мои зубы имели разум, они бы резко начали дергать нервную систему, чтобы я потерял сознание от шока и не обливал их такой холодной водой."

    with fade

    $ renpy.pause(1, hard=True)

    "На самом деле, всё было не так уж и плохо."
    "По крайней мере, могло быть и хуже."
    iv "Хорошо, план-минимум выполнен."
    "Может, Славя была права и мне стоит пойти покемарить ещё часик, пока могу?"

    menu:
        "Да, определённо спать":
            # фон
            "С этой мыслью я двинул обратно в сторону домика."
            "Некоторые жильцы домиков уже просыпались и не давали спать другим."
            #внешка домика
            "Летняя сирень, красота."
            "Я осторожно открыл дверь, и..."
            # цг ОД переодевается
            iv "Вот это вид!"
            iv "Четвертак бросаешь в приёмник, и дверная скважина открывается - это мог быть такой хороший заработок!"
            "Хорошая новость - меня не заметили."
            "Плохая новость - ни организм, ни я не хотели закрыть дверь."
            iv "Нет-нет-нет и ещё раз нет. Нельзя."
            iv "Моя рука закрывает дверь."
            iv "Я сказал, что моя рука берёт ручку и закрывает дверь..."

            if pt_wi >= 20:
                if pt_ka >= 20:
                    $ sch_day2_od_photo = True
                    "Возможно, что мы ещё аккуратно достаём второй рукой телефон и делаем быстрый снимок..."

                else:
                    "Возможно, я мог попытаться сфотографировать, но..."

                iv "Теперь точно закрыли дверь!"
                "Ни единого скрипа петель или щелчка замка."
                ivan "Фух..."
                "Я приземлился на шезлонг так же бесшумно."
                iv "Так нельзя - определённо. Я в свой возраст так бы сделал - определённо нет."
                iv "Экспериментально проверили, что гормоны контролировать я не могу."
                iv "Или экстремально. Или..."

                show black with fade

                $ renpy.pause(1, hard=True)

                "Меня кто-то толкнул за плечо."
                hide black
                show unblink
                "Пришлось открывать глаза."
                # фон и вожатая
                mt "Ваня, вставай, проснись и пой! Сегодня для тебя начинается первый полноценный день в нашем лагере!"
                ivan "На самом деле, не очень хорошая мотивация."
                mt "Не проснулся? Ничего. Умываться ходил уже?"
                ivan "Да, мам."
                # недобрая ОД
                mt "Не фамильярничай со своей вожатой."
                ivan "Извините, исправлюсь и докажу."
                "Вставать с шезлонга не хотелось совершенно. Да и отвечать на фразы вожатой тоже."
                mt "Вставай давай. Через пятнцадцать минут линейка."

            else:
                #цг вожатая обернулась
                "Вожатая обернулась."
                mt "Что? {w} Иван!"
                "Я хлопнул дверь и побежал в сторону умывальников под крики вожатой."
                # Фон
                "Чем холоднее, тем лучше!"
                "Я умылся пару раз, чтобы остудиться и оценить ситуацию."
                iv "При встрече меня ждёт а-та-та, но только если я окажусь с ней один на один. Либо же она предпочтёт не разглашать то, о чём могут подслушать различные разведчики."
                ivan "В любом случае, лучше перестраховаться."
                iv "Кстати, надо посмотреть, что тут за лес. Вчера я туда попасть не смог."
                iv "Заодно и посмотрю, насколько это живописная местность."
                $ sch_day2_forest = True
                $ sch_day2_od_failed = True
                return
            return


        "Прогулка придаст бодрости!"
