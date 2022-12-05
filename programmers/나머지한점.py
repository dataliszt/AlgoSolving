def solution(v):
    x_dict, y_dict = {}, {}
    
    for (x, y) in v:
        if x_dict.get(x):
            x_dict[x] += 1
        else:
            x_dict[x] = 1
        
        if y_dict.get(y):
            y_dict[y] += 1
        else:
            y_dict[y] = 1

    rest_x = list({key: val for key, val in x_dict.items() if val != 2}.keys())[0]
    rest_y = list({key: val for key, val in y_dict.items() if val != 2}.keys())[0]
    
    return [rest_x, rest_y]
        