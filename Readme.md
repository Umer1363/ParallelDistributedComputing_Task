# Python Multiprocessing & Multithreading (Friend Version)

This project demonstrates how to run **multiprocessing** and **multithreading** in Python to speed up CPU-bound tasks.  
The core function is in a separate file (`sandwich_friend.py`), and a single script (`parallel_sandwich_friend.py`) runs both approaches and compares execution times.

---

## Project Structure

├── sandwich_friend.py # Core function: make_sandwich()
├── parallel_sandwich_friend.py # Runs multiprocessing and multithreading
└── README.md # This file

yaml
Copy code

---

## How It Works

- **`sandwich_friend.py`** contains `make_sandwich()`, a CPU-heavy function that performs mathematical computations.  
- **`parallel_sandwich_friend.py`**:
  - Runs multiple processes in parallel using **multiprocessing** (CPU-bound tasks).  
  - Runs multiple threads in parallel using **multithreading** (I/O-bound or concurrent tasks).  
  - Measures and prints execution time for both approaches.

---

## How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/parallel-sandwich-friend.git
   cd parallel-sandwich-friend
Run the Combined Script

bash
Copy code
python parallel_sandwich_friend.py
This will first execute the multiprocessing version, then the multithreading version, displaying the execution times for each.

Requirements
Python 3.8+

No external libraries required

Key Concepts Demonstrated
multiprocessing.Process and join()

threading.Thread and join()

CPU-bound vs I/O-bound tasks

Measuring execution time with the time module

Safe multiprocessing with if __name__ == "__main__":

Using separate files for modular design (sandwich_friend.py)

Author
M. Umer Khan
Python Developer / Enthusiast