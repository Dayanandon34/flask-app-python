sudo usermod -aG docker ubtunu
sudo usermod -aG docker jenkins
groups jenkins
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock

sudo systemctl restart jenkins

groups jenkins

sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock

sudo systemctl start docker
sudo systemctl enable docker


sudo docker build . -t flask-app:latest
sudo docker run -d -p 7000:7000 flask-app:latest


sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock

sudo apt update
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d app1.aseemcloudtech.com




server {
    listen 80;
    server_name app1.aseemcloudtech.com;

    location / {
        proxy_pass http://127.0.0.1:7000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


ln -s /etc/nginx/sites-available/a /etc/nginx/sites-enabled/


sudo systemctl restart nginx
