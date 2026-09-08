FROM alpine:3.19
RUN apk add --no-cache build-base
WORKDIR /src
COPY . .
RUN make
ENTRYPOINT ["/src/app"]
