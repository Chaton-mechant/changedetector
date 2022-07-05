import contextlib
import re
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

version = ''
with open('changedetector/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)[1]

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    with contextlib.suppress(Exception):
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()

packages = [
    'changedetector',
]

setuptools.setup(
    name="changedetector",
    version=version,
    author="Lux Luth",
    author_email="luxusluth@gmail.com",
    description="A basic change detector for the Python, Ruby and C++.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chaton-mechant/changedetector",
    project_urls={
        "Bug Tracker": "https://github.com/Chaton-mechant/changedetector/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    packages=packages,
    python_requires=">=3.6",
)
