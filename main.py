import os, sys
fullurl = sys.argv[1]
url = fullurl.split('::')[0]
commenter = sys.argv[2]
print('Commenter:',commenter)
owner = sys.argv[3]
print('Owner:',owner)
fname = 'html/' + url.replace('/', '_-_') + '.html'
monolith_command = f'chmod +x monolith && ./monolith -aevf {url} -o {fname}'
print('Executing:',monolith_command)
monolith = os.popen().read()
