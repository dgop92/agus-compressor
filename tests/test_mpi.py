from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    print("Hello from rank 0")
else:
    print("Hello from rank %d" % rank)
