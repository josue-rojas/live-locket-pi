install_path=$(pwd)



# echo "Downloading rgb-matrix software setup:"
# curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh

# sed -n '/REBOOT NOW?/q;p' rgb-matrix.sh > rgb-matrix.tmp && mv rgb-matrix.tmp rgb-matrix.sh

# echo "Running rgb-matrix software setup:"
# sudo bash rgb-matrix.sh

# echo "Removing rgb-matrix setup script:"
# sudo rm rgb-matrix.sh
# echo "...done"

# --- Matrix service setup
echo "Removing matrix service if it exists:"
sudo systemctl stop matrix
sudo rm -rf /etc/systemd/system/matrix.*
sudo systemctl daemon-reload
echo "...done"

echo "Creating matrix service:"
sudo cp ./config/matrix.service /etc/systemd/system/
sudo sed -i -e "/\[Service\]/a ExecStart=${install_path}/matrix.py &" /etc/systemd/system/matrix.service
sudo mkdir /etc/systemd/system/matrix.service.d
matrix_env_path=/etc/systemd/system/matrix.service.d/matrix.conf
sudo touch $matrix_env_path
sudo echo "[Service]" >> $matrix_env_path
sudo systemctl daemon-reload
sudo systemctl start matrix
sudo systemctl enable matrix
echo "...done"

