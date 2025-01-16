
# Stub Files for Maya2024

Autodesk no longer includes stub files for Maya libraries in the devkit as they had been doing
for a number of years.  The stub files in this release are meant to take their place.  And further, they are meant to
be much more useful in that they provide the complete documentation without having to 
continually refer to the webpage documentation.  Sometimes it will be necessary, though, because
some specialized tables were not able to be reproduced in the stub file docstrings.

The release contains versions of the stub files output for 3 IDEs specific to their capability to
render certain docstring formatting.  These include VS Code, Pycharm and Eclipse.  Other IDEs
should be able to make use of them as well.  As long as they can handle extensions of either:
.pyi or .pypredef.

** Note:** While a certain amount of proofreading has been done, it is not possible to guarantee
everything has been ported correctly.  If you come across something that is not correct, please
leave a comment at the Gitlab release site for this project.


## Installation

Some of these stub files are very large.  With the default memory settings, IDEs will not be able to 
parse them.  Remember to increase the memory limits for the particular IDE that you are using.

Also note that most IDEs need to be restarted after setting the path to the stub files.  They
need to be forced to regenerate the information in the files.  This is especially true if you
have been using another set of Maya stub files.


### A. VS Code
- unzip the release to a directory of your choosing
- in VS Code, go to:
Settings -> Python - Auto Complete:Extra Paths -> Edit in settings.json
- Enter the path to the /vscode directory:   
[your directory]/release/maya2024/stubs/vscode/

### B. Pycharm
- unzip the release to a directory of your choosing
- in VS Code, go to:
Settings -> Python interpreter -> interpreter pulldown menu -> Show all -> Show interpreter paths (icon) ->
Add...
- Navigate to the path of the /pycharm directory:
[your directory]/release/maya2024/stubs/pycharm/


### C. Eclipse/Pydev
- unzip the release to a directory of your choosing
- in Eclipse, go to:
Windows -> Preferences -> PyDev -> Interpreters -> Python Interpreter -> Predefined (tab) -> New
- Navigate to the path of the /pycharm directory:
[your directory]/release/maya2024/stubs/eclipse/


## Releases
Previously released versions of stub files in:
- 2008, 2009, 2010, 2013, 2014