def extract_language(lang):
    lang = lang.split('.')
    lang.lstrip(*_)[0]
    return lang


print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))



