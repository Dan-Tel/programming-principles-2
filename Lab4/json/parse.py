import json

f = open("Lab4\json\sample-data.json", "r")
data = json.loads(f.read())

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for item in data["imdata"]:
  dn = item["l1PhysIf"]["attributes"]["dn"]
  descr = item["l1PhysIf"]["attributes"]["descr"]
  speed = item["l1PhysIf"]["attributes"]["speed"]
  mtu = item["l1PhysIf"]["attributes"]["mtu"]
  print("{:<50} {:<20} {:<9} {:<6}".format(dn, descr, speed, mtu))