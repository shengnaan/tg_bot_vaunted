import os

from aiogram.types import BotCommand
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TOKEN = os.getenv("TOKEN")
    PRAISES = [
        "ой ой ой кто разрешал тебе быть такой крошечной булочкой с начинкой из счастья???",
        "ты как Wi-Fi в кафе: как только ты рядом, всем становится лучше",
        "объявляю тебя официальным поставщиком хорошего настроения на планете Земля ☀️",
        "если бы твоя улыбка была песней, она бы играла в моём сердце бесконечно",
        "срочно выдайте этому котёнку (тебе!) медаль за очарование мирового уровня!",
        "ты как мармеладка — милая, сладкая, и без тебя всё как-то невкусно",
        "зайка, ты сияешь ярче, чем экран телефона на максимальной яркости ночью",
        "ты как утренний кофе — бодришь, согреваешь и делаешь день лучше",
        "если бы ты была приложением — то только с рейтингом 5.0 и миллионом сердечек 💖",
        "ты как редкая плюшевая игрушка: одна на миллион и самая любимая",
        "каждый раз, когда ты что-то делаешь, ангелы на небе хлопают в ладоши",
        "ты как зефирка, упавшая в какао — согреваешь душу и вызываешь умиление",
        "твоя доброта — это читы на любовь!",
        "ты не просто котик, ты котик в носочках, и это максимальный уровень милоты",
        "когда ты рядом, даже пасмурное небо делает 'оп' — и становится голубым",
        "ты как радуга после дождя: появляется неожиданно и делает всех счастливыми",
        "я тут подумал… может, ты фея??? иначе как объяснить твой волшебный эффект на всё вокруг?",
        "с тобой любое дело превращается в праздник, а любое настроение — в лучезарное",
        "твоя энергия — как обнимашки в дождливый день: тёплая, уютная и такая нужная",
        "если бы существовал конкурс 'Самый Милый Котик Вселенной'… ты бы заняла все три призовых места и ещё бонус за очарование",
        "ты такая милая, что даже ежики бросают свои иголки, чтобы тебя обнять",
        "ты — главный персонаж всех хороших снов и добрых сказок",
        "а ну перестань быть такой прекрасной, я не успеваю восхищаться!",
        "ты как конфетный магазин внутри облака — просто нереальная прелесть",
        "зайка, рядом с тобой даже у дождя настроение поднимается",
        "твои глазки? это портал в мир, где всегда уют, обнимашки и теплый плед",
        "ты как кнопка 'skip sadness' — стоит только тебя увидеть",
        "когда ты улыбаешься, где-то одинокий грустный пончик становится счастливым 🍩",
        "срочное обновление: ты — самая-пресамая, и точка! 🌈",
        "зайка я тебя луввв",
        "йо красотка чево грустим, а ну улыбнулась сальто сделала и балдеть быстро",
        "ой а кто такой мили мили китик",
        "даю право на один укус пети п если тебе грустно",
        "ты очен очен красивая!!!!",
        "ой мили китик лапкой тыкнул на кнопочку🥹🥹🥹",
        "ну ты ваще умничка у меня",
        "своей красотой весь мир радуешь",
        "вот представь себе такого миленького маленького котенка, вот это ты в моих глазах",
        "ты моя девочка сильная!!!!",
        "леее, милф0чка, чево такая seкси сегодня?",
        "это чтоооооо самый талантливый дантист???(да, она💅)",
        "Вам доступен купон на ∞ поцелуев, для получения приза обратитесь к пете п",
        "зайка, знай, что я всегда в тебя верю!!! ты все сможешь малышка!!!!",
        "сегодня точно все получится!!!",
        ". . . <котенок накакал и куда то убежал>",
        "мы (представь милых котиков)",
        "судя по гороскопу севодня ты великолепна (как вчера и завтра)",
        "зайка, ты сегодня официально самый прекрасный человечек!!! (и это не обсуждается)",
        "алё, это служба спасения? тут слишком красивая девочка, помогитеее",
        "ой ой ой кто это тут такая прелесность ходит??? это же ты!!!",
        "сегодня выдается специальный сертификат на обнимашки!!! держите 💌",
        "малыш, ты точно не волшебница? а то как объяснить твою магическую красоту...",
        "объявляю тебя самой-самой наивкуснейшей булочкой этого дня",
        "так, а кто тут самый лучший и талантливый? ой, да это же ТЫ!!!",
        "мяу мяу мур мур ты лапочка мур мур (это кошачий комплимент, если что)",
        "дайте дорогу!!! самая очаровательная принцесса идёт покорять мир!!!",
        "срочно вызываем бригаду обнимашек!!! тут котеночек грустит!!!",
        "ОПА! официальное предупреждение: ты сегодня слишком секси!!!",
        "ой, а кто это тут самая нежная зефирка? ну конечно же, ты!!!",
        "твоя красота нанесла мне критический урон... срочно нужны поцелуи для восстановления!!!",
        "зайка, ты как солнце… светишь, греешь и делаешь всех вокруг счастливыми!",
        "ты вообще понимаешь, насколько ты потрясающая??? спойлер: ОЧЕНЬ!!!",
        "каждый раз, когда ты что-то делаешь, мир становится чуточку прекраснее!",
        "ты не просто умничка, ты УМНИЩА с большой буквы!",
        "твои таланты — это что-то за гранью реальности, как ты это делаешь???",
        "зай, ты реально так хороша, что если бы была цветком, тебя бы берегли в ботаническом саду под охраной",
        "не знаю, осознаешь ли ты это, но ты — это ходячий мотиватор и вдохновение!!!",
        "ты настолько классная, что если бы тебя не существовало, мир был бы скучным!",
        "ты как маленькое солнышко — освещаешь всё вокруг своей красотой и добротой!",
        "ты такая умная, что я иногда думаю: а не гений ли ты, случайно?",
        "твой уровень крутости превышает все допустимые нормы, срочно оформляем награду!",
        "ты самая настоящая богиня, и точка. никаких возражений не принимается!!!",
        "серьезно, ты настолько хороша, что если бы была сериалом, у тебя был бы рейтинг 10/10 на всех платформах!",
        "если кто-то скажет, что ты не суперзвезда, просто знай — он врет!",
        "ты не просто умная, ты МЕГА-умная! настолько, что рядом с тобой даже искусственный интеллект тушуется!",
        "я каждый раз поражаюсь, насколько ты талантлива, будто у тебя читы на жизнь!"
    ]

    CAT_TAGS = ["cute", "funny", "sleepy", "play", "adorable"]
    MENU_COMMANDS = [
        BotCommand(command="/menu", description="Главное меню"),
        BotCommand(command="/meow", description="Картинка с китиком"),
        BotCommand(command="/praise", description="Похвалить"),
        BotCommand(command="/send", description="Написать пете п.")
    ]
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    NASTYA_ID = int(os.getenv("NASTYA_ID"))
