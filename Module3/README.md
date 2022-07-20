# Module 3

Local environment - all the software programmers need for their work installed on their computers.

## 3.1 Programming Tools

* Python interpreter
* A code editor or integrated development environment (IDE)
* Terminal / Command Prompt


### Terminal
Terminal emulator is an application running shell and used to execute commands in it.

See more here:
* https://en.wikipedia.org/wiki/List_of_Unix_commands
* https://en.wikipedia.org/wiki/Bash_(Unix_shell)


### Python interpreter
Python interpreter is a command that executes Python code. The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.

To start interactive interpreter run:

    python

#### Python virtual environment (virtualenv)
Virtualenv is a module built into Python that allows you to separate projects from each other. This way, when working on two projects at the same time, changes to one will not affect the other. The projects will be able for example to use the same library, but in two different versions.

Virtualenv creates the entire Python environment in a directory of your choice.

To create a virtual environment in directory `./venv/`:

    python3 -m venv ./venv/

To activate your virtual environment:

    source ./env/bin/activate

#### Pip
Pip is a tool to install external libraries (packages).

To istall a package:
    
    pip install package

**NOTE:** Remember to always install after activating the virtual environment - that way the packages you install will be available to the rest of your project's code.

To find out what packages you have installed at the moment, use the command:

    pip freeze


#### IPython
IPython is a powerful frontend to the original Python interpreter, whose features include syntax highlighting, instruction completion, history of typed commands, etc.

To install ipython:

    pip install ipython

To start ipython run:
    
    ipython

### Code Editor or IDE
A source-code editor is a text editor program designed specifically for editing source code of computer programs. 

Good examples of Python source code editors are:
* [Visual Studio Code](https://code.visualstudio.com/) (VSCode)

An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.

Good examples of Python IDEs are:
* JetBrains [PyCharm](https://www.jetbrains.com/pycharm/learn/)

## 3.2 Tracking code changes
Version control, also known as source control, is the practice of tracking and managing changes to software code. Version control systems are software tools that help software teams manage changes to source code over time. 

See more here:
* https://www.atlassian.com/git/tutorials/what-is-version-control

### Git
There are many version control systems. Git is the most popular one. 

Git makes it easy to save successive versions of a project. It is possible to use it locally on the computer and to connect to a remote repository to share files with other developers.

Remote repositories are online platforms where one can store not only current files, but also the full history of changes to a project.

See more here:
* https://rogerdudler.github.io/git-guide/

#### Git configuration
Before getting started, we will need to configure a few parameters in git. We only need to perform these operations once and they will work for all future projects.

First, we will save our username and email. This is needed because every saved version (called commit in git) will be signed - so that in teamwork you know who the author of a change is. If we don't do this, when we try to save a commit, Git will respond with the message "Please tell me who you are".

It will only take a moment to set up your user details:

* Open a terminal (you don't need to care what directory the terminal is currently pointing to, as we will be defining Git's global settings).
* Type the following command, specifying your name instead of the example:
```
git config --global user.name "Jan Kowalski"
```
* Then type another command, with your email address of course: 
```
git config --global user.email "jan.kowalski@example.com"
```
* You can check all global Git settings with the followwing command: 
```
git config --global -l
```

#### Git repository initialization

To initialize a git repo:

    git init

This operation will add a new .git folder to our project where the repository information will be stored.

#### Git status & commits

A commit saves changes to files relative to the previous commit, which means that only the files that have been modified are overwritten, not the entire repository.

To work with commits effectively, we need to learn how to check status of the repository. 

To displays the current status of the repository:

    git status

If the git repo is empty, then we will see:
* `On branch master` - tells us which branch (branch) of the project we are on,
* `No commits yet` - tells us that no commits have been written to the repository yet, 
* `nothing to commit` - means that there are no files to be written to the commit for now. 

On the other hannd, if we will create a file in the empty git repo, and then run `git status` command again, we will see information about `Untracked files`, i.e. files that have not yet been added to the index. 

Index of git repository is something like a waiting room, where there are files waiting for a commit. In other words, "untracked files" are files that have not yet been saved in any commits.

To prepare files for a commit, we have to first stage them with command:

    git add file.py

To save all files in a given directory, we can run:

    git add .

If we run now `git status`, the staged files will be displayed under `Changes to be commited`.

Once the file is stagged, we can commit it using command:

    git commit -m "Title of the commit"

#### The .gitignore file
Not all project files should always go into the repository (e.g. large binary files, external libraries, temporary/cache files etc.).  It is a good idea to add a `.gitignore` file, which tells git which files are to be ignored.

See Github's .gitignore templates:
* https://github.com/github/gitignore


#### Good practices for naming commits
Each commit will have a description (`Commit Message`). It is important that these descriptions are readable and fulfil the function of communicating within the team and documenting the progress of the project.


* Brevity - The commit message should briefly describe what has been changed from an earlier version. We should not to exceed 50 characters.
* Language - Commit message should start with a verb in the simple present tense, capitalized. A good first word for a commit title might therefore be "Add", "Remove", "Fix" or "Change". In contrast, a bad title would be "Added main.py" or "New file".
* Readability - We should avoid vague terms like "Add styles" or "Fix bug". We should be more specific instead, e.g. "Add shopping list dict" or "Fix bug in product list".

## 3.3 Git remote repository
The role of a remote repository is to:
* store the code outside of our computer (e.g. for safety),
* allow multiple developers working on the same project.

### Git remote repository hosting providers
To set up a remote repository on a server, we need a platform that provides remote git repositories. 

Among the most popular of these are:
* GitHub
* GitLab
* BitBucket.

### Working with remote repositories

### remote add
TODO

### clone
TODO

#### Push
The `git push` command is used to send commits from a local repository to a remote repository.

#### Pull
The `git pull` command pulls changes from the remote repository to the local repository. It normally applies when someone else is working on the same project.

#### Branch & Merge
TODO