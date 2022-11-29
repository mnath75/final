sudo cp -rf Application_Main.conf /etc/nginx/sites-available/Application_Main
chmod 777 /var/lib/jenkins/workspace/final

sudo ln -s /etc/nginx/sites-available/Application_Main /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx