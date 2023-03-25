# PiFrame

An LED matrix driven by a Raspberry Pi to display your currently playing
Spotify album.

<IMG>


## Overview

This was written alongside a blog post centred around the headless setup of a
Raspberry Pi, and creating a tool from the ground up. You can check that out
here <LINK>. For a condensed set of installation steps, but if you want more
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
    4) <follow steps as in [spotibar repo](https://github.com/conor-f/spotibar#installation)>
    5) `sudo chmod -R 777 config/`
    6) `docker compose up -d`
