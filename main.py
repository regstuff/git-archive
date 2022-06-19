import os
url = 'https://isha.sadhguru.org/in/en/wisdom'
fname = 'html/' + url.replace('/', '_-_') + '.html'
monolith = os.popen(f'chmod +x monolith && ./monolith -aevf {url} -o {fname}').read()
