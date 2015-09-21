# audio-locker
Mute/Unmute Windows on Lock/Unlock

## About
This script was written to mute/unmute (through AudioSrv) a Windows
computer on Lock/Unlock. The application must be started with Elevated
Permissions (start cmd with Admin rights) so AudioSrv can be start/stopped.

In the case the script crashes and you have no audio, type "net start AudioSrv" to restart your audio.
