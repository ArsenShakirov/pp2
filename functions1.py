def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2  # Number of rabbits
    x = numheads - y  # Number of chickens
    
    return x, y

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)

print(f"Chicks: {chickens}, Rabbits: {rabbits}")
