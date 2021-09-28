#!/usr/bin/env python3
from setuptools import setup
from os import getenv, path

PLUGIN_ENTRY_POINT = 'neon_tts_mimic = ' \
                     'neon_tts_plugin_mimic:MimicTTSPlugin'


def get_requirements(requirements_filename: str):
    requirements_file = path.join(path.abspath(path.dirname(__file__)), "requirements", requirements_filename)
    with open(requirements_file, 'r', encoding='utf-8') as r:
        requirements = r.readlines()
    requirements = [r.strip() for r in requirements if r.strip() and not r.strip().startswith("#")]

    for i in range(0, len(requirements)):
        r = requirements[i]
        if "@" in r:
            parts = [p.lower() if p.strip().startswith("git+http") else p for p in r.split('@')]
            r = "@".join(parts)
            if getenv("GITHUB_TOKEN"):
                if "github.com" in r:
                    r = r.replace("github.com", f"{getenv('GITHUB_TOKEN')}@github.com")
            requirements[i] = r
    return requirements


with open("readme.md", "r") as f:
    long_description = f.read()

with open("./version.py", "r", encoding="utf-8") as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]

setup(
    name='neon-tts-plugin-mimic',
    version=version,
    description='mimic tts plugin for NeonCore',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NeonGeckoCom/neon-tts-plugin-mimic',
    author='NeonGecko',
    author_email='developers@neon.ai',
    license='Apache-2.0',
    packages=['neon_tts_plugin_mimic'],
    install_requires=get_requirements("requirements.txt"),
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='neon mycroft plugin tts OVOS OpenVoiceOS',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
