# Custom metrics for evaluating forecast models
def mean_absolute_percentage_error(y_true, y_pred):
    return ((abs(y_true - y_pred) / y_true).mean()) * 100