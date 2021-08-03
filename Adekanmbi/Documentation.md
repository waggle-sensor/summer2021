Documentation for the implementing of profiling in ECR



#### Profile Database Schema

SageECR.Profiles

| Syntax      | Description |
| ----------- | ----------- |
| id          | VARCHAR(194) UNIQUE NOT NULL      |
| namespace   | VARCHAR(64) |
| name        | VARCHAR(64) |
| version     | VARCHAR(64) |
| time_created | TIMESTAMP DEFAULT CURRENT_TIMESTAMP |
| time_last_updated | TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP |
| app_profile | VARCHAR(256) |
| INDEX(id, namespace, name, version) |



#### ecr_api.py 

to trigger a app profile build in jenkins
curl -X POST ${ECR_API}/profile/sage/simple/1.0 -H "Authorization: sage token1"

app.add_url_rule('/profile/<string:namespace>/<string:repository>/<string:version>' view_func=Profile_build.as_view('profilebuildAPI'))

api endpoint calls the profile_build method

```
def post ()
    results = profile_app()
```




How to run profiling on ECR.

1. Follow the Submit app instruction / endpoint
2. Run this endpoint  
    curl -X POST ${ECR_API}/profile/sage/simple/1.0 -H "Authorization: sage token1"





### How to verify database

1. docker ps
2. docker -ti exec "mysql container id" bash
3. mysql -u sage -p test
4. show databases;
5. use SageECR;
6. show tables;
7. Select * From Apps;
