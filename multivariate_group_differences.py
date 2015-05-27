from scipy.stats import chi2_contingency
import pandas as pd


def chi_squared_contingency(var1, var2):
    '''Verbose run of scipy.stat's chi2_contingency'''
    

    ar_sig_contingency_table = pd.crosstab(var1, var2)


    chi2, p, dof, expected = chi2_contingency(ar_sig_contingency_table)
    if p <= 0.001:
        stars = '***'
    elif p <= 0.01:
        stars = '**'
    elif p <= 0.05:
        stars = '*'
    else:
        stars = ' '
    print 'Pearson\'s Chi-Squared Test\n'
    print "Contingency Table:\n"
    print ar_sig_contingency_table
    print "\n\n"
    print "X-squared = " + str(chi2) + ',  ' + "df =  " + str(dof) + ",  " + "p-value = " + str(p) + stars
    print "Expected frequencies:  \n (based on marginal sums of the table)" + "\n" + str(expected)
