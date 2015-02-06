Title: Making this website with Pelican
Date: 2015-02-05 15:14
Category: Programming
Tags: pelican, python, github
Slug: making-this-website-with-pelican
Authors: Santiago Chio
Summary: Path through making this website.

For the first article in the blog I'd like to explain the whole process that I made to set this website in
[GitHub Pages](https://pages.github.com/) with [Pelican](http://docs.getpelican.com/) a static site generator powered
by [Python](https://www.python.org/).

This will be a kind of tutorial/guide thought the [repository of this site](https://github.com/schiob/schiob.github.io).

#### Why Pelican and why GitHub Pages?
Because this website doesn't need a backend to fulfill its purpose, and because I don't want to mess around with a
server service (for now), I decided to host it in GitHub Pages, a free service that uses your GitHub repository directly to
generate a website.
Now, there are a large amount of ways to make a blog like this one, and there are others blogging
framewroks out there to use with GitHub Pages like [Octopress](http://octopress.org/), [Hexo](http://hexo.io/), 
[Foundation](http://foundation.zurb.com/), [Jekyll](http://jekyllrb.com/) (although Jekyll is the engine behind GitHub Pages),
and pretty much anything that can produce HTML and CSS, even your bare hands with a Text Editor.

All of this frameworks have something different, but they make the same work in the end.
So I chose Pelican simply because it's written in Python, and I love Python.

I assume that you're using Linux or an Unix-like operating system and Python 3.

With that being said let's get started.

## Setting up our environment
First of all, we need to have order in our project so let's create a virtual environment, I use
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org) it's a set of extensions that _wrappers_
[virtualenv](https://virtualenv.pypa.io) and make it easier to use.

If  you don't have them already just:
`pip install virtualenv virtualenvwrapper`
Create the virtual environment and switch to it:
```sh
mkvirtualenv --python=python3 blog
workon blog
```
Now install Pelican and Markdown if you're going to use it:
`pip install pelican Markdown`
We are going to use _ghp-import_ later on so install it also:
`pip install ghp-import`

## Creating our project

### GitHub repository
Because this is a personal webpage I'm going to use a user GitHub Page, therefore we have to [create a new repository](https://github.com/new)
with specific characteristics:
- The name of the repository must be _username.github.io_ where _username_ is your username on GitHub.
- As all the _User_ GitHub Pages everything in your master branch will be used to make your page.

Now go to the folder where you want to place your project and clone the repository:
`git clone https://github.com/username/username.github.io`

### Pelican project
Inside the project folder let's create a skeleton project:
`pelican-quickstart`
That command will ask you a set of questions for the configuration (you can change them later) of the page and it'll 
create a folder structure like this one:
.
+-- content/
+-- output/
+-- develop_server.sh
+-- Makefile
+-- pelicanconf.py
+-- publishconf.py

The _pelicanconf.py_ file is where I'll put all the configuration, you can use specific settings for publish your site located
in _publishconf.py_ but I'm not going to use it.

Maybe the most important settings are the URL related ones, but you can do a lot of things in the _pelicanconf.py_ file, feel free to
go to the [docs](http://docs.getpelican.com/en/3.5.0/settings.html) and check out all the possibilities.

## Writing content

The part of writing is pretty simple, all the content of the site is written in [Markdown](https://help.github.com/articles/markdown-basics/)
and the files are going to be in the _content_ folder. I separate the articles in category folders and the pages, the content
that don't change very often (Bio, About), in its own folder.

You can see the metadata syntax for Markdown post in the [pelican docs](http://docs.getpelican.com/en/3.5.0/content.html).

## Theme and personalization

Now that we have some sort of content in the page we can visualize it, select a theme and tweaking a little bit.

I selected the [Bootstrap 3 theme](https://github.com/DandyDev/pelican-bootstrap3), just clone the repository:
`git clone https://github.com/DandyDev/pelican-bootstrap3.git`
And then point the `THEME` variable in your _pelicanconf.py_ to `/path/to/pelican-bootstrap3`

Part of the beauty of Bootstrap 3 is that [Daan Debie](http://dandydev.net/) included all the Bootstrap 3 themes from
[Bootswatch](http://bootswatch.com/) made by [Thomas Park](https://github.com/thomaspark).
I which the Bootswatch theme to _flatly_ by setting the `BOOTSTRAP_THEME` variable to the _theme-name_.

At this point the webpage looked really good, but checking out some examples I saw a terrific webpage called
[Beneath Data](http://beneathdata.com/) created by [Tyler Hartley](http://www.tylerhartley.com/) with a beautiful design and
great content, so I use some of his design (hope he doesn't mind) and use it on my webpage.

If you want to change something of the theme just go to the theme folder and change it at will.

## Adding third party services

To add [Disqus comments](https://disqus.com), [Google analytics](www.google.com/analytics), and [AddThis](http://www.addthis.com/)
you have to create their respective accounts and then set the `DISQUS_SITENAME` `GOOGLE_ANALYTICS` and `ADDTHIS_PROFILE` to the 
code that each service provide you.

After that and with some luck everything should work automagically.

## Hosting in GitHub Pages

The last part. The repository structure and the page hosting.

All the content and the settings will be in a _source_ branch because the _master_ branch is used to create the actual page.

In order to keep only the _output/_ folder in the _master_ branch I used _ghp-import_, this little tool make a commit in a branch with only the
content of a specific folder:
`ghp-import -m "commit message" -b master output/ `
If no branch is specified the destination branch would be _gh-pages_ that it's the branch used in a Project site GitHub Page.

After that you can just:
`git push --all`
And the page should be up and running.
