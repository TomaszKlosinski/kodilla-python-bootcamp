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
Basic Git configuration
Before getting started, we will need to configure a few parameters in Git. We only need to perform these operations once and they will work for all future projects.

First, we will save our username and email. This is needed because every saved version (called commit in Git) will be signed - so that in teamwork you know who the author of a change is. If we don't do this, when we try to save a commit, Git will respond with the message "Please tell me who you are".

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
