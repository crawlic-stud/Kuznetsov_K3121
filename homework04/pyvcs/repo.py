import os
import pathlib
import typing as tp


def repo_find(workdir: tp.Union[str, pathlib.Path] = ".") -> pathlib.Path:
    git_dir = os.getenv("GIT_DIR", default=".git")
    workdir = pathlib.Path(workdir)
    while pathlib.Path("/") != workdir.absolute():
        if (workdir / git_dir).is_dir():
            return workdir / git_dir
        workdir = workdir.parent
    if (workdir / git_dir).is_dir():
        return workdir / git_dir
    else:
        raise Exception("Not a git repository")


def repo_create(workdir: tp.Union[str, pathlib.Path]) -> pathlib.Path:
    git_dir = os.getenv("GIT_DIR", default=".git")
    workdir = pathlib.Path(workdir)
    if workdir.is_file():
        raise Exception(f"{workdir} is not a directory")
    os.makedirs(workdir / git_dir / "refs" / "heads")
    os.makedirs(workdir / git_dir / "refs" / "tags")
    (workdir / git_dir / "objects").mkdir()
    with open(workdir / git_dir / "config", "w") as f:
        f.write("[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = false\n",)
    with open(workdir / git_dir / "HEAD", "w") as f:
        f.write("ref: refs/heads/master\n")
    with open(workdir / git_dir / "description", "w") as f:
        f.write("Unnamed pyvcs repository.\n")
    return workdir / git_dir

