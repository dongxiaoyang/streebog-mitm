#3 Nonlinearly Constrained Neutral Words Meet Guess-and-Determine Improved MITM Cryptanalysis on Streebog
==
* `MITMPRE_Stribog_v12_key_MCAK_guess_keyandstate_halfround_indicator_KMAC_start_W3.py`: Source code for 8.5-round preimage attack on Streebog-512 compression function, it takes about several days to find the solution in Figure 5. But we are not sure whether it is the optimal solution, because the MILP model is so large so that it will take too much time to get the optimal solutions, we run it about one month and we still can not get the optimal solutions.

* `MITMPRE_Stribog_v13_256_key_MCAK_guess_keyandstate_halfround_indicator_KMAC_start_W3.py`: Source code for 7.5-round preimage attack on Streebog-256 compression function, it takes about several days to find the solution in Figure 6. But we are not sure whether it is the optimal solution, because the MILP model is so large so that it will take too much time to get the optimal solutions, we run it about one month and we still can not get the optimal solutions.

* `MITMPRE_Stribog_v10_256_guess_graykey_6half.py`: Source code for 6.5-round preimage attack on Streebog-256 compression function, it takes about several hours to find the solution in Figure 10.

* `stribog512_7half.pdf`: A new solution of 7.5-round preimage attack on Streebog-512 compression function: \lambda^+=64, \lambda^-=16, m=24, l^+=40, l^-=0, so DoF^+=24, DoF^-=16, \sigma^+=0, \sigma^-=15. Because the neutral words are linearly constrained in the attack, we just use Algorithm 1 to mount the MITM attack. The time complexity is about 2^440 by Equation (3).
