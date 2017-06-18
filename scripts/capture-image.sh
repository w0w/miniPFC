#!/bin/bash

NAME=$1

fswebcam -S 10 -r 1280x720 --no-banner ./dump/image/$NAME.jpg
