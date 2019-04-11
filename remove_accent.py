import unicodedata

def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD',text).encode('ascii','ignore')\
        .decode('utf-8','ignore')
    return text

#The normal form KD (NFKD) will apply the compatibility decomposition, i.e. \
# replace all compatibility characters with their equivalents.

accented_text = 'Sómě Áccěntěd těxt'

non_accent_text = remove_accented_chars(accented_text)
print(non_accent_text)