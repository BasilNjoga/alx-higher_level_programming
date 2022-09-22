#!/bin/bash
#This script displays all http methods accepted
curl -s -v -X OPTIONS $1
