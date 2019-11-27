from urllib.parse import urlparse

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2]+'.'+results[-1]
    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except :
        return ''

print(get_domain_name('https://web.telegram.org/?utm_source=web_app_manifest#/im?p=u777000_13906695816728093379'))
