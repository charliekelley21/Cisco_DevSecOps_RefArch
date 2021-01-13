# go-hokies

To run the container please type the command
docker-compose up

The port it is running on is http://localhost:5000/

Before each commit please run hook.sh to validate that all libraries have been imported correctly.
PyTests run each time new code is pushed to the repository. The docker image is updated for each push as
well and this is done using GitActions.

