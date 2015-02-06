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

This will be a kind of tutorial.

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
```sh
pip install virtualenv virtualenvwrapper
```
Create the virtual environment and switch to it:
```sh
mkvirtualenv --python=python3 blog
workon blog
```
Now install Pelican and Markdown if you're going to use it:
```sh
pip install pelican Markdown
```
We are going to use _ghp-import_ later on so install it also:
```sh
pip install ghp-import
```

## Creating our project

### GitHub repository
Because this is a personal webpage I'm going to use a user GitHub Page, therefore we have to [create a new repository](https://github.com/new)
with specific characteristics:
- The name of the repository must be _username.github.io_ where _username_ is your username on GitHub.
- As all the _User_ GitHub Pages everything in your master branch will be used to make your page.

Now go to the folder where you want to place your project and clone the repository:
```sh
git clone https://github.com/username/username.github.io
```

### Pelican project
Inside the project folder let's create the  
