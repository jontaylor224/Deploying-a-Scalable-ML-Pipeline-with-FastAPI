import pytest
# add necessary import
from sklearn.ensemble import RandomForestClassifier
from ml.data import apply_label
from ml.model import train_model, compute_model_metrics


# implement the first test. Change the function name and input as needed
def test_apply_label():
    """
    Test that apply_label returns the correct salary label
    """
    # Your code here
    assert apply_label([1]) == '>50K'
    assert apply_label([0]) == '<=50K'


# implement the second test. Change the function name and input as needed
def test_train_model():
    """
    Test that train_model returns a RandomForest Classifier.
    """
    # Your code here
    X_train = [[0, 1], [1, 0], [1, 1], [0, 0]]
    y_train = [0, 1, 1, 0]

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test that compute_model_metrics returns expected values
    """
    # Your code here
    y = [0, 1, 1, 0]
    preds = [0, 1, 0, 0]

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(0.5)
    assert fbeta == pytest.approx(0.6666667)
