# Matrix like animated background generator

Made in 1 hour challenge. Program(```main.py```) generates frames to achive matrix background effect.\

To put gerated frames together into movie you can simmply use ffmpeg:
```
ffmpeg -framerate 30 -i %d.png -c:v libx264 -r 30 output.mp4
```

https://user-images.githubusercontent.com/62188864/200200438-0302995f-0536-4182-b243-1b1bb908cb42.mp4
