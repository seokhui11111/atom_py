import simplejson as json

#Dict (json) 선언
data={} #Dict {[],[],[]}
data['people'] = [] #array
data['people'].append(
    {'name':'kim',
    'website':'naver.com',
    'from':'Seoul'
    }
)
data['people'].append(
    {'name':'park',
    'website':'google.com',
    'from':'Busan'
    }
)
data['people'].append(
    {'name':'lee',
    'website':'daum.net',
    'from':'Incheon'
    }
)
print(type(data))
print(data) #Dict

#Dict -> str(json) 직렬화
e=json.dumps(data,indent=4)
print(type(e))
print(e)

#str -> Dict(json) 역직렬화
d=json.loads(e)
print(type(d))
print(d)

with open('D:/atom_py/section4/member.json','w',encoding='utf-8') as outFile:
    outFile.write(e)

with open('D:/atom_py/section4/member.json','r',encoding='utf-8') as inFile:
    r=json.loads(inFile.read())
    print('================')
    print(type(r))
    print(r)

    for p in r['people']:
        print('Name : ' + p['name'])
        print('Website : ' + p['website'])
        print('From : ' + p['from'])
        print('')
