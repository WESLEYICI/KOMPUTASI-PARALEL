# mimd_example.py
# MIMD - Multiple Instruction Multiple Data

from multiprocessing import Process

# Different algorithms (different instructions)

def run_algorithm_A(data):
    print("Process 1 - Algorithm A")
    print("Result:", data * 2)

def run_algorithm_B(data):
    print("Process 2 - Algorithm B")
    print("Result:", data + 10)

def run_algorithm_C(data):
    print("Process 3 - Algorithm C")
    print("Result:", data ** 2)

def run_algorithm_D(data):
    print("Process 4 - Algorithm D")
    print("Result:", data - 5)


if __name__ == "__main__":

    # Different data
    data_A = 5
    data_B = 10
    data_C = 3
    data_D = 20

    # Create processes (run in parallel)
    p1 = Process(target=run_algorithm_A, args=(data_A,))
    p2 = Process(target=run_algorithm_B, args=(data_B,))
    p3 = Process(target=run_algorithm_C, args=(data_C,))
    p4 = Process(target=run_algorithm_D, args=(data_D,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("All processes finished.")