This is the source code for the web pages in https://www.owasps.org/

The website is generated using Environment github-pages.

To contribute to this repository, you can edit simply using the GitHub integrated editor. You will need to have a GitHub account, and a new pull request with your changes will be created.

If you need to edit multiple files, or if you want to check the resulting pages before posting a pull request. It is a simple process, and you can check your work before submitting the changes.

Editing locally
You need Git and and IDE.
Install IDE Softwares to run the code.
Install Git
Fork this repo first.

$ git clone https://github.com/OWASP/owasp.github.io.git
Don't forget to make it recursive, or you will have errors executing hugo afterwards!

If you forgot, you can still run this command on your local repo:

$ git submodule update --init --recursive
Make your changes, commit to your fork of the repository, and create a pull request afterwards. It is very easy to create a PR going to the GitHub Web page of your repo. You will see a "create a pull request" link, so you follow that one and do a pull request against our repository.

After we merge your changes, a webhook will be fired to update your changes, and it take up to 5 minutes to go live.

GitHub
Signup for a GitHub account
Signin to GitHub

From there, you've got all the files ready to go and you can start your hugo server to preview the changes you made. Live reload will update your change in the browser as soon as you hit that save key.


Editors
Several editors for better markdown editing

Sublime has package called MarkdownExtended that improves Markdown + Front Matter syntax highlighting
Atom has a built in GitHub Markdown syntax highlighting
Visual Studio
WebStorm
Git Clients
Git, using command lines can be a little bit confusing at first, those UI clients will help wrap your head around it.

GitHub Desktop
Source Tree
