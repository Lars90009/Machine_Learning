class error_analysis(object):
       def precision(true_positives,no_pred_positives):
              true_positives = true_positives
              no_pred_positives = no_pred_positives
              precision = sum(true_positives)/sum(no_pred_positives)
              return precision

       def recall(true_positives,no_actual_positives):
              true_positives = true_positives
              no_actual_positives = no_actual_positives
              recall = sum(true_positives)/sum(no_actual_positives)
              return recall
       
       def f_score(precision,recall):
              numerator = 2*precision*recall
              denominator = precision + recall
              F_score = numerator/denominator
              return F_score

true_positives       = [200]
no_pred_positives    = [890]
no_actual_positives  = [210]

precision = error_analysis.precision(true_positives,no_pred_positives)
recall = error_analysis.recall(true_positives,no_actual_positives)
print(precision,recall)
f_score = error_analysis.f_score(precision,recall)
print(f_score)
