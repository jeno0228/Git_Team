from json import dump, load


rank = []
with open("code/member.json") as f1:
    data = load(f1)

for mem in data['user']:
            if mem['id']=="myname":
                mem['score'] = 20

with open('code/member.json', 'w') as f:
        dump(data, f, indent=2)
#for member in data['user']:
#    rank.append((member['id'],member['score']))
#print(rank)
#rank.sort(key=lambda x:x[1], reverse=True)
#print(rank[0][0])