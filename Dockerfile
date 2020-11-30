FROM continuumio/anaconda

WORKDIR /app

RUN conda install --channel=numba llvmlite \
    && conda install -c conda-forge rply

# Utility for compiler
RUN apt-get update
RUN apt-get -y install clang && apt-get -y install gcc

COPY . .
