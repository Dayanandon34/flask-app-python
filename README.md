CI/CD Pipeline:
CODE->GITHUB->JENKINS->DOCKER->FLASKAPPIMAGE->EC2 HOST ON WEB
--------------------------------------------------------------
Below commands give brief about this project works
--------------------------------------------------

-> launch ubuntu instace using AWS ||
-> connect ec2 ||
-> change user to root:  sudo su ||
-> install jenkins nad java 
-> install docker

-> create project in jenkins pull code from github repo
->sudo usermod -aG docker ubuntu
->sudo usermod -aG docker jenkisn
-> groups jenkins
-> sudo chown root:docker /var/run/docker.sock 
-->sudo chmod 660 /var/run/docker.sock
-> sudo systemctl restart jenkins

go to jenkins and write belo script
-> docker build . -t flask-app:latest 

echo "Image is created"
docker run -d -p 7000:7000 flask-app:latest
echo "App is live. access with IP: 7000"

-> give onbound acces in ec2 to port 7000
and check your pipline will be executes successfully

 check docker containers and images
->docker ps
-> docker images

check status of running programs
->netstat -tulnp

-------------------------------
|| Thank you, By Dayanand! ||
----------------------------------
