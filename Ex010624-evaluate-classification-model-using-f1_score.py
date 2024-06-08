#Cau hoi tu luan

#Function evaluates classification model using F1-score
def evaluate_classification_model (tp, fp, fn):
    if type(tp) != int:
        print ('tp must be int')
        return
    if type(fp) != int:
        print ('fp must be int')
        return
    if type(fn) != int:
        print ('fn must be int')
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print ('tp and fp and fn must be greater than 0')
        return
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision + recall)

    print('precision is', precision)
    print('recall is', recall)
    print('f1_score is', f1_score)

#exemple
evaluate_classification_model (-2, 2, 3)
evaluate_classification_model (50, 60, 20)
evaluate_classification_model (1, 3, 'a')
evaluate_classification_model ('a', 'b', 1)



