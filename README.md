# Project-Shell
## A Python Bash Replacement

### What is Project Shell?
Project Shell is a purely Python bash replacement for Python 3.3+ designed for everyday use. Currently you need to run it from the command line, but we will be changing this hopefully in the near future.

### Why Project Shell?

1. It's easy to contribute! You can easily add whatever feature that you want just by forking the repository and opening a pull request. Wait for the review to be accepted and you can use your new feature in the next release.

2. It's open source! Because of this, bugs are found relatively quickly and can be patched by the community. In addition, as mentioned above, any collaborator can add features, meaning that Project Shell has the potential to become the most versatile shell ever written!

3. It's written in Python! Show it off to all your fellow programmers. Tell them that you use a Python shell ;)

### I've found a bug. What do I do?
Open an issue in the issue tracker and be sure to include as many details as you can. That way, we can easily fix the issue.

### What license is Project Shell released under?
Because Project Shell is open source software, we have released it under the MIT license. In plain english, this means that you can do whatever you want with the software, as long as you don't hold us liable and keep a copy of the license in any distribution of the software and for any derivatives. Remember, none of use are legal advisers so don't take our word - read the LICENSE file and talk to an attorney if you're really worried

### How do I start using it?
Simply download the repository, `cd` into it using any terminal and run `python3 main.py`. Easy! If you want to use it more often, you may want to create a bash script on your desktop. This would run the `main.py` script from any directory, allowing you to hide the code away.  Keep in mind that the following script will only work on *nix like systems.

* Firstly, create a script and include the following code:
```
#!/bin/sh
python3 "/path/to/project-shell/main.py"
```

* Make the script executable with `chmod+x "/path/to/script.py"`
* You can now run this script by double-clicking on the file.
