# https://medium.com/@harrietty/load-testing-an-api-with-apache-benchmark-or-jmeter-24cfe39d3a23
# GET 
ab -c 10 -n 500 -r http://localhost:5000/square/1

# POST 
# ab -c 10 -n 100 -p event.json -r -T application/json localhost:5000/square/1

# Watch over every second 
# watch -n 1 ab -c 10 -n 500 -r http://localhost:5000/square/1


# My section 
# Mock 
for i in {1..50}; do curl http://localhost:5000/square/"$i"; done

for i in {1..50}; do curl http://localhost:5000/cube/"$i"; done