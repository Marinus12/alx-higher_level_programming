#!/bin/bash
# Takes ina aURL as an argument sends a GET request to the URL
# And displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"