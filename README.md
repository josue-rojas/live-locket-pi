# live-locket
A project that uses a led matrix connected to a raspberry pi to display images that friends send you. 

# Info
The front and backend of live-locket for the raspberry pi (the main user side). The hub for controlling the led matrix. 

There are three repos in total for this project. 
- https://github.com/josue-rojas/live-locket
- https://github.com/josue-rojas/live-locket-backend
- https://github.com/josue-rojas/live-locket-pi

# Requirements
On raspberry pi we are using
- sqlite
- python3

# Setup (for this repo only)
1. Clone this repo
2. `cd` into the project
3. run this to install `rgb-matrix software`
    ```
    echo "Downloading rgb-matrix software setup:"
    curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh

    sed -n '/REBOOT NOW?/q;p' rgb-matrix.sh > rgb-matrix.tmp && mv rgb-matrix.tmp rgb-matrix.sh

    echo "Running rgb-matrix software setup:"
    sudo bash rgb-matrix.sh

    echo "Removing rgb-matrix setup script:"
    sudo rm rgb-matrix.sh
    echo "...done"
    ```

Inspired by https://github.com/ryanwa18/spotipi/
