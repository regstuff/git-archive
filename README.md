# archive
Save offline archives of webpages with Github Actions & [Monolith](https://github.com/Y2Z/monolith).

## How-To
1. Create an issue with the url as the title (include http:// etc. Basically the fulltitle)
2. That's it!

Github Actions will trigger Monolith, which will download the webpage as a single file and store it in the html folder.

## To-Do
1. Add fulltext search functionality for all archived pages.

## Note
To prevent random people from archiving stuff in your repo by opening issues, [limit issue creation](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository) to repo collaborators. This can be set to a maximum of 6 months. You'll need to reset it after that again.
