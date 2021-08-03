Documentation for the implementing of profiling in ECR


Database S

How to run profiling on ECR.

1. Follow the Submit app instruction / endpoint
2. Run this endpoint  
    curl -X POST ${ECR_API}/profile/sage/simple/1.0 -H "Authorization: sage token1"



How to check Database.

1. docker ps
2. docker -ti exec "mysql container id" bash
3. mysql -u sage -p test
4. show databases;
5. use SageECR;
6. show tables;
7. Select * From Apps;

Code Changes.
1. sample_app.yaml
2.