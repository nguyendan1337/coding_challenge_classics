def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    print(points)
    arrows = 1
    current_end = points[0][1]

    for start, end in points[1:]:
        if start > current_end:
            arrows += 1
            current_end = end


    return arrows

# points = [[1,2],[2,3],[3,4],[4,5]]
# points = [[1,2],[3,4],[5,6],[7,8]]
# points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,5],[4,7],[6,9]]

print(findMinArrowShots(points))