#!/bin/bash
#This script sends a post request to the url
curl -s -X "POST" -d 'email=test@gmai.com' -d 'subject=I will always be here for PLD' $1
