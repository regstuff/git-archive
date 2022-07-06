import os, sys, json, requests
from requests.structures import CaseInsensitiveDict

print('Arguments:',sys.argv)

fullurl = sys.argv[1].strip()
url = fullurl.split('::')[0].rstrip()
if url[-1] == '/': url = url[:-1]

creator = sys.argv[2]
print('Issue creator:',creator)

owner = sys.argv[3]
print('Owner:',owner)

with open('config.json') as json_file: config = json.load(json_file) # Get config json
config['allowed_users'].append(owner) # Include owner in list of allowed users
print('Config allowed users:', config['allowed_users'])

if creator in config['allowed_users'] and ' ' not in url and (url[:7] == 'http://' or url[:8] == 'https://'): # Check if whoever created the issue is in the allowed users list, and whether the url is valid
  default_flags = config['default_flags'] # Default flags to run Monolith with
  print('Monolith Default Flags:',default_flags)
  
  wayback_archive = config['wayback_archive'] # Whether url is to be archived in Wayback Machine
  print('Archive to Wayback machine:', wayback_archive)
  
  fname = 'html/' + url.replace('http://','').replace('https://','').replace('/', '%2F') + '.html' # Filename to save the archive to

  if '::' in fullurl and fullurl.split('::')[1] != '': monolith_command = f'chmod +x monolith && ./monolith -{fullurl.split("::")[1]} {url} -o {fname}' # Are there any url-specific Monolith flags?
  elif '::' in fullurl: monolith_command = f'chmod +x monolith && ./monolith {url} -o {fname}' # Was a url specific blank monolith config prescribed?
  else: monolith_command = f'chmod +x monolith && ./monolith -{default_flags} {url} -o {fname}' # Default operation

  print('Executing:',monolith_command)
  monolith = os.popen(monolith_command).read() # Run Monolith
  print('Monolith executed')
