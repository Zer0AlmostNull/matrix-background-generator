# Matrix like animated background generator

Made in 1 hour challenge. Program(```main.py```) generates frames to achive matrix background effect.

To put gerated frames together into movie you can simmply use ffmpeg:
```
ffmpeg -framerate 30 -i %d.png -c:v libx264 -r 30 output.mp4
```

See results at:
https://youtu.be/F7Ov8-s2Y_I
