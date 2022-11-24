import pickle


def get_all_data():
    try:
        with open("data.p",'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def add_id(id, password):
    data = get_all_data()
    assert id not in data
    data[id] = {'id':id,'password':password}
    with open('data.p','wb') as f:
        pickle.dump(data,f)

def get_data(id):
    data = get_all_data()
    return data[id]

add_id('admin','password1')

data = get_data(id)
print(data['id'])
print(data['password'])




