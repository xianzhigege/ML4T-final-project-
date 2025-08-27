The Manul strategy outperforms the benchmark because active trading decision that capitalize on price reversals.
<img width="1000" height="600" alt="Ml BM insample compare" src="https://github.com/user-attachments/assets/2baa5bf1-3864-4014-93ef-9915fb7397f9" />
Out-sample performance(2010-2011)
The Manual Strategy performance degrade due to unseen market condi-tion, highlighting potential overfitting or the statis nature of predefined threshold
<img width="1000" height="600" alt="Ml BM outsample compare" src="https://github.com/user-attachments/assets/ba98aea9-5588-46af-a817-76d0add5741a" />
In-sample
Bench market : Relies on buy and hold steady return during upward trend but suffer during downturns
Manual Stratrgy :
Perform better than the benchmark due to the rule based trades that capture sig-nificant market movement
Strategy Learner:
Outperform both strategies, dynamically adapting to market condition and lev-eraging reinforcement learning to optimize trades.
<img width="1000" height="600" alt="insample compare" src="https://github.com/user-attachments/assets/2232bf86-d68d-4112-a7c3-beaca3d7dc84" />
Out of Sample :
Benchmark Strategy:
Stable performance consistent with the market
Manual Strategy :
A little bit better than Benchmark
Strategy Learner :
Better than the other two but with reduced margins compared to the in-sample results. Because the model trained by in-sample data so it has better perfor-mance. But out-sample need it to use the trained model to predict which will have worse performance.
<img width="1000" height="600" alt="outsample compare" src="https://github.com/user-attachments/assets/f2fcfaa5-0c8c-4b8b-80f0-40fb1c4ba8cf" />
Result and Interpretation
CR vs impact:
CR decrease significantly from 0 to 0.01 but still decrease from 0.01 to 0.02. this confirm that higher transaction cost erode overall portfolio performance
<img width="1000" height="600" alt="cr_impact" src="https://github.com/user-attachments/assets/243489b5-2caa-4a5d-920e-56c179b2e805" />
Sharp Ration (SR) vs Impact:
Like CR, sharp ration also decrease with increase of impact
<img width="1000" height="600" alt="sr_impact" src="https://github.com/user-attachments/assets/7a2deaeb-54df-4ac4-9167-96f231c38ce0" />
Nomalized Portfolio vs Impact:
The chart shows the portfolio growth slows down with increasing im-pact.
<img width="1000" height="600" alt="portval_norm_impact" src="https://github.com/user-attachments/assets/1137c564-3311-4aaf-b4c7-fa9984c46dfe" />

