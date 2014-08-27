def classification_metrics(y_test, y_pred):
'''Prints off useful classification metrics, given a set of true and predicted values

returns: the confusion matrix'''
    cm = confusion_matrix(y_test, y_pred)
    print 'Confusion_Matrix:'
    print 'Accuracy:', m.accuracy_score(y_test, y_pred)
    print 'Sensitivity (True Positive Rate):', cm[0,0]/(cm[0,0] + cm[1,0])
    print 'Specificity (True Negative Rate):', cm[1,1]/(cm[0,1] + cm[1,1])
    return cm
