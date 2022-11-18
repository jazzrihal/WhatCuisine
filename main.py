import requests
import time
import random
from pathlib import Path


path = Path.cwd() / 'history.txt'
if not path.exists():
  path.touch()
with open(path, 'r') as f:
  hit_countries = []
  for ln in f:
    hit_countries.append(ln)

response = requests.get('https://restcountries.com/v3.1/all').json()
no_of_countries = len(response) + 1

print(f'Found {no_of_countries} countries')
print('Selecting country at random...')
time.sleep(5)

found_new = False
while not found_new:
  i = random.randint(0, no_of_countries - 1)
  selected_country = response[i]['name']['common']
  
  if selected_country not in hit_countries:
    found_new = True

print(f'You\'re eating in {selected_country}')

with open(path, 'a') as file:
  file.write(
    f'\n{selected_country}'
  )
  