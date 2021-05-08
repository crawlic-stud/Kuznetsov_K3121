import os
import pathlib
import typing as tp


def repo_find(workdir: tp.Union[str, pathlib.Path] = ".") -> pathlib.Path:
    # PUT YOUR CODE HERE
    ...


def repo_create(workdir: tp.Union[str, pathlib.Path]) -> pathlib.Path:
    os.chdir(workdir)
    os.mkdir('.git')
    os.chdir('.git')
    file = open('HEAD', 'w')
    file.write("ref: refs/heads/master\n")
    file = open('config', 'w')
    file.write(
        "[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = false\n")
    file = open('description', 'w')
    file.write("Unnamed pyvcs repository")
    os.mkdir('refs')
    os.mkdir('objects')
    os.chdir('refs')
    os.mkdir('heads')
    os.mkdir('tags')
    pass


