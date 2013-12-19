Pebble Mac PowerPoint Remote Control
==============
Forked from smarthomewatch
See  makrco's original project
pebble home automation hack: http://makr.co/blog/pebble-home-automation/


This started off as a curiosity as I just wanted to use my Pebble to advanced PowerPoint slides. I posted a video online and received some requests to share so I've posted this.

Make sure pebble python lib is on your PYTHONPATH
eg:
export PYTHONPATH=$PYTHONPATH:~/pebble-dev/libpebble

To run try:

./presenter_controller.py --lightblue --pebble_id=<YOUR PEBBLE MAC ADDRESS>

e.g.

./presenter_controller.py  --lightblue --pebble_id=00:17:5A:4B:4C:4D

Usage:
run the above command
run powerpoint in fullscreen
enter the music app on the Pebble watch
use the forward and back arrows to advance slides
