# NBAdrafter
This is my personal project for the Machine Learning course at NYU Tandon School of Engineering.\
*Performed by Dutchak Bohdan* :sleeping:
<br><br>




## Description
Here will be description of the project generally, also pipelines, technologies explained etc etc.\
Some of the parts will be written on Python3. The reasons of it is the variety of different libraries and tools it has to collect, process and plot data. Also I feel more confident with this language.
<details>
  <summary>
    Expand
  </summary>

---
`data_parser.py`
  My python script to collect data from [NBA Reference](https://www.basketball-reference.com/). The data is about all players performance from season to season.
  Functions:
  - `get_teams_urls(year:int)` - returns list of subdirectories of URL of all teams of particular season ([Like this one](https://www.basketball-reference.com/teams/BRK/2022.html)), since through 20 years teams changed.
  - `get_column_names(table)` - returns list of column names of Roster and Per Game tables
  - `get_per_game(url)` - returns pd.DataFrame with data collected from Per Game table
  - `get_roster(url)` - returns pd.DataFrame with data collected from Roster table
  - `process_data(df : pd.DataFrame, year)` - performs some primary data processing such as converting height from feet to meters and pounds to kilograms
  - `append_data(season_data, team)` - concatenates team data into one seaon dataframe.

---
`data_merger.py`
  Simple script, that concatenates all season's data into one dataframe.

---
`config.py`
  Configurations.
  - `start_year` - beginning year, from which to collect data.
  - `end_year` - last year, from which to collect data.
  - `url` - Scheme and domains of the main URL.
  - `season_url` - Season URL for adding year and particular team to get page with data tables.
---
`EDA.ipynb`
  Exploratory Data Analysis for the collected data performed in R. As a result - list of the best features to be fitted into the model + some insights that help to choose it.

</details>
<br>



## Weekly progress
I like to keep my progress together. Also, since I messed up with deadlines, I decided to handle my progress here. Also, it can be formatted into a fancy page.\
Current progress: **[Week 11](https://github.com/bohdan-dutchak/NBAdrafter/blob/main/README.md#week-11)**.

<details>
  <summary>
    Show progress
  </summary>



<details>
<summary><h3>Week 1</h3></summary>
  This one is the pilot week, I will try to cope with everything.    
  
#### Work done
  - ISLR chptrs 1-2
  - Watched the lecture
  - Introduction to ML
  - [Cool vid about bias and variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)
#### Problems faced
  - None actually, but it is just a beginning
#### Next steps
  - Complete first 4 weeks and start the project.

#### Brief list of notes for this week 
  - There are two paradigms of estimation of the model:
    1. Prediction (focusing on the result i.e. the output variable)
    2. Inference (providing analytics of the different trends and relations between variables)
  - Regarding to the paradigms, there is a trade-off between more flexible (Deep learning, SVM, Boosting, Bagging, GAM) and more interpretable models (Lasso, OLS). The more flexible model is, the bigger *variance* it has and vice versa with *bias*.\
  Bias is kinda squared error, the worse model fits the training data, the bigger bias is.\
  Variance is the difference in fits between datasets.
  - Learning of the model can be supervised or unsupervised (more rarely semi-supervised), which depends on the existence of the response variable.
  - Very low MSE on training data may indicate overfitting.
  - bias-variance trade-off is an estimation method of test MSE by result train variable.
  - KNN is the model with optionally chosen K - the number of nearest neighbors. The smaller K is, the more flexible model.
</details>



<details>
<summary><h3>Week 2</h3></summary>

Week 2 took me a little, I should speed up.\
Anyways, it is about the LOGIT, LDA, QDA, KNN and NBayes.
  
#### Work done
  - [Confounding explained](https://www.youtube.com/watch?v=bcfg9kcxeuU)
  - ISLR chptr 4
  - Watched the lecture
#### Problems faced
  - In chapter 2 it is said, that it is hard to compute model accuracy on the testing data, since sometimes there is no test data. Why can't we just take a 30% of it as a data for testing. So we don't train model on this part.
  - Didn't get the baseline problem when we use k-1 classes. 
#### Next steps
  - I have a cool idea about the subject of my project, but I have to validate that it is reasonable to make it.
  - Also I should speed up reading the book.

#### Brief list of notes for this week   
  - You can use OLS to make classifier with 2 classes, but it is not recommended
  - In order to decrease risks of false positive we can manually decrease the threshold of the probability from 0.5 to i.e. 0.1
  - Confounding is a bias that leads to the wrong relation dependencies between some variable and result. Here we have example of probability of default given the person is student or not. Confounding misleads us to the conclusion that students are more risky creditee, but those are so only when the credit balance is unknown. Otherwise non-student is more risky.
  - While making a MLR there is choice between k-1 classes estimation with the baseline, but there are pitfalls there, so *softmax* is a better decision. It estimates the class by taking the biggest probability of all. The sum of probabilities are always 1.
  - Two types of errors:
    * Type 1 (false negative) - rejecting true $h_0$. We must avoid this error
    * Type 2 (false positive) - accepting $h_1$. That is alright, no serious consequences if the $h_0$ is formulated properly.
  - The higher the ratio of parameters p to number of samples n, the more we expect this overfitting to play a role
  - **Sensitivity** -  the percentage of correctly predicted classes in relation to all members of the class $(sens = \frac{1}{\Sigma true} \Sigma \hat{true})$
  - **Specificity** - percentage of non-defaulters that are correctly identified $(spec = 1 - \frac{\Sigma\hat{true}}{\Sigma true})$
  - The decision to which type of error to follow has to be based on the domain.

|Confusion matrix|        |True |class|       |
|-------------|--------|-----|-----|-------|
|             |        |Neg  |Pos  |*Total*|
|**Predicted**|Negative|TN   |FN   |$\hat{N}$|
|**class**    |Positive|FP   |TP   |$\hat{P}$|
|             |*Total* |N    |P    |Y    |

|Name|Definition|Synonyms|
|---|---|---|
|False pos. rate| $FP/N$|Type 1 error, 1 - Specificity|
|True pos. rate| $TP/P$|1 - Type 2 error, sensitivity, recall, error|
|Pos. pred value| $TP/\hat{P}$|precision|
|Neg. pred value| $TN/\hat{N}$| |

  - Using Bayes classifier we need to choose density function. LDA or QDA can help. The first one has smaller variance, but bigger bias. We should not use it in case of relatively small training set.
  - Naiive Bayes can be used when reducing the variance is important, so p is relatively large or n is small.
</details>



<details>
<summary><h3>Week 3</h3></summary>
  SVM
  
#### Work done
  - Watched the [lecture](https://www.youtube.com/watch?v=_PwhiWxHK8o) aboyt SVM
  - Some useful [videos](https://www.youtube.com/watch?v=efR1C6CvhmE) about SVM
#### Problems faced
  - Generally I need more examples where to use SVM, but I'm good
#### Next steps
  - It's time to complete EDA and beggin with the model.
#### Brief list on notes for this week
  - SVM it used in the cases, where there is wide boundary area between classes, also when it is impossible to set the linear boundary between classes.

</details>



<details>
<summary><h3>Week 4</h3></summary>
  Pointing out the project idea and collecting data (with python). <br>
  The execution time for collecting each individual player performance for 20 seasons (~10000 observations) is approximately 10 minutes.
  
#### Work done
  - [Cool article about EDA](https://towardsdatascience.com/a-gentle-introduction-to-exploratory-data-analysis-f11d843b8184)
  - [Example of an EDA](https://github.com/dformoso/sklearn-classification/blob/master/Data%20Science%20Workbook%20-%20Census%20Income%20Dataset.ipynb)
  - Read some papers on the NYU CMS (partic. about EDA)
  - Watched the lecture
#### Problems faced
  - Had some troubles with collecting of data, but it works fine now.
  - Also I don't think, I could have parse all this data with R, so I'm sorry for using it in this part of the project.
#### Next steps
  - Completing EDA
  - Completing some overdued assignments ;)
#### Brief list on notes for this week
  - Data collecting is pretty interesting.
</details>



<details>
<summary><h3>Week 5</h3></summary>
  EDA is ready!
  
#### Work done
  - Completed EDA
  - [An amazing rticle about feature selecting](https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/)
  - Watched the lecture
#### Problems faced
  - Hard to decide which feature to choose, since I am afraid of overfitting the model
  - R is tough
#### Next steps
  - Completing some more assignments
#### Brief list on notes for this week
  * **Feature Selection**: Select a subset of input features from the dataset
    * **Unsupervised**: Do not use the target variable (e.g. remove redundant variables)
      * Correlation
    * **Supervised**: Use the target variable (e.g. remove irrelevant variables)
      * **Wrapper**: Search for well-performing subsets of features
        * [Recursive Feature Elimination](https://machinelearningmastery.com/rfe-feature-selection-in-python/)
      * **Filter**: Select subsets of features based on their relationship with the target
        * Statistical Methods (i.e. p-value)
        * Feature Importance Methods
      * **Intrinsic**: Algorithms that perform automatic feature selection during training
        * Decision Trees
  * **Dimensionality Reduction**: Project input data into a lower-dimensional feature space (i.e. PCA)

</details>



<details>
<summary><h3>Week 6</h3></summary>
  KNN and deadlines ;(
  
#### Work done
  - [Amazing article about KNN](https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/)
  - Watched the lecture
#### Problems faced
  - R is tough
#### Next steps
  - Completing some more assignments
  - Fitting Model
#### Brief list on notes for this week
  - None
</details>



<details>
<summary><h3>Week 7</h3></summary>
  Working with Dimensionality.
  
#### Work done
  - Watched the lecture.
  - Completed test 1.
#### Problems faced
  - R is tough
  - I faced misunderstanding, when my LOGIT performed way better that I expected. Besides, the type of data I fitted was described in the ISLR as non aplicable for LOGIT. wtf.
#### Next steps
  - HW 1
  - ISLR chptr 6
#### Brief list on notes for this week
  - Not yet
</details>



<details>
<summary><h3>Week 8</h3></summary>
  Model fitting.
  
#### Work done
  - Completed HW1
  - [Article that saved my life (about bias and variance)](https://www.analyticsvidhya.com/blog/2020/12/a-measure-of-bias-and-variance-an-experiment/)
  - I feel like I got way better with using R   B)
  - [Cool code template for future](https://github.com/ranasingh-gkp/Machine-Learning/blob/master/New%20algorithms%20in%20machine%20learning/logistic%20regression/multinomial-logistic-regression.R)
#### Problems faced
  - R is tough
  - Somehow my LOGIT had zero bias -_-
#### Next steps
  - HW2
  - Test 2
  - ISLR chprt 6
#### Brief list on notes for this week
  - OvO, OvR ROC curves for multinomial classifications.
  - model bias = mean(avg(model_trained_on_population(test) - model_trained_on_sample(test)))
  - model variance var(model_trained_on_population(test), model_trained_on_sample(test))
</details>



<details>
<summary><h3>Week 9</h3></summary>
  Cross validation, SVM, and other tools for working with dimensions. Almost done with deadlines.
  
#### Work done
  - Completed HW 2
  - ISLT chptr 6
#### Problems faced
  - R is tough
  - Some unexplainable results in my models.
#### Next steps
  - Last assignment (test 2)
#### Brief list on notes for this week
  - I don't have time, may be later
</details>



<details>
<summary><h3>Week 10</h3></summary>
  Yep. I'm done with the deadlines.
  
#### Work done
  - Completed (last) Test 2
  - ISLT chptr 8
  - Watched lectures for week 9, 10
#### Problems faced
  - R is tough
  - Didn't actually have enough time to fully complete last test, but that is alright...
#### Next steps
  - Read the book and finish leactures.
#### Brief list on notes for this week
  - I'm really tired rn, may be later.
</details>



<details>
<summary><h3>Week 11</h3></summary>
  I need a brief break,
  
#### Work done
  - TBD
#### Problems faced
  - R is tough
  - Keep postponing everything till the last moment
#### Next steps
  - Read the book and finish leactures.
  - Fill the Description part
#### Brief list on notes for this week
  - 
</details>


</details>
:blue_square::blue_square::blue_square::blue_square:<br>
:yellow_square::yellow_square::yellow_square::yellow_square:
