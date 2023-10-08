FROM postgres:15-bullseye

COPY ./docker/local/postgres/maintanance /usr/local/bin/maintanance

RUN chmod +x /usr/local/bin/maintanance/*

RUN mv /usr/local/bin/maintanance/* /usr/local/bin/ \
    && rmdir /usr/local/bin/maintanance