This project is a web app that is used to predict the price of properties in Banglaore.

For this project the datasets is used which contains the price of the various areas in Bangalore along with their features like bhk,no of bathrooms,area,price per squareFoot and the other important features.

The Linear Regression model is used which has an accuracy of almost 91 percent and this is furhter deployed to a web App using Flask Server.

The Link of the dataset: [https://www.kaggle.com/datasets/bhavik0901/bangalore-house-price-prediction](url)

Model Training: 
The dataset contains 13,000 price of data,In the pre processing stage all the null values are removed and the outliers are removed for each column , the missing values in thhe dataset are filled.Also some new features are added to remove outliers like Price per square Foot.
The location Column is One Hot Encoded.Ridge and Lasso Regression are furhter applied to improve the accuracy of the model.

The train and the test split is 80% and 20% for this model.

![image](https://github.com/CuntAdnan/PropertyPricePrediction/assets/98183132/ff435390-8a88-4422-9cf5-bc566a59715f)

![image](https://github.com/CuntAdnan/PropertyPricePrediction/assets/98183132/82223a42-73f3-4099-8057-293db575eb9d)


After the model is created is it converted to a pickle file and then deployed to a Flask Server
