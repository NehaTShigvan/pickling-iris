
import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
info = requests.get(url).text       #fetching data from the website
#storing the data fetched from the website in a file
with open("iris.txt",'w') as f:
    f.write(info)

#opening a file in read mode 
with open("iris.txt",'r') as f:
    data = f.readlines()

#making a list containing a list of each line in a file
iris_list = [i.split(",") for i in data]
# print(iris_list)

#pickling
file = 'iris.pkl'
file_obj = open(file,"wb")
pickle.dump(iris_list,file_obj)
file_obj.close()

#unpickling
file_obj = open(file,'rb')
iris_data = pickle.load(file_obj)
print(iris_data)