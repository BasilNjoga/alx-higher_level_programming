#!/bin/bash
#This script sends a post request to the url
curl -s -X "POST" -F 'email=test@gmai.com' -F 'subject=I will always be here for PLD' $1
