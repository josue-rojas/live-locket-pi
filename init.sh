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
sudo systemctl disable matrix
sudo rm -rf /etc/systemd/system/matrix.*
sudo systemctl daemon-reload
echo "...done"

echo "Creating matrix service:"
# Ensure the script is executable
sudo chmod +x "${install_path}/matrix.py"
sudo cp ./config/matrix.service /etc/systemd/system/
sudo sed -i -e "/\[Service\]/a ExecStart=${install_path}/matrix.py" /etc/systemd/system/matrix.service
sudo sed -i -e "/\[Service\]/a WorkingDirectory=${install_path}/" /etc/systemd/system/matrix.service

# Create service.d directory if it doesn't exist
sudo mkdir -p /etc/systemd/system/matrix.service.d
matrix_env_path=/etc/systemd/system/matrix.service.d/matrix_env.conf
sudo touch $matrix_env_path
echo "[Service]" | sudo tee $matrix_env_path
sudo systemctl daemon-reload
sudo systemctl start matrix
sudo systemctl enable matrix
echo "...done"
