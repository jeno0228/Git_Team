import json

file_path = "code/member.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

a = []
i =0

in_str = input("회원가입하시겠습니까 아니면 로그인하시겠습니까? (회원가입/아무거나-로그인)")

i=0
while in_str=="회원가입":
    new_id = str(input("아이디을 입력해주세요:\n"))
    for member in json_data['user']:
        while member['id']==new_id:
            print(new_id+"라는 아이디가 이미 존재합니다.")
            new_id = input("다시 입력해주세요:\n")
    new_pw = str(input("비밀번호를 입력해주세요:\n"))
    json_data['user'].append({
        "id": new_id,
        "password": new_pw,
        "score": 0
    })
    
    with open('code/member.json', 'w') as f:
        json.dump(json_data, f, indent=2)

    print("회원가입이 완료 되었습니다.\n 아이디는 "+new_id+"이고 비밀번호는 "+new_pw+"입니다")
    in_str = input("회원가입하시겠습니까 아니면 로그인하시겠습니까?(회원가입/아무거나-로그인)")
whatid = input("아이디를 입력해주세요:\n")

for mem in json_data['user']:
    if mem['id']==whatid:
        a.append(i)
        real_pw = mem['password']
        current_score = mem['score']
    i=i+1
while len(a) == 0:
    print("아이디가 존재하지 않습니다.")
    whatid = input("아이디를 다시 입력해주세요:\n")
    i=0
    for mem in json_data['user']:
        if mem['id']==whatid:
            a.append(i)
        i=i+1
whatpw = input("비밀번호를 입력해주세요")
while whatpw != real_pw :
    print("비밀번호가 일치하지 않습니다.")
    whatpw = input("비밀번호를 다시입력해주세요.\n")
print("로그인 되셨습니다. 아이디는 "+str(whatid)+"이고 현재 score는 "+str(current_score)+"입니다")



