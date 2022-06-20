import os, sys, json
print('Arguments:',sys.argv)

fullurl = sys.argv[1].strip()
url = fullurl.split('::')[0]
if url[-1] == '/': url = url[:-1]

commenter = sys.argv[2]
print('Commenter:',commenter)

owner = sys.argv[3]
print('Owner:',owner)

with open('config.json') as json_file: config = json.load(json_file)
default_flags = config['default_flags']
print('Monolith Default Flags:',default_flags)
config['allowed_users'].append(owner)
print('Config allowed user:', config['allowed_users'])

if commenter in config['allowed_users'] and ' ' not in url and (url[:7] == 'http://' or url[:8] == 'https://'):
  fname = 'html/' + url.replace('http://','').replace('https://','').replace('/', '_-_') + '.html'

  if '::' in fullurl and fullurl.split('::')[1] != '': monolith_command = f'chmod +x monolith && ./monolith -{fullurl.split("::")[1]} {url} -o {fname}'
  elif '::' in fullurl: monolith_command = f'chmod +x monolith && ./monolith {url} -o {fname}'
  else: monolith_command = f'chmod +x monolith && ./monolith -{default_flags} {url} -o {fname}'

  print('Executing:',monolith_command)
  monolith = os.popen(monolith_command).read()
