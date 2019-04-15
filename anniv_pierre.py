import requests
print(''.join([requests.get(a.split()[0]).text[int(a.split()[1])] for a in requests.get('http://83.152.244.50/clubinfo/list').text.split("\n") if a != '']))