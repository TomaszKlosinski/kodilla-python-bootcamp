# Module 3

Local environment - all the software programmers need for their work installed on their computers.

## 3.1 Programming Tools

* Python interpreter
* A code editor or integrated development environment (IDE)
* Terminal / Command Prompt


### Terminal
Terminal emulator is an application running shell and allowing to execute commands within.

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
* Visual Studio Code (VSCode)

An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.

Good examples of Python IDEs are:
* PyCharm
