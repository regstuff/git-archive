# git-archive
Save offline archives of webpages with Github Actions & [Monolith](https://github.com/Y2Z/monolith).

## How-To
1. [Fork this repo](https://github.com/regstuff/git-archiver/fork). In your repo, create an issue with the url as the title (Eg. https://cnn.com/)

2. That's it! Github Actions triggers Monolith to download the webpage and store it as a single file in the html folder.

OR
1. [Fork this repo](https://github.com/regstuff/git-archiver/fork). Open this in your browser: https://YOUR_USERNAME.github.io/git-archiver/YOUR_GITHUB_ACCESS_TOKEN/?archiveurl=https://the-url-you-want-to-archive
   
   Replace with your username, Github access token ([see this](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) on how to generate) & the appropriate url to archive.  
   (Eg. https://regstuff.github.io/git-archiver/ghp_abcd1234/?archiveurl=https://cnn.com)

2. That's it! A custom 404 page creates a new issue and triggers Github Actions.

## IMPORTANT
1. To prevent random people from archiving stuff in your repo by opening issues, [limit issue creation](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository) to repo collaborators. This can be set to a maximum of 6 months. You'll need to reset it after that again.

2. If you're using the browser method, make sure no one sees your access token. To limit the damage in such situations, make sure you set the personal access token's scopes to repo (preferably public repo), when creating the token.

3. Most browsers allow you to [add a custom search engine](https://support.google.com/chrome/answer/95426?hl=en), which can be triggered by a short code in the focus bar. You can set this up as a shortcut to the archiver, by setting the search engine url to https://YOUR_USERNAME.github.io/git-archiver/YOUR_GITHUB_ACCESS_TOKEN/?archiveurl=%s (in Chrome/Chromium browsers. Similar things are possible in Firefox). Again, make sure no one sees your access token.

4. How much space does Github give you? [Github says](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#repository-size-limits): "We recommend repositories remain small, ideally less than 1 GB, and less than 5 GB is strongly recommended."

   Assuming each webpage is 1-1.5 MB on average, that means 600-1000 webpages for 1 GB, or 3000-5000 pages for 5 GB.

   A few more interesting details over at [Stackoverflow](https://stackoverflow.com/a/59479166/3016570).
   
   To save on space, check out Monolith's [many flags](https://github.com/Y2Z/monolith#options). Low-hanging fruit includes -i, -c & -j (exclude images, CSS & Javascript). Edit the -aevf part in main.py accordingly.

## To-Do
1. Add fulltext search functionality for all archived pages.
