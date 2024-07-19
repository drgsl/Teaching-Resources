import matplotlib as plt
import arviz as az
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pymc3 as pm

def curve10():
    x_1p = np.vstack([x_1**i for i
    in range(1, order+1)])
    x_1s = (x_1p - x_1p.mean(axis=1, keepdims=True))
    x_1p.std(axis=1, keepdims=True)
    y_1s = (y_1 - y_1.mean()) / y_1.std()
    
    plt.scatter(x_1s[0], y_1s)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
        
    with pm.Model() as model_p:
        alpha = pm.Normal('alpha', mu=0, sd=1)
        beta = pm.Normal('beta', mu=0, sd=10, shape=order)
        gamma = pm.HalfNormal('gamma', 5)
        miu = alpha + pm.math.dot(beta, x_1s)
        y_pred = pm.Normal('y_pred', mu=miu, sd=gamma, observed=y_1s)
        idata_p = pm.sample(2000, return_inferencedata=True)
        
    x_new = np.linspace(x_1s[0].min(), x_1s[0].max(), 100)
    
    alpha_p_post = idata_p.posterior['alpha'].mean(("chain", "draw")).values
    beta_p_post = idata_p.posterior['beta'].mean(("chain", "draw")).values
    idx = np.argsort(x_1s[0])
    y_p_post = alpha_p_post + np.dot(beta_p_post, x_1s)
    plt.plot(x_1s[0][idx], y_p_post[idx], 'C2', label=f'model order {order}')
    
    plt.scatter(x_1s[0], y_1s, c='C0', marker='.')
    plt.legend()

def curve100():
    x_1p = np.vstack([x_1**i for i
    in range(1, order+1)])
    x_1s = (x_1p - x_1p.mean(axis=1, keepdims=True))
    x_1p.std(axis=1, keepdims=True)
    y_1s = (y_1 - y_1.mean()) / y_1.std()
    
    plt.scatter(x_1s[0], y_1s)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
        
    with pm.Model() as model_p:
        alpha = pm.Normal('alpha', mu=0, sd=1)
        beta = pm.Normal('beta', mu=0, sd=100, shape=order)
        gamma = pm.HalfNormal('gamma', 5)
        miu = alpha + pm.math.dot(beta, x_1s)
        y_pred = pm.Normal('y_pred', mu=miu, sd=gamma, observed=y_1s)
        idata_p = pm.sample(2000, return_inferencedata=True)
        
    x_new = np.linspace(x_1s[0].min(), x_1s[0].max(), 100)
    
    alpha_p_post = idata_p.posterior['alpha'].mean(("chain", "draw")).values
    beta_p_post = idata_p.posterior['beta'].mean(("chain", "draw")).values
    idx = np.argsort(x_1s[0])
    y_p_post = alpha_p_post + np.dot(beta_p_post, x_1s)
    plt.plot(x_1s[0][idx], y_p_post[idx], 'C2', label=f'model order {order}')
    
    plt.scatter(x_1s[0], y_1s, c='C0', marker='.')
    plt.legend()

def curve_array():
    x_1p = np.vstack([x_1**i for i
    in range(1, order+1)])
    x_1s = (x_1p - x_1p.mean(axis=1, keepdims=True))
    x_1p.std(axis=1, keepdims=True)
    y_1s = (y_1 - y_1.mean()) / y_1.std()
    
    plt.scatter(x_1s[0], y_1s)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
        
    with pm.Model() as model_p:
        alpha = pm.Normal('alpha', mu=0, sd=1)
        beta = pm.Normal('beta', mu=0, sd=np.array([10, 0.1, 0.1, 0.1, 0.1]), shape=order)
        gamma = pm.HalfNormal('gamma', 5)
        miu = alpha + pm.math.dot(beta, x_1s)
        y_pred = pm.Normal('y_pred', mu=miu, sd=gamma, observed=y_1s)
        idata_p = pm.sample(2000, return_inferencedata=True)
        
    x_new = np.linspace(x_1s[0].min(), x_1s[0].max(), 100)
    
    alpha_p_post = idata_p.posterior['alpha'].mean(("chain", "draw")).values
    beta_p_post = idata_p.posterior['beta'].mean(("chain", "draw")).values
    idx = np.argsort(x_1s[0])
    y_p_post = alpha_p_post + np.dot(beta_p_post, x_1s)
    plt.plot(x_1s[0][idx], y_p_post[idx], 'C2', label=f'model order {order}')
    
    plt.scatter(x_1s[0], y_1s, c='C0', marker='.')
    plt.legend()

if __name__ == '__main__':
    az.style.use('arviz-darkgrid')
    
    data = np.loadtxt('date.csv')
    x_1 = data[:, 0]
    y_1 = data[:, 1]
    order = 5
    
    curve10()
    curve100()
    curve_array()