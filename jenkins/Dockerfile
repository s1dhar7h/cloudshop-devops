FROM docker:28-cli AS dockercli

FROM jenkins/jenkins:lts-jdk21

USER root

COPY --from=dockercli /usr/local/bin/docker /usr/local/bin/docker
COPY --from=dockercli /usr/local/libexec/docker/cli-plugins /usr/local/libexec/docker/cli-plugins



#
# FROM jenkins/jenkins:lts-jdk21

# USER root

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends docker.io && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*