# CA-coronavirus-visualization

Description: Visualization of COVID data in CA 


Requirements: 

1. Create virtual environment named HW5, then activate it.
  ![image](https://raw.githubusercontent.com/TrojanDaniel/CA-coronavirus-visualization/master/venv_screenshots/1.png)
2  pip install all the dependencies. 
![image](https://raw.githubusercontent.com/TrojanDaniel/CA-coronavirus-visualization/master/venv_screenshots/1.png)
3  Run resulting.py. 
![image](https://raw.githubusercontent.com/TrojanDaniel/CA-coronavirus-visualization/master/venv_screenshots/1.png)
![image](https://raw.githubusercontent.com/TrojanDaniel/CA-coronavirus-visualization/master/venv_screenshots/1.png)
![image](https://raw.githubusercontent.com/TrojanDaniel/CA-coronavirus-visualization/master/venv_screenshots/1.png)

Docker 

1 Download docker desktop.
https://www.docker.com/products/docker-desktop

2 create Dockerfile and use it to build image.

3 Create Image   RUN: docker build -t ubuntu . 

4 run the image in default port(5006). RUN: docker run -p 5006:5006 -it ubuntu 

5 Check the visualization result in  http://localhost:5006/resulting


Results 

![image](https://raw.githubusercontent.com/TrojanDaniel/CA-coronavirus-visualization/master/venv_screenshots/1.png)
![image](https://raw.githubusercontent.com/TrojanDaniel/CA-coronavirus-visualization/master/venv_screenshots/1.png)
