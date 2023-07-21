# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
# RUN apt-get update && apt-get -y install wget curl jq vim net-tools bash tar

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt 
#--no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
# RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

# FROM builder as dev-envs

# RUN <<EOF
# apk update
# apk add git
# EOF

# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /