forwarder_name = "melee1"
log_count = 2511232
threshold = 100

if log_count == 0:
    print ("Crit Crit this node is silent")
elif log_count < threshold:
    print ("Warning, log count is being sketchy")
else:
    print ("Normal Operation")