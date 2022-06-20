import os, sys, json
print('Arguments:',sys.argv)

fullurl = sys.argv[1]
url = fullurl.split('::')[0]
if url[-1] == '/': url = url[:-1]

commenter = sys.argv[2]
print('Commenter:',commenter)

owner = sys.argv[3]
print('Owner:',owner)

with open('config.json') as json_file: config = json.load(json_file)
default_flags = config['default_flags']
print('Monolith Default Flags:',default_flags)

if url[-5:] != '.html': fname = 'html/' + url.replace('/', '_-_') + '.html'
else: fname = 'html/' + url.replace('/', '_-_')

if '::' in fullurl and fullurl.split('::')[1] != '': monolith_command = f'chmod +x monolith && ./monolith {fullurl.split("::")[1]} {url} -o {fname}'
elif '::' in fullurl: monolith_command = f'chmod +x monolith && ./monolith {url} -o {fname}'
else: monolith_command = f'chmod +x monolith && ./monolith -ifave {url} -o {fname}'
  
print('Executing:',monolith_command)
monolith = os.popen(monolith_command).read()
