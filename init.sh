install_path=$(pwd)
# replace with user name (
user_name='withcheesepls'


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
sudo cp ./config/matrix.service /etc/systemd/system/
sudo sed -i -e "/\[Service\]/a ExecStart=${install_path}/matrix.py" /etc/systemd/system/matrix.service
sudo sed -i -e "/\[Service\]/a WorkingDirectory=${install_path}/" /etc/systemd/system/matrix.service
# user is to have access to image folder with user that has correct permissions
sudo sed -i -e "/\[Service\]/a User=${user_name}/" /etc/systemd/system/matrix.service


# Create service.d directory if it doesn't exist
sudo mkdir -p /etc/systemd/system/matrix.service.d
matrix_env_path=/etc/systemd/system/matrix.service.d/matrix_env.conf
sudo touch $matrix_env_path
echo "[Service]" | sudo tee $matrix_env_path
sudo systemctl daemon-reload
sudo systemctl start matrix
sudo systemctl enable matrix
echo "...done"


# # --- Images service setup
echo "Removing images service if it exists:"
sudo systemctl stop images
sudo systemctl disable images
sudo rm -rf /etc/systemd/system/images.*
sudo systemctl daemon-reload
echo "...done"

echo "Creating  images service:"
# Ensure the script is executable
sudo chmod +x "${install_path}/images.py"
sudo cp ./config/images.service /etc/systemd/system/
sudo sed -i -e "/\[Service\]/a ExecStart=/usr/bin/python3 ${install_path}/images.py" /etc/systemd/system/images.service
sudo sed -i -e "/\[Service\]/a WorkingDirectory=${install_path}/" /etc/systemd/system/images.service

# Create service.d directory if it doesn't exist
sudo mkdir -p /etc/systemd/system/images.service.d
images_env_path=/etc/systemd/system/images.service.d/images_env.conf
sudo touch $images_env_path
echo "[Service]" | sudo tee $images_env_path
sudo systemctl daemon-reload
sudo systemctl start images
sudo systemctl enable images
echo "...done"
