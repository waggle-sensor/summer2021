Documentation for the implementing of profiling in ECR

#### API Endpoint to trigger profiling

Use this to trigger a app profile build in Jenkins

```
curl -X POST ${ECR_API}/profile/sage/simple/1.0 -H "Authorization: sage token1"
```

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

app.add_url_rule('/profile/<string:namespace>/<string:repository>/<string:version>' view_func=Profile_build.as_view('profilebuildAPI'))

class definition for profiling. [Using pluggable views] (https://flask.palletsprojects.com/en/2.0.x/views/#method-views-for-apis). The class consist of get and post functions that processes both the GET and POST request respectively.

def get - function retrieves the app information stored in ECR database returns a build information or error if app not found.
def post - function calls profile_app function as well a returning build information

```
class Profile_build(MethodView):
    @login_required
    @has_resource_permission( "READ" )
    #def get(self, app_id):
    def get(self, namespace, repository, version):

        #namespace, repository, version
        requestUser = request.environ.get('user', "")
        isAdmin = request.environ.get('admin', False)

        try:
            result = get_build(requestUser,isAdmin, namespace, repository, version)
        except ErrorResponse as e:
            raise e
        except Exception as e:
            raise ErrorResponse(f"get_build returned: {type(e).__name__},{str(e)}", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)


        return jsonify(result)

    @login_required
    @has_resource_permission( "FULL_CONTROL" )
    def post(self, namespace, repository, version):

        requestUser = request.environ.get('user', "")
        isAdmin = request.environ.get('admin', False)

        skip_image_push = request.args.get('skip_image_push', "") in ["true", "1"]

        result = profile_app(requestUser, isAdmin, namespace, repository, version, skip_image_push=skip_image_push)
        return jsonify(result)

```

2. def profile_app - function checks if there are any current Jenkins jobs and triggers a Jenkins job to build the required app.


```
def profile_app(requestUser, isAdmin, namespace, repository, version, skip_image_push=False):
    
    host = config.jenkins_server
    username = config.jenkins_user
    password = config.jenkins_token

    try:

        js = jenkins_server.JenkinsServer(host, username, password)
    except Exception as e:
        raise ErrorResponse(f'JenkinsServer({host}, {username}) returned: {str(e)}', status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

    ecr_db = ecrdb.EcrDB()
    app_spec, ok = ecr_db.listApps(user=requestUser , namespace=namespace, repository=repository, version=version, isAdmin=isAdmin)
    if not ok:
        return {"error":f"app_spec not found {namespace}/{repository}:{version}"}

    app_id = app_spec.get("id", "")
    if not app_id:
        return {"error":"app id not found"}

    source = app_spec.get("source", None)
    if not source:
        return {"error":"source  not found"}

    app_human_id = createJenkinsName(app_spec)



    overwrite=False
    if js.hasJenkinsJob(app_human_id):
        overwrite =  True

    try:
        js.createProfileJob(app_human_id, app_spec, overwrite=overwrite, skip_image_push=skip_image_push)
    except Exception as e:
        raise ErrorResponse(f'createJob() returned: {str(e)}', status_code=HTTPStatus.INTERNAL_SERVER_ERROR)


        
    queue_item_number = js.build_job(app_human_id)


    queue_item = None

    # this loop will wait for Jenkins to return build number
    # note that the previous queue_item_number is a temporary global queue number which will be useless after some time.
    number = -1
    while number == -1:
        time.sleep(2)

        try:
            queue_item = js.server.get_queue_item(queue_item_number)
        except Exception as e: # pragma: no cover

            if not "does not exist" in str(e):
                raise ErrorResponse(f'get_queue_item() returned: {str(e)}', status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

        if not queue_item:
            continue

        executable=queue_item.get("executable", None)
        if not executable:
            continue

        number = executable.get("number", None)
        if not number: # pragma: no cover
            continue

        break


    build_name = "some name"
    architectures = source.get("architectures", None)
    if not architectures:
        raise ErrorResponse(f'architectures not specified in source', status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

    try:
        ecr_db.SaveBuildInfo(app_id, build_name, number, architectures)

    except Exception as e:
        raise ErrorResponse(f'error inserting build info for {app_id}, {build_name}, {number} , SaveBuildInfo: {str(e)}', status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

    #time.sleep(6)

    #queued_item = js.server.get_queue_item(queue_item_number)

    #returnObj = {"queue_item_number":queue_item_number, "queued_item": queued_item}
    #return returnObj
    build_request_counter.inc(1)
    return {"build_number": number }

```

### jenkins_server.py

3. def createProfileJob - function triggers a profiling Jenkins job, using the Jenkins template app spec information are passed.

```
 
    def createProfileJob(self, id, app_spec, overwrite=False, skip_image_push=False):
    
            # format https://github.com/user/repo.git#v1.0


            version = app_spec["version"]

            source=app_spec.get("source", None)
            if not source :
                raise Exception("field source empty")
  

            git_url = source.get("url", "")
            git_branch = source.get("branch", "main")
            git_directory = source.get("directory", ".")
            if git_directory.startswith("/"):
                git_directory=git_directory[1:]

            platforms = source.get("architectures", [])
            if len(platforms) == 0:
                raise Exception("No architectures specified")
            platforms_str = ",".join(platforms)

            platforms_list = " ".join(platforms)

            build_args = source.get("build_args", {})
            build_args_command_line = ""
            for key in build_args:
                value = build_args[key]
                build_args_command_line += f" --build-arg {key}={value}"

            if docker_build_args != "":
                build_args_command_line += f" {docker_build_args}"


            actual_namespace = ""
            namespace = app_spec.get("namespace", "")
            if len(namespace) > 0:
                actual_namespace = namespace
            else:
                actual_namespace = app_spec.get("owner", "")

            # The registry user credentials are defined in the casc_jenkins.yaml file.
            docker_login='''withCredentials([usernamePassword(credentialsId: 'registry-user', passwordVariable: 'REGISTRY_USER_PWD', usernameVariable: 'REGISTRY_USERNAME')]) {
                    sh 'echo $REGISTRY_USER_PWD | docker login -u $REGISTRY_USERNAME --password-stdin ''' +docker_registry_url +''''
                }
            '''

            do_push="--push"
            if skip_image_push:
                docker_login = ""
                do_push =""
            
            name = app_spec["name"]

            template = Template(jenkinsfileTemplateProfile)

            name_app = namespace + "/" + name + ":" + version

            try:
                jenkinsfile = template.substitute(  url=git_url,
                                                    branch=git_branch,
                                                    directory=git_directory,
                                                    namespace=actual_namespace,
                                                    name=name,
                                                    version=version,
                                                    platforms=platforms_str,
                                                    build_args_command_line=build_args_command_line,
                                                    docker_registry_url=docker_registry_url,
                                                    docker_login=docker_login,
                                                    platforms_list = platforms_list,
                                                    app_docker_args = "-v /tmp/data-config.json:/run/waggle/data-config.json",
                                                    app_args = "-stream top_live -object car -interval 1",
                                                    app_name = "waggle/plugin-objectcounter:0.0.0",
                                                    k = "sage/simple:1.0 .",
                                                    c = name_app,
                                                    app_url = "https://github.com/waggle-sensor/application-profiling.git",
                                                    app_branch = "tool-suite",
                                                    app_dir = ".",
                                                    d = "localhost:5002/profiling-agent:latest",
                                                    do_push=do_push)
            except Exception as e:
                raise Exception(f'  url={git_url}, branch={git_branch}, directory={git_directory}  e={str(e)}')

            #print(jenkins.EMPTY_CONFIG_XML)
            newJob = createPipelineJobConfig(jenkinsfile, f'{actual_namespace}/{name}')
            print(newJob)




            newJob_xml = xmltodict.unparse(newJob) #.decode("utf-8")
            #print("------")
            #print(newJob_xml)
            #print("------")
            #print(jenkins.EMPTY_CONFIG_XML)
            #print("------")

            if overwrite:
                self.server.reconfig_job(id , newJob_xml)
            else:
                self.server.create_job(id, newJob_xml)


            timeout = 10

            while True:
                try:

                    my_job = self.server.get_job_config(id)
                    return my_job
                except jenkins.NotFoundException as e: # pragma: no cover
                    pass
                except Exception as e: # pragma: no cover
                    raise

                if True: # pragma: no cover
                    time.sleep(2)
                    timeout -= 2

                    if timeout <= 0:
                        raise Exception(f'timeout after job creation')
                    continue


            return 1
            #print("jobs: "+server.jobs_count())




def createPipelineJobConfig(jenkinsfile, displayName):
        jenkins_job_example_xml = '''<?xml version='1.1' encoding='UTF-8'?>
        <flow-definition plugin="workflow-job@2.39">
        <displayName>overwrite_me</displayName>
        <description></description>
        <keepDependencies>false</keepDependencies>
        <properties/>
        <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition" plugin="workflow-cps@2.80">
            <script>pipeline {
        agent any

        stages {
            stage(&apos;Hello&apos;) {
                steps {
                    echo &apos;Hello World&apos;
                }
            }
        }
        }
        </script>
            <sandbox>true</sandbox>
        </definition>
        <triggers/>
        <quietPeriod>0</quietPeriod>
        <disabled>false</disabled>
        </flow-definition>
        '''



        job = xmltodict.parse(jenkins_job_example_xml)

        #jenkinsfile = 'pipeline {}'
        print(json.dumps(job, indent=4))

        job["flow-definition"]["definition"]["script"] = jenkinsfile # cgi.escape(jenkinsfile)
        job["flow-definition"]["displayName"] = displayName
        #job["project"]["scm"]["userRemoteConfigs"]["hudson.plugins.git.UserRemoteConfig"]["url"] = 'https://github.com/sagecontinuum/sage-cli.git'


        print(json.dumps(job, indent=4))
        return job

```

### config.py

jenkinsfileTemplateProfile - defines the Jenkins template used by the Jenkins job.

```
jenkinsfileTemplateProfile = '''
  node('master') {        
            stage ('Profile Build'){

                    git branch: '${branch}',
                        url: '${url}'
                    dir("$${env.WORKSPACE}/${directory}"){
                        docker.withRegistry('https://localhost:5002') {
                            def customImage = docker.build("${c}")
                            customImage.push()
                        }
                }
            }

            stage ('Profiler Image'){
                git branch: '${app_branch}',
                    url: '${app_url}'

                docker.withRegistry('https://localhost:5002') {
                    def Image = docker.image("${c}")
                    Image.pull()
                             
                    dir("$${env.WORKSPACE}/${app_dir}"){  
                        def server_container_build = docker.build('profiling-agent', '--build-arg APP_NAME=${c} .')
                          server_container_build.push('latest')
                    }    

                }

            }

             stage ('Profiling'){
                    git branch: '${branch}',
                        url: '${url}'
                     dir("$${env.WORKSPACE}/${directory}"){
                    docker.withRegistry('https://localhost:5002') {

                        docker.image('profiling-agent'). withRun('-t --entrypoint /bin/bash --volumes-from jenkins --network host ${app_docker_args}') {
                              // sh 'mkdir profile_output'
                               echo "The Docker container has finished, stashing profile metrics..."
                               sh 'ls -l'
                                
                        }

                    }
                }
            }

        stage ('Saving Profile Output'){
                sh """
                    if [ -d "$${env.WORKSPACE}/profile_output" ] 
                    then
                         docker exec -i sage-ecr_db_1 mysql -usage -ptest -e 'USE SageECR;UPDATE Profiles SET app_profile = "${namespace}/${name}/profile_output" WHERE namespace = "sage" ; '
                    else
                        echo "Error: Directory profile_output does not exists."
                    fi
                """
                sh 'ls -l'

        }
        
}
        
'''

```

### How to run app profile

1. Build ECR with command

```./run.sh -d --build
  ```

2. Follow [documentation](https://github.com/sagecontinuum/sage-ecr/blob/master/docs/api_spec.md) to submit app

3. Trigger app profile command

```
curl -X POST ${ECR_API}/profile/{namespace}/{name}/{version} -H "Authorization: sage token1"
e.g curl -X POST ${ECR_API}/profile/sage/simple/1.0 -H "Authorization: sage token1"
```

### How to debug and verify database

1. docker ps
2. docker -ti exec "mysql container id" bash
3. mysql -u sage -p test
4. show databases;
5. use SageECR;
6. show tables;
7. Select * From Profiles;
