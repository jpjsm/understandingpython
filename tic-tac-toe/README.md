# Tic Tac Toe 
## A tale about trying to train a machine to play Tic Tac Toe through Reinforcement Learning

To run the Jupyter notebooks in Binder press:  [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/fcarsten/tic-tac-toe/master)

The goal of this series is to implement and test a couple of different approaches to 
training a computer how to play **Tic Tac Toe**. We will create:

* A player that plays completely randomly, 
* Two players that implement simple forms of the Min-Max algorithm, 
* Several players that we will train through Reinforcement Learning:
    * a Tabular Q-Learning player.
    * a Simple Neural Network Q-Learning player.
    * a Deep Neural Network Q-learning player.
    * a Policy Gradient Descent based player.

I assume you are familiar with:
* The rules and basic strategy of playing Tic Tac Toe.
* Basic Python 3 programming and use of a Python IDE or Jupyter Notebooks.
* At least rudimentary knowledge of Tensorflow and Neural Networks would be helpful, but you might be able to do 
without (give it a try and if it's too overwhelming do some of the beginner tutorials, 
and then try again).

## Developer

### Setup

```
conda create -n tic-tac-toe python=3.12
conda activate tic-tac-toe
pip install ipython==8.24.0 matplotlib=3.8.4 numpy==1.26.4 tensorboard==2.16.2 tensorflow==2.16.1 jupyterlab==4.1.8 notebook==7.1.3
```

### Verify correct environment

In an activated environment:

- Windows: powershell prompt
  - if you happen to have configured your `conda` environment for powershell; if you have not and would like to enable `conda` for PowerShell see: [Step-by-Step Guide to Activating Conda Environment from PowerShell](https://saturncloud.io/blog/activating-conda-environment-from-powershell-a-guide-for-data-scientists/)
  - `conda activate tic-tac-toe`
  - `conda env export | select-string '(8.24.0|3.8.4|1.26.4|2.16.(1|2)|4.1.8|7.1.3)'`
    > ipython==8.24.0 <br/>
      jupyterlab==4.1.8 <br/>
      matplotlib==3.8.4 <br/>
      notebook==7.1.3 <br/>
      numpy==1.26.4 <br/>
      tensorboard==2.16.2 <br/>
      tensorflow==2.16.1 <br/>
      tensorflow-intel==2.16.1 <br/>

- Windows: command prompt
  - Manually verify the contents of `conda env export` output.

- Linux:
  - `conda env export | grep -E '(8.24.0|3.8.4|1.26.4|2.16.(1|2)|4.1.8|7.1.3)'`
    > ipython==8.24.0 <br/>
      jupyterlab==4.1.8 <br/>
      matplotlib==3.8.4 <br/>
      notebook==7.1.3 <br/>
      numpy==1.26.4 <br/>
      tensorboard==2.16.2 <br/>
      tensorflow==2.16.1 <br/>
      tensorflow-intel==2.16.1 <br/>
