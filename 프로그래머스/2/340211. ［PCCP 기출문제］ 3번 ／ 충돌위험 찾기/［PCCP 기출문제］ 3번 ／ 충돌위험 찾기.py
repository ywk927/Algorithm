def solution(points, routes):
    individual_routes = [[] for _ in range(len(routes))]
    answer = 0
    max_route = 0
    # print(individual_routes)
    for i in range(len(routes)):
        f = len(routes[i])
        k = 0
        individual_routes[i].append((points[routes[i][0] - 1][0], points[routes[i][0] - 1][1]))
        while k < f-1:
            start_robot = routes[i][k] - 1 # 인덱스 관리용
            end_robot = routes[i][k+1] - 1
            start_i = points[start_robot][0]
            start_j = points[start_robot][1]
            end_i = points[end_robot][0]
            end_j = points[end_robot][1]
            # individual_routes[i].append((start_i,start_j))
            # print(start_i, start_j, end_i, end_j)
            if start_i != end_i:
                if start_i > end_i:
                    while start_i != end_i:
                        individual_routes[i].append((start_i -1, start_j))
                        start_i -= 1
                elif start_i < end_i:
                    while start_i != end_i:
                        individual_routes[i].append((start_i +1, start_j))
                        start_i += 1
            if start_j != end_j:
                if start_j > end_j:
                    while start_j != end_j:
                        individual_routes[i].append((start_i, start_j-1))
                        start_j -= 1
                elif start_j < end_j:
                    while start_j != end_j:
                        individual_routes[i].append((start_i, start_j+1))
                        start_j += 1
            k += 1
        # print(individual_routes[i])
        if len(individual_routes[i]) > max_route:
            max_route = len(individual_routes[i])
    for i in range(len(individual_routes)):
        for _ in range(max_route - len(individual_routes[i])):
            individual_routes[i].append((0,0))
    # print(individual_routes)
    # print(max_route)
    for j in range(max_route):
        new_cnt = set()
        counted = set()
        for i in range(len(individual_routes)):
            if individual_routes[i][j] not in new_cnt:
                new_cnt.add(individual_routes[i][j])
            elif individual_routes[i][j] not in counted and individual_routes[i][j] in new_cnt and individual_routes[i][j] != (0,0):
                answer += 1
                counted.add((individual_routes[i][j]))
    return answer