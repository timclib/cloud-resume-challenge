#!/bin/bash
set -e

RESOURCE_GROUP="cloud-resume"
LOCATION="eastus"
STORAGE_NAME="timcloudresume2026"

az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION

az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file azure/bicep/main.bicep \
  --parameters storageAccountName=$STORAGE_NAME