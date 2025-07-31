#install selenium
python3 -m venv venv/
source venv/bin/activate
pip3 install selenium

#install chrome
curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
pip3 install undetected-chromedriver

#run selenium script
python3 login.py

#join tailscale
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --accept-routes
