from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
import pickle

df = pd.read_csv('BBFinalDataset.csv')

X = df.drop('GROUP',axis=1)
y = df['GROUP']

scaler = StandardScaler() 
scaler.fit(df.drop('GROUP',axis=1))

out = scaler.transform(df.drop('GROUP',axis=1))
df_scal = pd.DataFrame(out,columns=df.columns[:-1])

X_train, X_test, y_train, y_test = train_test_split(df_scal,df['GROUP'],test_size=0.30,random_state=101)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)

pickle.dump(knn, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
