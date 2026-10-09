FROM alpine:3.20 AS build
RUN apk add --no-cache build-base autoconf automake
WORKDIR /src
COPY . .
RUN ./configure && make && make check

FROM alpine:3.20
COPY --from=build /src/app /usr/local/bin/app
USER nobody
ENTRYPOINT ["/usr/local/bin/app"]
