def main():
    d = {'website': 'google', 'url': 'google.ru'}
    try:
        data = d['url']
    except Exception:
        data = 'htts://'
        return data
    else:
        data = data.upper()
    print(data)

print(main())
