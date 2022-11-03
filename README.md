# Women's E-Commerce Clothing Reviews Data Analysis

Software and data analysis considerations on the _Women’s Clothing E-Commerce dataset_ from Kaggle.

_This is a Women’s Clothing E-Commerce dataset revolving around the reviews written by customers. Its nine supportive features offer a great environment to parse out the text through its multiple dimensions. The dataset available on Kaggle, and can be download it from this link: https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews._

There are several files in this repository that answer some tasks that I wanted to confront:

1) **Task 1:** Refactored code to create a base class and other classes that inherit from the base class (see `data_app/preprocessing.py` file).

2) **Task 2:** Algorithm selection that reduces the time complexity of the grid search in place of searching for the regularization parameter of the logistic regression algorithm (see `data_app/optimizer.py` file).

3) **Task 3:** API for CRUD operations (see `data_app/application.py`, `data_app/data.py` files and `data_app.py` which uses the two aforementioned files). Run `data_app.py` to create database and load CSV data to it, and see read, add, update and delete API methods run.

4) **Task 4:** Inference API for predictions from data science model (see `inference.py` file). Contains two test review cases.
