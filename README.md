# Near monitoring stack

Monitoring stack based on Prometheus and Grafana. Uses official near image.

# Requirements

- Docker 19 or later
- Docker compose 1.26 or later

# Installation

1) Edit docker-compose and replace `YOUR_BETANET_ACCOUNT_ID` with your accound ID
2) Run `docker-compose up -d` and then check that every container is up
3) Authorize in Grafana at `http://your_host_ip:3000`. At first login you will be asked to set a new password. Default credentials are `admin/admin`
4) Import NEAR dashboard from file `grafana/dashboards/near.json`
5) Have fun

# Alert manager
  todo

### Todos

 - write alert manager instructions
 - upload dashboard at Grafana Labs
 - add alarm for need to update NEAR

License
----

MIT