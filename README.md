# Topic 2 -- Logistic Regression 

## Overview of this Repository
This repository contains all the teaching material related to **Logistic Regression**. The master `branch` contains the sample code for the instructor to **reference**, and the `workshop` branch contains the **empty notebooks** for the instructor and students to program in.

## For the Instructors:

This section details instructions to guide the instructor in delivering the course. The instructor should fill out the blank notebooks in the `workshop` branch according to the reference in the `master` branch (if it is possible, use dual monitors so you can have the reference code opened side by side.) **There will be function calls already written in the blank notebook, please run those calls without modifications.**

Below is the curriculum of this repository, as well as the order of content to be delivered. **Be sure to familiarize yourself with the code before teaching! Feel free to explore the notebooks as well as the web app `suv.py`**.

### Getting set up (Jupyter Notebook)
1. Clone this repo into a working directory and switch to the **workshop** branch.
2. Create and activate a virtual environment with the command below:
```bash
# MacOS/Linux
$ python3 -m venv env
$ source env/bin/activate
```
```bat
:: Windows
\> python -m venv env
\> .\env\Scripts\activate
```
3. If you are in the virtual environment, you should see the `(env)` marker. Now, install all the dependencies:
```bash
# MacOS/Linux
$ pip install -r requirements.txt
```
```bat
:: Windows
\> python -m pip install -r requirements.txt
```
4. You are ready to go! 

### Getting set up (Google Colab)
1. Clone this repo into a working directory and switch to the **workshop** branch.
2. Open the desired notebook in Google Colab
3. Unzip your `colab.zip` file in Google Colab
4. In your notebook, be sure to install the necessary dependencies. Do not install directly from `requirements.txt`
5. You are ready to go! 


## Topic 2 -- Logistic Regression Notebook

#### Installing Dependencies
- Talk a bit about the dependencies to install (eg. what each module is used for)
- Import the modules in the notebook

#### Linear Regression vs Classification
- Introduce classification example: Given your height, are you going to be admitted into the NBA? (Yes, No)
    - display the height dataset `display_height_dataset()`
    - describe the dataset (eg. "This person is 1.5 m tall, therefore he did not get admitted into the NBA")
- describe fitting a linear regression model to our data
    - `display_height_line1()`
    - paraphrase the paragragh below, talking about representing the output as a probability, and letting that decide whether to predict 0 or 1.
    - Note the shortcomings of linear regression
    - talk about adding an outlier, and visualize the fit: `display_height_line2()` 
    - talk about how linear regression is affected by outliers and is not bounded between 0 and 1, therefore unsuitable for classification problems

#### Logistic Regression
- Similarities with Linear Regression

#### Sigmoid Function
- Talk about the sigmoid activation function, what it does, etc
    - Fill out the body of `def sigmoid(z)`.
    - `display_func(sigmoid)`

#### Cost Function
- Different cost function to account for the sigmoid function (BCE)
    - Talk about the idea of convex and non-convex function, why we need to have convex cost functions (gradient descent)
    - `disp_convex()`

#### Putting it All Together
- Go through the pseudo-code
    - highlight the similarities and differences between linear and logistic regression
- desmos link, move the sliders `w` and `b` to fit the data
- geogebra link for visualizations in 3D

#### Binary Classifications
- Talk about classifing on to output states
- NBA Example: admitted? (yes, no)

#### Pokemon Classification Problem
- Setting the problem: Is the pokemon legendary or not? 
    - load the dataset and display it
    - Note the `is_legendary` column: all legendary pokemons are at the bottom
- Therefore, we need to shuffle the data. Write code to shuffle the data
    
#### Choosing our Features
- Choose our features based on whether or not we think there will be correlations with the output
    - This is done to simplify this example, to make training faster, but we don't necessarily have to use only those features.

#### Imbalanced Classes
- read the intuition
- print out the number of positive and negative features to see if there is any imbalance.

#### Training our Logistic Regression Model
- Be sure to highlight the similarities and differences between the linear regression model
- note the class weights used to balance the imbalanced dataset.
- At the end of training, highlight the differences in evaluation metrics
    - what is accuracy
    - what is F1 score
    - why those over R2 score

#### Confusion Matrix
- Highlight the use of confusion matrix
    - to get a better understanding of where the model is predicting wrong, how is it predicting wrong, is it acceptable, etc.

#### Observations
- let students note the results of the model, and learn to record their findings.

#### Multi-Class Classification
- predicting one out of the many classes
- Problems with label encoding (classes = [0, 1, 2, 3, ..., n])

#### One vs All
- Talk about training 4 classifiers for the example above, one for each class
- whichever output is the highest, the model will predict that class

#### One Hot Encoding
- contrast that against label encoding
- describe the np.arrays shown on screen

#### Choosing our features
- Identify the problem we are trying to solve: (Fire, water, grass or none of the above?)
- Ask students to think about which features would they pick to solve the problem

#### Choosing our label
- Remind students that we want to have a One-Hot encoding of `Fire`, `Water`, `Grass`, and `NA`
- Use `pd.get_dummies()` to form dummies
- Be sure to print out the dataframes so students can visualize the data

#### Training the Multi-class Classifier
- Demonstrate the `OneVsRestClassifier()`, make sure students understand that it is basically training 4 classifiers, one for each class
- 

#### Observations
- Note the results of the classifier
- create confusion matrix, letting students know that converting back into label encoding is necessary because sklearn.metrics.confusion_matrix is designed to work with label-encoding
- Write down the observations


## SUV Purchase Predictor Web App
#### Setting up the environment
- Start off by opening `suv_purchase.ipynb` in the jupyter notebook, as well as running `suv.py` in the **vscode terminal**. The web app can be opened in a browser by `CTRL` + left-clicking on the localhost address in the terminal when running `suv.py`
#### suv_purchase.ipynb
- Reference code has been commented, therefore read the comments to understand what the code is doing.
- This programming project is meant to be taught in a code-and-commentary style.
- It is recommended to review the reference code before teaching

#### Moving onto suv.py
- briefly give the students a tour of the web app
- fill out the blank portions of the python file, referencing the reference file.
- commentate as you go, make sure you are able to explain what each line of code does (comments are provided, and only exist in the portions you are going to fill out)
- work from top to bottom.







