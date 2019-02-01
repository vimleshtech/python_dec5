import numpy as np 
import matplotlib.pyplot as plt 
  
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x)  #count
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x - n*m_y*m_x) 
    SS_xx = np.sum(x*x - n*m_x*m_x) 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b):
# plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o") 
    
    # predicted response vector 
    
  
    # plotting the regression line 
    plt.plot(x_newData, y_pred, color = "g")
    plt.plot(x,y,'.')
  
    # putting labels 
    plt.xlabel('x-label') 
    plt.ylabel('y-label') 
  
    # function to show plot 
    plt.show() 
  

# observations 
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
x_newData=np.array([10,11,12,17])
 
# estimating coefficients 
b = estimate_coef(x, y) 
print("Estimated coefficients:\nb_0 = {} \n b_1 = {}".format(b[0], b[1])) 
y_pred = b[0] + b[1]*x_newData 
# plotting regression line
plot_regression_line(x, y, b)
plot_regression_line(x_newData, y_pred, b) 
  

