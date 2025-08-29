# Proof-of-Work (PoW) Simulator

This Python script provides a simple, clear demonstration of the Proof-of-Work (PoW) algorithm, which is the foundation of security for many major cryptocurrencies like Bitcoin.

## What is Proof-of-Work?

Proof-of-Work is a computational "puzzle" that network participants (miners) must solve to add a new block of transactions to the blockchain. The puzzle involves finding a number (a "nonce") that, when combined with the block's data and hashed, produces a result that meets a certain criteria (e.g., a hash starting with a specific number of leading zeros).

This process is difficult and time-consuming, which prevents malicious actors from easily altering the blockchain.

## How This Script Works

1.  **Sets a Difficulty:** A `DIFFICULTY` constant defines how many leading zeros the target hash must have.
2.  **Starts Mining:** The script enters a loop, trying different `nonce` values starting from 0.
3.  **Hashes and Checks:** In each loop, it combines the block data with the current `nonce` and calculates the SHA-256 hash.
4.  **Finds a Solution:** The loop continues until it finds a hash that meets the difficulty requirement.
5.  **Reports Results:** It then prints the successful `nonce`, the valid `hash`, and the total time it took to find the solution.

### Experiment with Difficulty

Try changing the `DIFFICULTY` variable at the top of the `pow_simulator.py` script.
- A `DIFFICULTY` of `4` should be found relatively quickly.
- Increasing it to `5` will take significantly longer.
- Increasing it to `6` might take several minutes, clearly demonstrating the exponential increase in work required.

## How to Run
```bash
python3 pow_simulator.py
