import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    def load_data(self):

        self.dataset['bmi'] = self.dataset['bmi'].fillna(self.dataset['bmi'].mean())

        #self.dataset['gender'] = self.dataset['gender'].replace({'Male': 0, 'Female': 1, 'Other': 0})

        #self.dataset['ever_married'] = self.dataset['ever_married'].replace({'No': 0, 'Yes': 1})

        #self.dataset['age'] = self.dataset['age'].astype(int)
        self.dataset['age'] = pd.cut(self.dataset['age'], 16)

        #self.dataset['avg_glucose_level'] = self.dataset['avg_glucose_level'].astype(int)
        self.dataset['avg_glucose_level'] = pd.cut(self.dataset['avg_glucose_level'], 16)

        #self.dataset['bmi'] = self.dataset['bmi'].astype(int)
        self.dataset['bmi'] = pd.cut(self.dataset['bmi'], 16)

        #Sadge
        #self.dataset = pd.get_dummies(self.dataset, columns=['work_type'])
        #self.dataset['work_type'] = self.dataset['work_type'].replace({'Never_worked': 0, 'children': 1, 'Private': 2, 'Govt_job': 3, 'Self-employed': 4})


        #self.dataset['Residence_type'] = self.dataset['Residence_type'].replace({'Rural': 0, 'Urban': 1})



        #self.dataset.loc[(self.dataset['smoking_status'] == 'Unknown') & (self.dataset['heart_disease'] == 1), 'smoking_status'] = 'smokes'
        #self.dataset.loc[(self.dataset['smoking_status'] == 'Unknown') & (self.dataset['heart_disease'] == 0), 'smoking_status'] = 'never smoked'
        #self.dataset.loc[(self.dataset['smoking_status'] == 'Unknown') & (self.dataset['bmi'] == 3), 'smoking_status'] = 'formerly smoked'
        #self.dataset['smoking_status'] = self.dataset['smoking_status'].replace({'never smoked': 0, 'formerly smoked': 1, 'smokes': 2})



        le = LabelEncoder()

        le.fit(self.dataset['age'])
        self.dataset['age'] = le.transform(self.dataset['age'])

        le.fit(self.dataset['avg_glucose_level'])
        self.dataset['avg_glucose_level'] = le.transform(self.dataset['avg_glucose_level'])

        le.fit(self.dataset['bmi'])
        self.dataset['bmi'] = le.transform(self.dataset['bmi'])

        le.fit(self.dataset['gender'])
        self.dataset['gender'] = le.transform(self.dataset['gender'])

        le.fit(self.dataset['ever_married'])
        self.dataset['ever_married'] = le.transform(self.dataset['ever_married'])

        le.fit(self.dataset['work_type'])
        self.dataset['work_type'] = le.transform(self.dataset['work_type'])

        le.fit(self.dataset['Residence_type'])
        self.dataset['Residence_type'] = le.transform(self.dataset['Residence_type'])

        le.fit(self.dataset['smoking_status'])
        self.dataset['smoking_status'] = le.transform(self.dataset['smoking_status'])

        self.dataset['bmi'] = self.dataset['bmi'].replace({4: 3})


        return self.dataset




