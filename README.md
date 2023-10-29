# hack2023
Verizon 5G challenge - Hackathon 2023

This project connects cars to a Mobile Edge Computing (MEC) system using a 5G network. Here, the 5G network is a simplified representation that connects cars using an IP address (here, a one digit unique id). Cars can broadcast sensor data to the MEC, which is then aggregated into a visual representation of the roadway. The MEC can then sort the relevant data and message individual cars with relevant information about the roadway ahead and behind.

Example commands:
- all vehicles in system: py main.py environment/environment1/environment
- some vehicles in system: py main.py environment/environment2/environment