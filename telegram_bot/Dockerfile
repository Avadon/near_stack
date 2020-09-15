FROM golang:1.14.4-alpine3.12 as builder

ADD . /prometheus_bot

RUN \
    cd / && \
    apk add --no-cache make tzdata && \
    cd prometheus_bot && \
    go get -d -v && \
    CGO_ENABLED=0 GOOS=linux go build -v -a -installsuffix cgo -o prometheus_bot 

FROM alpine:3.12
COPY --from=builder /prometheus_bot/prometheus_bot /
RUN apk add --no-cache ca-certificates tzdata tini
USER nobody
EXPOSE 9087
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/prometheus_bot"]
