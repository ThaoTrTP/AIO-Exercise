#Viet function lua chon regression loss function
def regression_loss (num_samples, loss_name):
    import numpy as np
    if type(num_samples) != int:
        print ('num_samples must be an integer')
        return
    total_loss = 0
    for i in range (num_samples):
        predict = np.random.uniform(0, 10)
        target = np.random.uniform(0, 10)
        if loss_name == 'mae':
            loss = abs(predict - target)
        if loss_name == 'mse':
            loss = (predict - target)**2
        total_loss = total_loss + loss
        print (f'sample {i}, predict: {predict}, target: {target}')
        print (f'loss: {loss}')
        print (f'total_loss: {total_loss}')
        print(' ')
    final_result = total_loss/num_samples
    print (f'loss_{loss_name}: {final_result}')
              

regression_loss(3, 'mse')
regression_loss(3.8, 'mse')


    
    