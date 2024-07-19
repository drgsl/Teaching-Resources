from collections import defaultdict
from pprint import pprint

import numpy as np


class SparseMatrix:
    def __init__(self, p, n, data, rows, cols):
        self.p = p
        self.n = n
        self.matrix = defaultdict(lambda: defaultdict(np.float64))
        for i, entry in enumerate(data):
            current_row = rows[i]
            current_col = cols[i]
            self.matrix[current_row][current_col] = entry

    def __getitem__(self, item):
        return self.matrix[item]

    def __len__(self):
        return self.p

    def shape(self):
        return self.p, self.n

    # def is_symmetric(self):
    #     rows, cols = np.triu_indices(n=self.p, m=self.n)
    #     for i in range(len(rows)):
    #         if self.matrix[rows[i]][cols[i]] != self.matrix[cols[i]][rows[i]]:
    #             return False
    #     return True

    def is_symmetric(self):
        for i in self.matrix.keys():
            for j in self.matrix[i].keys():
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def __str__(self):
        for i in range(self.p):
            elements = []
            for j in range(self.n):
                elements.append(self.matrix[i][j])
            print(elements)
        return ""


def read_sparse_matrix(filename):
    # file of type: n on first line, second line: x, i, j, where x = A[i][j]
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        data, rows, cols = [], [], []
        for line in f:
            parts = [li.strip() for li in line.split(",") if len(li) != 0 and li != '\n']
            if not len(parts):
                continue
            x = float(parts[0].strip())
            i = int(parts[1].strip())
            j = int(parts[2].strip())
            data.append(x)
            rows.append(i)
            cols.append(j)
    return n, data, rows, cols

def generate_symmetric_sparse_matrix(p, n):
    rows, cols = np.triu_indices(n=p, m=n)
    approx_size_upper_triangle = int((n*p)/2)
    data = [np.random.randint(1, 100) for _ in range(approx_size_upper_triangle) if np.random.random() > 0.5]

    while len(rows) != len(data) or len(cols) != len(data):
        pos_to_remove = np.random.randint(0, len(rows))
        rows = np.delete(rows, pos_to_remove)
        cols = np.delete(cols, pos_to_remove)

    rows, cols = np.concatenate((rows, cols)), np.concatenate((cols, rows))
    data = np.concatenate((data, data))

    return data, rows, cols

def power_iteration_method(data, epsilon=1e-6, max_iterations=1000):
    # Initialize x_0 and y_0
    x = np.random.rand(len(data))
    y = np.zeros(len(data))
    # Normalize x_0
    x /= np.linalg.norm(x)
    # Initialize Rayleigh quotient and iteration counter
    rq = 0
    i = 0
    while i < max_iterations:
        # Compute Ay_i
        y = np.dot(data, x)
        # Compute the Rayleigh quotient
        rq_new = np.dot(y, x) / np.dot(x, x)
        # Check convergence
        if np.linalg.norm(rq_new - rq) < epsilon:
            break
        # Normalize y_i
        y /= np.linalg.norm(y)
        # Update x_i and Rayleigh quotient
        x = y.copy()
        rq = rq_new
        # Increment iteration counter
        i += 1
    # Return largest eigenvalue and associated eigenvector
    return rq, x

def power_iteration_method_matrix(A, epsilon=1e-6, max_iterations=1000):
    # Initialize x_0 and y_0
    x = np.random.rand(A.shape[1])
    y = np.zeros(A.shape[0])
    # Normalize x_0
    x /= np.linalg.norm(x)
    # Initialize Rayleigh quotient and iteration counter
    rq = 0
    i = 0
    while i < max_iterations:
        # Compute Ay_i
        y = np.dot(A, x)
        # Compute the Rayleigh quotient
        rq_new = np.dot(y, x) / np.dot(x, x)
        # Check convergence
        if np.linalg.norm(rq_new - rq) < epsilon:
            break
        # Normalize y_i
        y /= np.linalg.norm(y)
        # Update x_i and Rayleigh quotient
        x = y.copy()
        rq = rq_new
        # Increment iteration counter
        i += 1
    # Return largest eigenvalue and associated eigenvector
    return rq, x


def print_second_point(A, b):
    # Compute the Singular Value Decomposition of A
    U, S, VT = np.linalg.svd(A)

    # Print the singular values of A
    print("Singular values of A:", S)

    # Compute the rank of A
    rank = np.linalg.matrix_rank(A)
    print("Rank of A:", rank)

    # Compute the condition number of A
    cond_num = np.linalg.cond(A)
    print("Condition number of A:", cond_num)

    # Compute the Moore-Penrose pseudoinverse of A
    A_inv = np.linalg.pinv(A)
    print("Pseudoinverse of A:\n", A_inv)

    # Compute the solution x^i of the system Ax = b
    x_i = np.dot(A_inv, b)
    print("Solution x^i:", x_i)

    # Compute the norm ||b - Ax||
    norm_resid = np.linalg.norm(b - A.dot(x_i))
    print("Norm of the residual:", norm_resid)

    # Compute the pseudo-inverse in the sense of least squares
    A_j = np.linalg.inv(A.T.dot(A)).dot(A.T)
    print("Least-squares pseudoinverse of A:\n", A_j)

    # Compute the norm ||A^i - A^j||
    norm_diff = np.linalg.norm(A_inv - A_j)
    print("Norm of the difference:", norm_diff)


if __name__ == "__main__":
    # Read the matrixes from files
    matrixes = []
    for i in ["512", "1024", "2023"]:
        n, data, rows, cols = read_sparse_matrix("m_rar_sim_2023_{}.txt".format(i))
        matrix = SparseMatrix(n, n, data, rows, cols)
        matrix_normal = np.zeros((n, n))
        for i_1 in range(n):
            for j_1 in range(n):
                matrix_normal[i_1][j_1] = matrix[i_1][j_1]

        # checking if matrix is symmetric
        if matrix.is_symmetric():

            print(f'Matrix m_rar_sim_2023_{i} is symmetric: ')
        else:
            print(f'Matrix m_rar_sim_2023_{i} is not symmetric')

        eigenvalue, x = power_iteration_method(data)
        print(f'For Matrix m_rar_sim_2023_{i}: eigen = {eigenvalue} \nx = {x}\nNorm: {np.linalg.norm(data - eigenvalue)}\n\n')

        matrixes.append(matrix)
        eigenvalue_matrix, x_matrix = power_iteration_method_matrix(matrix_normal)
        print_second_point(matrix_normal, eigenvalue_matrix)
    # Generate the matrix
    p, n = 5, 5
    data, rows, cols = generate_symmetric_sparse_matrix(p, n)

    generated_matrix = SparseMatrix(p, n, data, rows, cols)
    generated_matrix_normal = np.zeros((n, n))

    for i_1 in range(n):
        for j_1 in range(n):
            generated_matrix_normal[i_1][j_1] = generated_matrix[i_1][j_1]

    if np.linalg.det(generated_matrix_normal) == 0:
        print("Singular matrix, recalculating matrix")

    while np.linalg.det(generated_matrix_normal) == 0:
        data, rows, cols = generate_symmetric_sparse_matrix(p, n)
        generated_matrix = SparseMatrix(p, n, data, rows, cols)
        generated_matrix_normal = np.zeros((n, n))
        for i_1 in range(n):
            for j_1 in range(n):
                generated_matrix_normal[i_1][j_1] = generated_matrix[i_1][j_1]

    if generated_matrix.is_symmetric():
        print(f'Generated matrix is symmetric')
    else:
        print(f'Generated matrix is not symmetric')
    eigenvalue, x = power_iteration_method(data)
    eigenvalue_matrix, x_matrix = power_iteration_method_matrix(generated_matrix_normal)
    print(f'For generated matrix: eigen = {eigenvalue} \nx = {x}\nNorm: {np.linalg.norm(data - eigenvalue)}\n\n')
    print_second_point(generated_matrix_normal, eigenvalue_matrix)



