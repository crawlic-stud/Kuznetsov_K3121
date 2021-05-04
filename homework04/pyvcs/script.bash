#!/bin/bash
mkdir .git
mkdir .git\refs\heads
mkdir .git\refs\tags
mkdir .git\objects
echo "ref: refs/heads/master\n" > .git/HEAD
echo "[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = false\n" >> .git/config
echo "Unnamed pyvcs repository" >> .git/description