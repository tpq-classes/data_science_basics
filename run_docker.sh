docker run -ti -h ubuntu -v $(pwd):/root/live -p $1:$1 ubuntu:latest /bin/bash
