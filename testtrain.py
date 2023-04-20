from sklearn.tree import DecisionTreeClassifier

# Define the training data and labels
data = [    
    [34, 80],
    [25, 85],
    [48, 90],
    [61, 95],
    [76, 100],
    [43, 105],
    [19, 110],
    [52, 115],
    [27, 120],
    [69, 125],
    [32, 130],
    [44, 145],
    [59, 135],
    [12, 120],
    [39, 150],
    [70, 160],
    [23, 175],
    [80, 140],
    [36, 112],
    [50, 140]
]
dict ={0:"a",1:"b",2:"c",3:"d",4:"e"}
y_train =[0, 0, 0, 1, 1, 1, 2, 2, 2, 3,3, 3, 4, 4,3,2,1,2,4,1]
# print(len(y_train)==len(data))
# Create a decision tree classifier and fit it to the training data
clf = DecisionTreeClassifier()
clf.fit(data, y_train)

# Make predictions on new data
X_test = []
print("number of participants:")
t=int(input())
for item in range(t):
    l1=[0,0]
    l1[0]=int(input())
    l1[1]=int(input())
    # l1[2]=int(input())
    X_test.append(l1)
    
y_pred = clf.predict(X_test)
print(dict[y_pred[0]])
# Print the predicted labels

