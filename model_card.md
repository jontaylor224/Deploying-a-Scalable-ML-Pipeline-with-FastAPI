# Model Card

For additional information, see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This is a binary classification model designed to predict whether an individual's annual income exceeds or falls below $50,000. The model uses a Random Forest Classifier with 100 decision trees and a fixed random state of 42 to provide reproducible results. The model is implemented using Python and scikit-learn.

The model uses both continuous and categorical features from the Census Income dataset. Categorical features are transformed using one-hot encoding, and the filtered encoder is saved with the trained model so that the same feature transformation can be applied during inference.

## Intended Use

The intended use of this model is educational and experimental. It demonstrates a machine learning pipeline that loads and processes tabular data, trains a classification model, evaluates model performance, and provides predictions through a reusable model and preprocessing pipeline.

The model is not intended to be used as the sole basis for making decisions about an individual's employment, income, credit, housing, insurance, or other consequential circumstances. Predictions should not be interpreted as verified information about an individual's actual income. 

## Training Data

The model was trained using the Census Income dataset that was provided with the project. This data is based on the [UC Irvine Machine Learning Repository Census Income dataset](https://archive.ics.uci.edu/dataset/20/census+income). The dataset contains 32561 records and 15 columns, including the `salary` target variable.

The target variable contains two classes: `<= 50K` and `> 50K`. The dataset contains six numerical features and eight categorical predictor features. The categorical features used by the model are `workclass`, `education`, `marital status`, `occupation`, `relationship`, `race`, `sex`, and `native-country`.

The data was divided into training and test sets using an 80/20 split. The split used a fixed random state and stratification by the `salary` variable to maintain the relative distribution of the target classes between the training and test datasets.

The categorical features were transformed using a `OneHotEncoder` with `handle_unknown="ignore"`. The encoder was fitted using the training data and then reused to transform the test data.

## Evaluation Data

The model was evaluated on the test portion of the Census Income dataset  held out during training.  The test set contains approximately 20 percent of the original dataset. 

In addition to evaluating overall model performance, the model was evaluated separately across every unique value of each categorical feature. This slice-based evaluation was used to identify differences in model performance between groups represented in the test data.

Some categorical slices contain very few observations. Consequently, metrics for those slices may not provide reliable performance estimates and should be interpreted in the context of the number of observations in each slice.

## Metrics

The model was evaluated using precision, recall, and F1 score. These metrics were calculated for the positive class, which represents individuals with an annual income greater than $50,000. 

On the test data, the model achieved the following results:
 - Precision: 0.7353
 - Recall: 0.6378
 - F1 score: 0.6831

Precision measures the proportion of individuals predicted to have an income greater than $50K who actually belong in the `>50K` class. Recall measures the proportion of actual `>50K` individuals that the model correctly identifies. The F1 score is the harmonic mean of precision and recall, providing a combined measure of these two aspects of classification performance. 

Performance varied across categorial slices:
 - The `HS-grad` slice contained 2120 observations and had an F1 score of 0.4861.
 - The `Bachelors` slice contained 1096 observations and had an F1 score of 0.7618.
 - The `Other-service` slice contained 684 observations and had an F1 score of 0.2667.
 - The `Prof-speciality` slice contained 818 observations and had an F1 score of 0.7989.
 - The `Own-child` slice contained 1032 observations and had an F1 score of 0.2857.

These slice-level results demonstrate that overall performance does not reflect equal performance across all categorical groups in the evaluation data. 

## Ethical Considerations

The dataset contains attributes such as race, sex, marital status, relationship, and native country.  These attributes describe individuals represented in the historical dataset and can be associated with differences in model performance across slices. 

The evaluation demonstrated that model performance varies across categorical groups. In particular, differences in recall and F1 score were observed among several groups. These differences should be considered before using a model of this type for applications that could affect individuals. 

The model learns statistical patterns from historical data and therefore may reproduce patterns or relationships present in that data. A prediction from this model should not be interpreted as an objective assessment of an individual's income or personal characteristics.

## Caveats and Recommendations

This model's performance is dependent on the dataset used for training and evaluation. The evaluation results should not be assumed to represent performance on populations or data collected under different conditions. 

Some categorical data slices in the test data contain very few observations. Metrics calculated from these groups can vary substantially and should not be interpreted as reliable estimates of general performance for those groups.

The model should therefore be evaluated on representative and sufficiently large datasets before being considered for any practical application. Additional monitoring should include overall precision, recall, and F1 score, as well as performance across relevant categorical slices. 

Because this model was developed as part of an educational machine learning project, its predictions should not be used as the sole basis for consequential decisions about individuals. 