def solution(max_weight, specs, names):
    
    weight_stack = 0
    truck = 0
    
    # spec 탐색 시간을 O(1)로 만들기 위해 
    # dictionary 자료형에 spec 저장 
    spec_dict = {}
    for (name, weight) in specs:
        spec_dict[name] = weight
    
    for name in names:
        if weight_stack + int(spec_dict[name]) > max_weight:
            truck += 1
            weight_stack = int(spec_dict[name])
        else:
            weight_stack += int(spec_dict[name])

    return truck + 1