import re
import string

from anyway.models import TagsList, NewsFlashTags

TAG_TO_RELATED_WORDS = dict(
    minor_injuries = ['קל'],
    moderate_injuries = ['בינוני-קשה' ,'בינוני'],
    severe_injuries = ['קשה', 'אנוש'],
    injured = ['נפגעה', 'נפגע', 'פצועות', 'פצועים', 'פצועה', 'פצוע', 'נפצעו', 'נפצעה', 'נפצע'],
    deadly_accident = ['מותן', 'מותם', 'מותה', 'מותו', 'מות', 'מוות', 'קטלני', 'קטלנית', 'הרוגים', 'הרוגה', 'הרוג', 'נהרגו', 'נהרגה', 'נהרג'],
    hit_and_run = ['פגע וברח'],
    frontal_accident = ['חזיתית'],
    overturned = ['התהפכות', 'התהפך', 'התהפכה'],
    male = ['גבר', 'גברים', 'צעיר', 'נהג', 'הולך רגל', 'ילד', 'נער', 'פעוט', 'תינוק', 'קשיש', 'רוכב'],
    female = ['אישה', 'צעירה', 'נהגת', 'הולכת רגל', 'ילדה', 'נערה', 'פעוטה', 'תינוקת', 'קשישה', 'רוכבת', 'אשה', 'נשים'],
    child = ['ילד', 'ילדה', 'ילדים', 'ילדות', 'תינוק', 'תינוקת', 'פעוט', 'פעוטה'],
    elder = ['קשישה', 'קשיש'],
    pedestrians = ['הולכות רגל', 'הולך רגל', 'הולכת רגל', 'הולכי רגל'],
    bus = ['אוטובוס'],
    truck = ['משאית', 'מערבל בטון', 'רכב משא'],
    taxi = ['מונית'],
    tractor = ['טרקטור', 'טרקטורון'],
    motorcycle = ['קטנוע', 'אופנוע'],
    atv = ['טרקטורון'],
    private_driver_vehicles = ['מכונית', 'רכב'],
    bikes_and_scooters = ['אופניים', 'קורקינט'],
    electric = ['חשמליים', 'חשמלי'],
    night = ['הערב', 'הלילה'],
)
REGEX_EXPRESSION = r'\s?{} '
TAG_NAME_TO_ID = {tag.tag_name: tag.tag_id for tag in TagsList.query.all()}


def extract_tags_from_desc(data):
    tags = []
    # Strip punctuation for regex purposes
    data = data.translate(data.maketrans('', '', string.punctuation))
    for tag, related_words in TAG_TO_RELATED_WORDS.items():
        for word in related_words:
            if re.search(REGEX_EXPRESSION.format(word), data):
                tags.append(tag)
                break
    return tags

def save_tags_to_db(tags, news_flash_id):
    for tag in tags:
        NewsFlashTags(
            news_flash_id = news_flash_id,
            tag_id = TAG_NAME_TO_ID[tag],
        ).save()

def extract_and_save_tags(news_flash_obj):
    tags = extract_tags_from_desc(news_flash_obj.description)
    save_tags_to_db(tags, news_flash_obj.id)
