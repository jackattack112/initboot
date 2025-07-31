#join tailscale
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --accept-routes

#install selenium
python3 -m venv venv/
source venv/bin/activate 
pip3 install selenium

#run selenium script
python3 logins.py
