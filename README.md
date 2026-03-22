# audacious-libkss

An Audacious plugin that uses [libkss](https://github.com/digital-sound-antiques/libkss) to play KSS music files (MSX, SMS, Game Gear).

Supports all MSX sound chips: PSG, SCC, OPLL/FMPAC, MSX-Audio/OPL. Per-channel stereo panning for PSG and SCC, OPLL channel stereo. Parses NEZplug extended m3u/m3u8 playlists for track titles, durations, and fade times. Configurable via Audacious preferences panel.

## Building

```bash
git clone --recursive https://github.com/ramonsmits/audacious-libkss
cd audacious-libkss
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
sudo cmake --install build
```

## Building with Podman

```bash
podman build -t audacious-libkss .
podman cp "$(podman create --rm audacious-libkss)":/kss-libkss.so .
cp kss-libkss.so "$(pkg-config --variable=plugin_dir audacious)/Input/"
```
