# jenkins-test-fredrick

hi this mission will make it that every push in the git up will start the jenkinsefile.
it will download ansible on your instance, (100% will work on aws linux cant promise the others)
run the build_playbook.yml that will download all that is needed.
the jenkinsfile created the container using docker compose (inside the flask directory), it will check that they run correctly with curl and if so will push it to my reposotory.


whats needed!
get ssh between the jenkins server and the prodaction server 
create an iam role that will allow you to access the repo (or configure aws)
and create the nodes based on the jenkinsfile
