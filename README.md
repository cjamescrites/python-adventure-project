# python-adventure-project

This is a RPG adventure game, built using python that is played in the terminal with user-input advancing the story/game. 
This repo provides a linux environment in a virtual machine utilizing vagrant.

Below are the steps needed to run the game.

# Pre-requisites...
You will need the following programs installed in order to utilize this repo.
 
# WINDOWS/LINX USERS:
- IDE (VS Studio, etc.)
- Vagrant
- Virtual Box 

# M1 CHIP USERS:
- IDE (VS Studio, etc.)
- Rosetta
- Vagrant
- VMWare Fusion

# Running the repo

# WINDOWS/LINX USERS:
1) Clone Repo into your IDE
2) In the Vagrantfile, make sure the "Windows/Linux Machine Users" code block is not commented out.
3) In the Vagrantfile, make sure the "M1 Machine Users" code block is commented out.
4) Enter vagrant up in the terminal
5) In the terminal, if python version is 3.8 or older...
    In the app folder, comment out line 5, and make sure lines 8-12 are not commented out.
    If python version is 3.9 or newer...
    In the app folder, comment out lines 8-12, and make sure line 5 is not commented out.
6) Enter vagrant ssh into the terminal
7) Enter cd app into the terminal
8) Enter python3 adventure.py to begin the game

# M1 CHIP USERS:
1) Clone Repo into your IDE
2) In the Vagrantfile, make sure the "M1 Machine Users" code block is not commented out.
3) In the Vagrantfile, make sure the "Windows/Linux Machine Users" code block is commented out.
4) Enter vagrant up in the terminal
5) In the terminal, if python version is 3.8 or older...
    In the app folder, comment out line 5, and make sure lines 8-12 are not commented out.
    If python version is 3.9 or newer...
    In the app folder, comment out lines 8-12, and make sure line 5 is not commented out.
6) Enter vagrant ssh into the terminal
7) Enter cd app into the terminal
8) Enter python3 adventure.py to begin the game

