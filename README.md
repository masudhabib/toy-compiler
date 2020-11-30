# Toy compiler with Python

## Set up instruction
<b>Option 1</b> - Use Docker 

A Dockerfile is included to streamline the installation process. This will create a Linux container for the toy compiler to be run on.

To build the image from the Dockerfile

```
docker build -t toy_llvm .
```

To start the container

```
docker run -it toy_llvm /bin/bash
```

<b>Option 2</b> - Set up the dependencies manually

Requirements: Anaconda is preferred as it is easy to install some of the packages

```
conda install --channel=numba llvmlite
conda install -c conda-forge rply
apt-get -y install clang
apt-get -y install gcc
```

## Run the compiler
1. Make changes to `input.toy`
The input for the program is located in the `input.toy` program. It translates the text into machine readable language

2. Convert `input.toy` into c program
```
python main.py
clang output.ll -c -o output.o
gcc output.o -o output
```

3. Run the compiler
```
./output
```

