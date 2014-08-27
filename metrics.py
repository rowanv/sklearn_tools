from scipy.stats import beta
from scipy.stats import binom_test
import sklearn.metrics as m
 
def binom_interval(success, total, confint=0.95):
    '''
    from paulgb's binom_interval.py'''
    quantile = (1 - confint) / 2.
    lower = beta.ppf(quantile, success, total - success + 1)
    upper = beta.ppf(1 - quantile, success + 1, total - success)
    return (lower, upper)
    
def classification_metrics(y_test, y_pred):
    cm = m.confusion_matrix(y_test, y_pred)
    #95% confidence interval
    #No-information rate
    #P-value [acc > NIR]
    print 'Confusion_Matrix:'
    print cm
    print '\n'
    print 'Overall Statistics:'
    print 'Accuracy Confidence Interval:', binom_interval(sum(diag(cm)),sum(cm))
    print 'Accuracy P Value:', binom_test(sum(diag(cm)), n = sum(cm) )
    print 'Accuracy:', m.accuracy_score(y_test, y_pred)
    print 'Sensitivity (True Positive Rate):', cm[0,0]/(cm[0,0] + cm[1,0])
    print 'Specificity (True Negative Rate):', cm[1,1]/(cm[0,1] + cm[1,1])
