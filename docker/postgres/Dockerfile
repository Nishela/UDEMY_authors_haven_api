FROM postgres:15-bullseye

COPY ./docker/postgres/maintanance /usr/bin/maintanance

RUN chmod +x /usr/bin/maintanance/*

RUN mv /usr/bin/maintanance/* /usr/bin/ \
    && rmdir /usr/bin/maintanance