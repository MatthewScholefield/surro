# Surro

*A game played through only sounds (headphones recommended).*

**Your goal:** Find the source of the music without dying. 

[![Screenshot](https://images2.imgbox.com/10/77/RJx8SxBE_o.gif)](https://photos.app.goo.gl/vl7rXW9XBKDG3vTo2)

## Game Info

### Visual Key

The color on the screen acts as a visual aid to help show objects close to you.

 - **Blue:** Wall
 - **Red:** Evil Enemy
 - **White:** Source of Music (Target)

### Controls

 - **Movement:** Up, Down, Left, Right
 - **Restart:** Space
 - **Change Game Mode:** M

### Game Modes

 - **Regular:** Escape the evil noise while finding the source of the music
 - **Timed:** There is no enemy, and instead your health steadily decreases

## Installation

You can find binaries on [the release page](https://github.com/MatthewScholefield/surro/releases). Otherwise, follow the instructions below. ***Warning:** The Windows instructions below are untested. If you try them out and something doesn't go right, it'd be great to troubleshoot the issue so that the instructions can be improved.*

 - Install Python 3 on your system and open a command prompt in the directory you downloaded this repository
 - Install OpenAL library:
   - **Linux:** Use your package manager. Some possible names: `libopenal-dev`, `openal-devel`
   - **Windows:** Download the [Windows Installer here](https://www.openal.org/downloads/)
 - Setup virtual environment:
   - **Linux:** `./setup.sh`
   - **Windows:**
     - [**Create a virtualenv**](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/)
     - `pip install -r requirements.txt`
 - [Add some songs](https://github.com/MatthewScholefield/surro/tree/master/songs) to `songs/`
 - Run:
   - **Linux:** `./start.sh`
   - **Windows:** Activate the virtualenv you created and run `python surro/__main__.py`

## Contributing

All PRs are welcome. Feel free to use the issue tracker if you encounter a bug. The codebase uses PEP8 with a line length of 100 characters.

