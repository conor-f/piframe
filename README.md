# PiFrame

An LED matrix driven by a Raspberry Pi to display your currently playing
Spotify album.

![Cover Image](https://user-images.githubusercontent.com/2671067/227734710-66669b88-7e8b-4638-9de7-89157410044f.jpeg)

## Overview

This was written alongside a blog post centred around the headless setup of a
Raspberry Pi, and creating a tool from the ground up. You can check that out
[here](https://blog.randombits.host/piframe/). For a condensed set of installation steps, but if you want more
narrative, check the blog post out. There are a number of limitations and
improvements that can be made, and I welcome them all in the issues of this
repo.


## Installation

  This is designed to be run on a Raspberry Pi 3B+, with `docker compose` as
outlined in the blog post. Grab the Docker image conorjf/piframe from [here](https://hub.docker.com/r/conorjf/piframe).

  Then follow the installation steps as follows:

    1) Add docker-compose.yaml to the Pi
    2) `docker compose pull`
    3) `docker compose run -it piframe spotibar --init`
    4) Follow steps as in the spotibar repo here: https://github.com/conor-f/spotibar
    5) `sudo chmod -R 777 config/`
    6) `docker compose up -d`
