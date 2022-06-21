import os, sys, json, requests
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
  
  if wayback_archive == "yes": #If config set to archive to Wayback machine
    url = "https://web.archive.org/save"
    
    # Documentation at https://docs.google.com/document/d/1Nsv52MvSjbLb2PCpHlat0gkzw0EvtSgpKHu4mk0MnrA/ & backup at https://gist.github.com/regstuff/82e690db2f1d91ba59f6681c1abad6cf
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"LOW {os.environment['WBACCESS']}:{os.environment['WBSECRET']}" # Generate your keys at https://archive.org/account/s3.php - you need to be logged into archive.org
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    data = f"url={url}" + "/&skip_first_archive=1" # Speed up the archiving process
    resp = requests.post(url, headers=headers, data=data)

    if resp.status_code == 200: print('Wayback archiving was successful, with message:', resp.json()['message'])
    else: print('Wayback archiving failed, with status code:', resp.status_code)
