# playwright

# build
```sh
docker build -t [image_name] .
```

# run test.
```sh
docker run --name [container_name] -it [image_name] /bin/bash
```

# run test. exit for remove container
```sh
docker run --rm --name [container_name] -it [image_name] /bin/bash
```