Networking - assignment 2

The HTTPS-ws.py and JSON-ws.py programs run on port 3000, and HTTPS-ws.py is run on port 443
They were run using Python 3.8.5

JSON-ws.py -- The command used to run a POST operation for the JSON program was: "curl -i -X POST -H 'Content-Type: application/json' -d '{"operation" : "__", "arguments" : [_,_]}' localhost:3000"
HTTPS-ws.py -- The PEM pass phrase generated for the HTTPS file is sxk1093

The errors covered are:
400 -- if the request is impossible to process, meaning it doesn't follow the format of declaring an operation string and arguments integers
422 -- if the request has the right format but the operation isn't valid, ex dividing by 0