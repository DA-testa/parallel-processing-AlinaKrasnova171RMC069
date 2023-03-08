# python3

def parallel_processing(n, m, data):
    
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    line = []
    output = []

    for i in range(n):
        line.append([i,0])

    for j in range(m):
        lineX = min(line, key = lambda x: x[1])
        output.append((lineX[0],lineX[1]))
        lineX[1] += data[j]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]

    result = parallel_processing(n,m,data)

    for i, t in result:
        print(i,t)
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    
    # TODO: create the function
    
    # TODO: print out the results, each pair in it's own line


if __name__ == "__main__":
    main()
