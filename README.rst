Yak-Tak | Tic-Tac-Toe
================================================================================

Yak-Tak is a game of Tic-Tac-Toe that will never lose to a human player.
You'll wish you had played **Global Thermonuclear War** instead.

Installation
--------------------------------------------------------------------------------

Yak-Take is built on top of `Flask`_.

.. _Flask: http://flask.pocoo.org/

Python
~~~~~~

To get running with Yak-Tak, you'll need to have `Python`_.  Yak-Tak is
developed and tested to run on Python 2.7.x (32-bit).  It may run on other
versions of Python, but this is not a guarantee.

.. _Python: http://www.python.org/

Installing Packages
~~~~~~~~~~~~~~~~~~~

Yak-Tak depends on the following Python packages:

* `Flask`_

To install all of these dependencies, simply run::

  > pip install -r requirements.txt

If you are on Windows and don't have the *pip* command, you must install it
first.  Check the `pip and distribute on Windows`_ section for more information
about how to do that.

.. _`Flask`: http://flask.pocoo.org/

*pip* and *distribute* on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(Documentation originally copied from `Flask docs on pip and distribute`__.)

__ http://flask.pocoo.org/docs/installation/#pip-and-distribute-on-windows

On Windows, installation of *easy_install* is a little bit trickier, but still
quite easy. The easiest way to do it is to download the `distribute_setup.py`_
file and run it. The easiest way to run the file is to open your downloads
folder and double-click on the file.

Next, add the *easy_install* command and other Python scripts to the command
search path, by adding your Python installation's Scripts folder to the *PATH*
environment variable. To do that, right-click on the "Computer" icon on the
Desktop or in the Start menu, and choose "Properties". Then click on "Advanced
System settings" (in Windows XP, click on the "Advanced" tab instead). Then
click on the "Environment variables" button. Finally, double-click on the "Path"
variable in the "System variables" section, and add the path of your Python
interpreter's Scripts folder. Be sure to delimit it from existing values with a
semicolon. Assuming you are using Python 2.7 on the default path, add the
following value::

  ;C:\Python27;C:\Python27\Scripts

And you are done! To check that it worked, open the Command Prompt and execute
``easy_install``. If you have User Account Control enabled on Windows Vista or
Windows 7, it should prompt you for administrator privileges.

Now that you have easy_install, you can use it to install pip::

  > easy_install pip

.. _distribute_setup.py: http://python-distribute.org/distribute_setup.py

Running Yak-Tak
--------------------------------------------------------------------------------

You can run Yak-Tak by simply running the following command::

  > make

Then open up your favorite browser and visit ``http://localhost:5000/``.

Running Unit Tests
--------------------------------------------------------------------------------

Unit tests are provided.  Simply run the following command::

  > make test

Notes
--------------------------------------------------------------------------------

I did not optimize this application for performance.  I wanted to accomplish
this application in a straightforward way and focus on making it testable as
a primary goal.

The web interface is built using JavaScript and HTML5.  I'm developing it with
Chrome and I plan to test it with Firefox, but I do not plan to test it on too
many browsers to save me some time.  I'm also not testing this on mobile
devices, at least not now.

Also, the web interface is using expanded JavaScript and CSS.  If this were
a hosted game I'd worry about minimizing and compressing these assets to make
as few requests as possible, but this game is only going to be run locally.

Python is an amazingly flexible language that lets you use Object-Oriented
patterns when you need them.  I chose to make the computer player (wopr)
a library of functions because I am a firm believer that you should only use
Object-Oriented programming where you need its benefits.

To build the computer player I took inspiration from *functional programming*
and made each function independent from one another and always return
something, even if it's a value of *None*.  This makes it easy for me to
arrange these functions to build a whole computer player using *null
coalescing* (at least that's what the C# people call it).  Maybe in the future
I'll make several versions of the computer players, one that's interesting to
play against and makes mistakes.

When I started this project I thought about how to make the computer player.
Tic-Tac-Toe is an easy enough game to pre-compute all the possible games that
can be played with a modern machine.  However, I think it's more fun to design
strategies and see how they play out.  Maybe I made more work for myself, but
this is the first computer player I've written.

Hope you like it.
