import os, sys
url = sys.argv[1]
fname = 'html/' + url.replace('/', '_-_') + '.html'
monolith = os.popen(f'chmod +x monolith && ./monolith -aevf {url} -o {fname}').read()