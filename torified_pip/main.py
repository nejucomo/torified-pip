import os
import sys
import subprocess


bindir = os.path.dirname(os.path.realpath(sys.argv[0]))
myself = os.path.join(bindir, 'torified-pip')
asidepip = os.path.join(bindir, 'not-torified-pip')


def main(argv=sys.argv):
    """
    Always run pip via torify.
    """
    install_symlinks()
    subargv = ['torify', asidepip] + argv[1:]
    pfmt('+ {!r}', subargv)
    r = subprocess.call(subargv)
    install_symlinks()
    sys.exit(r)


def install_symlinks():
    announced = False
    for name in os.listdir(bindir):
        if name.startswith('pip'):
            a = install_symlink(name, announced)
            announced = announced or a


def install_symlink(pipname, announced):
    pippath = os.path.join(bindir, pipname)

    if os.path.islink(pippath) and os.path.realpath(pippath) == myself:
        return announced

    if not announced:
        pfmt('Installing torified-pip:')

    asidepath = os.path.join(bindir, 'not-torified-{}'.format(pipname))
    pfmt('Rename {!r} -> {!r}', pippath, asidepath)
    os.rename(pippath, asidepath)
    pfmt('Symlink {!r} -> ./torified-pip', pippath)
    os.symlink('./torified-pip', pippath)
    return True


def pfmt(tmpl, *args):
    print(tmpl.format(*args))
