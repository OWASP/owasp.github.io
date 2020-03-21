# owasp.github.io
OWASP Foundation main site repository

### local development

since there's no Gemfile included with this repo at the moment, the easiest thing
to do is to fake a new jekyll install by running the following:

```
$ bundle exec jekyll new --force --skip-bundle
$ bundle install
$ bundle exec jekyll serve
```

unfortunately, because the local build is currently broken, you'll see the following
error:

```
  Liquid Exception: Could not locate the included file 'news-events.html' in any of ["/home/adam/Desktop/projects/owasp.github.io/_includes", "/home/adam/.rvm/gems/ruby-2.6.3/gems/minima-2.5.1/_includes"]. Ensure it exists in one of those directories and, if it is a symlink, does not point outside your site source. in index.md
```

to resolve this, just delete the following line from `index.md`:

`{% include news-events.html %}`

then run `bundle exec jekyll serve` again, and you should be able to access the
site at `localhost:4000`. It still doesn't look exactly right, and I assume this
is because some of the downloaded assets are hosted at relative paths from the main
domain, so aren't available in this source code.

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

The website is licensed under a [Creative Commons Attribution-ShareAlike 4.0
International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
