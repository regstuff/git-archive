# git-archive
Save offline archives of webpages with Github Actions & [Monolith](https://github.com/Y2Z/monolith). Archive by creating a Github issue, or through your browser omnibox's search shortcuts.

## Setup
### To archive via Github issues
1. [Fork this repo](https://github.com/regstuff/git-archiver/fork). 

### To archive via browser omnibox
1. [Fork this repo](https://github.com/regstuff/git-archiver/fork). 

2. Create a [Github access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

3. [Set up Github Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-your-site) for your repo. Wait 5 minutes for Github to make your page live. 

## How-to archive
### Via Github issues
In your repo, create an issue with the url as the title (Eg. https://cnn.com/)

That's it! Github Actions triggers Monolith to download the webpage and store it as a single file in the html folder.

**Note:** Make sure you include http(s):// in the issue title.

### Via browser omnibox 
Open this in your browser: https://YOUR_USERNAME.github.io/git-archiver/YOUR_GITHUB_ACCESS_TOKEN/?archiveurl=https://the-url-you-want-to-archive

Replace with your username, the access token you created & the appropriate url to archive. (Eg. https://regstuff.github.io/git-archiver/ghp_abcd1234/?archiveurl=https://cnn.com)

That's it! The custom 404 page creates the new issue and triggers Github Actions.

Most browsers allow you to [add a custom search engine](https://support.google.com/chrome/answer/95426?hl=en), which can be triggered by a short code in the omnibox. You can set this up as a shortcut to the archiver, by setting the search engine url to https://YOUR_USERNAME.github.io/git-archiver/YOUR_GITHUB_ACCESS_TOKEN/?archiveurl=%s (in Chrome/Chromium browsers. Similar things are possible in Firefox [through Mycroft](https://support.mozilla.org/en-US/kb/add-or-remove-search-engine-firefox#w_mycroft-project-search-engine-plugins)).

## Options
**Monolith Flags:** Flags default to -ifave (ignore images, video, audio, frames and network errors). Change your default in config.json

**Per-url Flags:** You can override the default flags on a per-url basis. Just add :: to the end of the url, followed by the flags you want. 

   Eg 1. https://cnn.com::jc - ignore javascript and css.

   Eg 2. https://cnn.com:: - Monolith runs without any flags. Audio & video will be downloaded as well. Watch your repo size!

**Collaborative Archiving:** By default, only issues created by the repo owner trigger the archiving workflow. To add additional users, add to the allowed_users list in config.json. Eg. ["someone", "someone-else"]

**Archive to Wayback Machine:** Set the 'wayback_archive' flag to 'yes' or 'no'. You'll need to create an account at archive.org and generate your keys at https://archive.org/account/s3.php Then [add them](https://github.com/regstuff/git-archive/settings/secrets/actions/new) as repository secrets named WAYBACK_S3_ACCESS & WAYBACK_S3_SECRET 

## Security
1. If you're using the browser method, make sure no one sees your access token. To limit the damage in such situations, make sure you restrict the personal access token's scopes to repo (preferably public repo), when creating the token.

2. If you don't want people to see what you've archived, make your repo private. Github pages are still public, even for private repos. You can either disable Github pages (you won't be able to use the omnibox method), or add basic authentication (don't forget to add the login:password to the url in your omnibox & search shortcut).

**Note:** Free Github accounts are limited to 2000 build minutes/month across all private repos. Should be plenty, but keep an eye on your quota.

## Github storage limits
How much space does Github give you? [Github says](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#repository-size-limits): "We recommend repositories remain small, ideally less than 1 GB, and less than 5 GB is strongly recommended."

Assuming each webpage is 1-1.5 MB on average, that means 600-1000 webpages for 1 GB, or 3000-5000 pages for 5 GB.

More interesting details over at [Stackoverflow](https://stackoverflow.com/a/59479166/3016570).
   
To save on space, check out Monolith's [many flags](https://github.com/Y2Z/monolith#options). Low-hanging fruit includes -c & -j (exclude CSS & Javascript). 

## To-Do
1. Add fulltext search functionality for all archived pages.

2. Config option to list archived pages on project page.

3. Use issue labels to categorize archived page

4. Per-url auto-archive to wayback machine

5. Detect the result of actual archiving workflow and pass it to the 404 page & issue
