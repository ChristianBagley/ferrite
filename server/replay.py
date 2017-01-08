import xml.etree.ElementTree
from readability import Document
from langdetect import detect

from models import Visit
from database import db_session

LANG = {
    'en': 'english',
    'fr': 'french'
}


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


for v in Visit.query.all():
    doc = Document(v.raw_dom)
    v.extacted_text = remove_tags(doc.summary())
    v.lang = LANG.get(detect(v.extacted_text), 'simple')

db_session.commit()
