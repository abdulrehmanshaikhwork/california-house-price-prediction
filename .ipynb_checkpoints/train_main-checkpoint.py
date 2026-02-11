import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score

#1. Load The DataSet
housing = pd.read_csv("housing.csv")

#2. Create a Income Category
housing['income_cat'] = pd.cut(housing["median_income"], 
bins = [0.0, 1.5, 3.0, 4.5, 6.0, np.inf], 
labels = [1, 2, 3, 4, 5])

#3. Create a Stratified TestSet
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
     strat_train_set = housing.loc[train_index].drop('income_cat', axis=1)
     strat_test_set = housing.loc[test_index].drop('income_cat', axis=1)

#4. We will work on the copy of training data
housing = strat_train_set.copy()

#5. Seperate features and labels
housing_labels = housing['median_house_value'].copy()
housing = housing.drop('median_house_value', axis=1)

print(housing, housing_labels)

#6. List Numerical and categorical columns
num_attribs = housing.drop('ocean_proximity', axis=1).columns.tolist()
cat_attribs = ['ocean_proximity']

#7. Lets make the pipeline 

#(i) for numerical columns
num_pipeline = Pipeline([
     ("imputer", SimpleImputer(strategy="median")),
     ("scaler", StandardScaler()),
])

#(ii) for categorical columns
cat_pipeline = Pipeline([
     ("onehot", OneHotEncoder(handle_unknown='ignore')),
])

#8. Construct the full pipeline
full_pipeline = ColumnTransformer([
     ("num", num_pipeline, num_attribs),
     ("cat", cat_pipeline, cat_attribs)
])

#9. Transform The Data
housing_prepared = full_pipeline.fit_transform(housing)
print(housing_prepared.shape)

#10. Train the model
#(i) Linear regression 
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)
lin_preds = lin_reg.predict(housing_prepared)
lin_rmse = -cross_val_score(lin_reg, housing_prepared, housing_labels, scoring='neg_root_mean_squared_error', cv=10)
#print(f"The Root Mean Square Error for Linear Regression is {lin_rmse}")
print(pd.Series(lin_rmse).describe())

#(ii) Decision Tree
des_tree = DecisionTreeRegressor()
des_tree.fit(housing_prepared, housing_labels)
des_preds = des_tree.predict(housing_prepared)
#des_rmse = root_mean_squared_error(housing_labels, des_preds)
des_rmse = -cross_val_score(des_tree, housing_prepared, housing_labels, scoring='neg_root_mean_squared_error', cv=10)
#print(f"The Root Mean Square Error for Decision Tree Regressor is {des_rmse}")
print(pd.Series(des_rmse).describe())

#(iii) Random Forest
ran_for = RandomForestRegressor()
ran_for.fit(housing_prepared, housing_labels)
ran_for_preds = ran_for.predict(housing_prepared)
ran_rmse = -cross_val_score(ran_for, housing_prepared, housing_labels, scoring='neg_root_mean_squared_error', cv=10)
#print(f"The Root Mean Square Error for Random Forest Regressor  is {ran_rmse}")
print(pd.Series(ran_rmse).describe())
