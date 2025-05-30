
# ThinkTank CLI Deployment Guide

## Manual Deployment Process
1. Build: `docker build -t thinktankregistry.azurecr.io/thinktankcli:latest .`
2. Push: `docker push thinktankregistry.azurecr.io/thinktankcli:latest`
3. Deploy: `az webapp config container set --name ttank-webapp-g15 --resource-group [your-rg] --docker-custom-image-name thinktankregistry.azurecr.io/thinktankcli:latest`
