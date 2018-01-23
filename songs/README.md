# Demo Songs

[Click here](https://drive.google.com/file/d/1hMaEgZNCcw5u2xtwcfdJU2p2pHMf3_y9/view?usp=sharing) for a zip file containing a set of properly formatted songs. They are the files from [this video](https://www.youtube.com/watch?v=WXRweSJNEyA) converted using the process below.

# How to add songs

At the moment, songs have to be encoded a very specific way. If you have `ffmpeg` or `sox`, you can run either of the following commands to convert audio files:

**Ffmpeg:**

```bash
ffmpeg -i INPUT.XYZ -acodec pcm_s16le -ar 44100 -ac 1 OUTPUT.wav
```

**Sox:**

```bash
sox INPUT.XYZ -r 44100 -b 16 -c 1 -e signed-integer OUTPUT.wav
```

### Format

The following format is required:

 - **Type:** wav
 - **Rate:** 44100
 - **Channels:** 1
 - **Format:** Signed Integer
 - **Bitdepth:** 16

