def build_bridge(chunk, goal):
    junction = chunk / 2

    result = False

    if chunk == goal:
        result = True

    else:
        combination = chunk

        while combination <= goal:
            combination = combination + junction + chunk

            if combination == goal:
                result = True

    return result



print(build_bridge(2, 20))
print(build_bridge(2, 18))