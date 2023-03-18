ranked = [100, 90, 90, 80, 80, 40]
ranked = sorted(list(set(ranked)), key=lambda x: -x)
    
print(ranked)
