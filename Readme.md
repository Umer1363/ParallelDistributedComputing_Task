# Python Multiprocessing & Multithreading (Friend Version)

This project demonstrates how to run **multiprocessing** and **multithreading** in Python to speed up CPU-bound tasks.  
The core function is in a separate file (`examplecode.py`), and a single script (`multiprocessing_test.py`) runs both approaches and compares execution times.

---

## Project Structure

├── examplecode.py # Core function: eg_test()
├── multiprocessing_test.py # Runs multiprocessing and multithreading
└── README.md # This file

yaml
Copy code

---

## How It Works

- **`examplecode.py`** contains `eg_test()`, a CPU-heavy function that performs mathematical computations.  
- **`multiprocessing_test.py`**:
  - Runs multiple processes in parallel using **multiprocessing** (CPU-bound tasks).  
  - Runs multiple threads in parallel using **multithreading** (I/O-bound or concurrent tasks).  
  - Measures and prints execution time for both approaches.

---

## How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/ParallelDistributedComputing_Task.git
   cd ParallelDistributedComputing_Task
Run the Combined Script

bash
Copy code
python multiprocessing_test.py
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

Using separate files for modular design (examplecode.py)

Author
M. Umer Khan

Python Developer / Enthusiast
