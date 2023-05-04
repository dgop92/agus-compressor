# Agus compressor

## Usage

```
python compresor.py LaBiblia.txt
```

```
python descompresor.py
```

```
python verificador.py LaBiblia.txt
```

### MPI Usage:

```
docker-compose run --rm mympi mpiexec --allow-run-as-root -n 2 python <script-location>
docker-compose run --rm mympi mpiexec --allow-run-as-root -n 2 python /app/tests/test_mpi.py
```
