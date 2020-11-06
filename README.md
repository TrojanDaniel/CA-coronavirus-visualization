# CA-coronavirus-visualization

Description: Visualization of COVID data in CA 


Requirements: 

1. Create virtual environment named HW5, then activate it.

  ![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/1.png)
  
  ![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/2.png)
  
2  pip install all the dependencies. 

![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/3.png)

![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/4.png)


3  Run resulting.py. 

Docker 

1 Download docker desktop.
https://www.docker.com/products/docker-desktop

2 create Dockerfile and use it to build image.


![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/5.png)


3 Create Image   RUN: docker build -t ubuntu.

![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/6.png)

4 run the image in default port(5006). RUN: docker run -p 5006:5006 -it ubuntu 

![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/7.png)

5 Check the visualization result in  http://localhost:5006/resulting


Results 


![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/8.png)

![image](https://github.com/TrojanDaniel/CA-coronavirus-visualization/blob/main/steps_screenshots/9.png)


