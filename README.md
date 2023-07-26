# Do these things

```
sudo raspi-config
# Choose Interfacing Options -> SPI -> Yes Enable SPI interface
sudo reboot
```

```
git clone https://github.com/angushtlam/decorify.git
./decorify/scripts/setup_pi.sh
python ./decorify/scripts/init_epd_7in5_V2.py
```

## Set up script to run automatically on device
```
sudo nano /etc/systemd/system/decorify.service
```

```
[Unit]
Description=decorify Service
After=multi-user.target

[Service]
Type=simple
User=pi
ExecStart=/usr/bin/python /home/pi/decorify/scripts/init_epd_7in5_V2.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```
sudo chmod 644 /etc/systemd/system/decorify.service
sudo systemctl daemon-reload
sudo systemctl enable decorify.service
```