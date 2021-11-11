# rickroll\_sensehat
This single function python program plays Never Gonna Give you Up on the 8x8 RGB led matrix of the Raspberry Pi SenseHat.

## Installation
- Add the function rickroll() to your code
- Import the necessary builtin modules (numpy, glob, os, PIL, time)
- Extract `rick.tar.gz` into a folder `img` which should lie where your python script is:
```
cd img
tar -xzvf rick.tar.gz
```
The provided archive `rick.tar.gz` contains 5300 png pictures of 8x8 pixel resolution, which is the whole 3.32 minute video.

If the orientation is wrong use `sense.set_rotation(90)` etc.

## Sound
One way would be to play an mp3 file with `omxplayer`, which is preinstalled on RPi OS
```
import subprocess
subprocess.Popen("omxplayer rickroll.mp3")
```

## Playing other movies
If your video editor can export to 8x8 png frames directly, that would be the easiest.
I used shotcut to export the video to 16x8 png frames, then the python PIL module's Image.crop() function to bulk crop the images to 8x8.
