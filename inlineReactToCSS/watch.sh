#!/bin/bash
tmux new-session 'echo js_file; watch cat ./input/default.js' \; split-window 'echo css_file; watch cat ./input/default.css' \;  select-layout even-horizontal
