import csv
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# capturing data
data = []
with open('mydata2.csv','r') as f:
    reader = csv.reader(f)
    for i in reader:
        if len(i)>0:
            data.append(i)
final = data[1:]

# Feature and target set data
'''
feature set -
plyer_x,plyer_y,enemy_x,enemy_y,left,right
target set -
hit
'''
x = []
y = []
for i in final:
    x.append(i[:6])
    y.append(i[-1])

# splitting the training and testing data 70:30
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3)

# decision tree classifier creation
my_model = DecisionTreeClassifier()
my_model.fit(x_train,y_train)
y_pred = my_model.predict(x_test)
print('model trained')
print(metrics.accuracy_score(y_test,y_pred))# 72 - 75%


