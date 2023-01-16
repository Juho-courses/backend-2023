import requests
parit = {
    'koulu': 'SAMK',
    'vuosi': 2023,
}

print(parit['koulu'])
parit['asd'] = 12312
print(parit)

r = requests.get('https://www.samk.fi')
