Development environment

Install Kodi v18 (Leia) 

    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:team-xbmc/ppa
    sudo apt-get update
    sudo apt-get install kodi

Before addon reinstallation:

   rm -rf ~/.kodi

Run AceStream docker on RPi

sudo docker run --restart always -d --privileged --name acestream -p 127.0.0.1:62062:62062 -p 127.0.0.1:6878:6878 -p 8621:8621 docker.io/aaaler/acestream-pi --client-console --live-buffer 50 --max-connections 400 --max-peers 200
