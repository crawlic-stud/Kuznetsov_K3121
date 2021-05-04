import os
import shutil

def repo_create(path='.'):
    try:
        os.chdir(path)
        os.mkdir('.git')
        os.chdir('.git')
        file = open('HEAD', 'w')
        file.write("ref: refs/heads/master\n")
        file = open('config', 'w')
        file.write("[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = false\n")
        file = open('description', 'w')
        file.write("Unnamed pyvcs repository")
        os.mkdir('refs')
        os.mkdir('objects')
        os.chdir('refs')
        os.mkdir('heads')
        os.mkdir('tags')
    except FileExistsError:
        shutil.rmtree('.git')

print(repo_create(), 'Done')


