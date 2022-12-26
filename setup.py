import subprocess
import argparse
import os
from glob import glob


def _build_wheel(source_dir, destination_dir):
    try:
        subprocess.check_call(['python', 'setup.py', 'bdist_wheel', '--dist-dir', destination_dir], cwd=source_dir)
    except subprocess.CalledProcessError:
        print('Error while building wheel from {} directory'.format(source_dir))


def build_wheels(sources, wheels):
    """
    Trying to create wheel for package in each subdirectory from specified sources dir.
    """
    dest_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), wheels))
    for src_dir in glob(os.path.join(sources, '*')):
        if os.path.isdir(src_dir):
            _build_wheel(src_dir, dest_dir)


parser = argparse.ArgumentParser(
    description='Build wheels for all packages from sources dir specified.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--sources-dir", dest="sources", required=False, default="./venv/src", help="sources directory path")
parser.add_argument("--wheels-dir", dest="wheels", required=False, default="./wheels", help="path to directory with wheels")

args = parser.parse_args()
kwargs = args.__dict__
build_wheels(**kwargs)