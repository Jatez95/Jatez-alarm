# Jatez-alarm

This project is to learn

This alarm have a GUI with three principal options:

1 -> set the alarm
2 -> set a timer
3 -> download a sound

And a suboption that allows you to set the sound of the alarm and the timer

This project is aredy done but in a CLI, currently working on a GUI. this UI will allow you to change between these options and set the sound or atleast i will try to do it.

The first component or the alarm:

In this component you can set the time the alarm will sound, even if you didnt set the alarm sound,
if there is no sound it will a take an alarm sound from windows (Not Linux nor MacOS).

In the alarm component you can set days, but i dont know if this realy works because normally this is remembered by the system. But i dont know how to do that so only sounds when the program is running. So the days its something i will never know if realy works

The second component is a timer.

Just a regular timer you set the time, and this will sound when reach 0 and the sound is the same thing that the alarm does.

And last but not less, you can download a sound with the third component, this only works with youtube videos.

A few more things to know, is that there is a function in the downloader that extracts the drives name Example: (C: or D: or F:).

then checks if one of the drives have the Users folder, and if exists saves something like this: C:\Users\Logged User\
and the last thing this do is, check if the alarm sounds folder exists. If this dosnt exists will create the folder

If you navigated to througout the folders of the project, you probably noticed about a cli and alarm folder. Well this folders does nothing is not called anytime its only the GUI, sound_player.py and the Downloader.