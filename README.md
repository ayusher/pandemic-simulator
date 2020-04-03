# pandemic_simulator
A python script to simulate pandemic spread


# What is implemented?
* Once a Person object is created, it represents a sick patient
  * Assigned a healed-by date, death date (if unlucky)
* People can get tested
  * If tested, they stay isolated for the rest of their sickness and are assumed to not spread the disease anymore
  
  # What can be implemented?
  * Social distancing can be represented by a reduced branch factor
  
  # Variables to change
  * total_pop: the total population present
  * death_rate: the rate in range [0, 1] that dies as a result of the disease
  * asym_rate: the rate in range [0, 1] that has no symptoms of the disease, but carries it
  * tests_per_day: the number of tests that are run to determine sickness per day (function with input as day number)
  * test_pos_rate: the rate in range [0, 1] that tests positive for the disease (ex. only 5% of coronavirus test results are positive)
  * incubation_time: the average number of days a person is infectious
  * inc_unc_m: the uncertainty below the incubation time
  * inc_unc_m the uncertainty above the incubation time
  * branch_factor: the average number of people that a sick person infects
  * tot_dead: the number of people dead at the beginning of the simulation as a result of the pandemic
  * t_pos: the number of people in the starting population that have been tested positive
  * day: the starting day
  * start_num: the number of people sick on the starting day
  
  
