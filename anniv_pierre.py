import requests
print(''.join([chr(sum([sum([ord(a) for a in b]) for b in requests.get(lol)]) % 256) for lol in ['http://83.152.244.50/']]))