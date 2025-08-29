import hashlib
import time

# The difficulty of the puzzle.
# The number of leading zeros the final hash must have.
# Try increasing this number from 4 to 5 and see how much longer it takes!
DIFFICULTY = 4

def proof_of_work(block_data):
    """
    Simulates the Proof-of-Work mining process.
    
    Args:
        block_data (str): The data to be included in the block.

    Returns:
        tuple: A tuple containing the valid hash and the nonce that produced it.
    """
    nonce = 0
    print(f"Starting mining for block with data: '{block_data}'")
    print(f"Difficulty: Find a hash starting with {DIFFICULTY} zeros.\n")
    
    start_time = time.time()
    
    while True:
        # Combine the block data with the current nonce value
        text_to_hash = block_data + str(nonce)
        
        # Calculate the SHA-256 hash of the combined string
        current_hash = hashlib.sha256(text_to_hash.encode()).hexdigest()
        
        # Check if the hash meets the difficulty requirement
        if current_hash.startswith('0' * DIFFICULTY):
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            print("--- Block Mined Successfully! ---")
            print(f"Nonce found: {nonce}")
            print(f"Valid Hash:  {current_hash}")
            print(f"Time taken:  {elapsed_time:.4f} seconds")
            
            return current_hash, nonce
        
        # If not, increment the nonce and try again
        nonce += 1

if __name__ == "__main__":
    # Some sample transaction data for our block
    sample_block_data = "Transaction from Alice to Bob for 10 BTC"
    proof_of_work(sample_block_data)
