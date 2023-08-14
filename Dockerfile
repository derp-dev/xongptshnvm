docker pull nvcr.io/nvidia/nemo:23.06

docker run --runtime=nvidia -it --rm \
  -v \
  --shm-size=16g \
  -p 8888:8888 \
  -p 6006:6006 \
  --ulimit memlock=-1 \
  --ulimit stack=67108864 \
  nvcr.io/nvidia/nemo:23.06
  