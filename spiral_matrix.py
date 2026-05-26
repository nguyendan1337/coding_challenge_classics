class Solution:
    #my ugly messy one that works
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        directions = [ (0,1), (1,0), (0,-1), (-1,0) ]
        seen = set()


        y, x = 0, 0
        # print(f"({y},{x})")
        result = []
        result.append(matrix[y][x])
        seen.add((y,x))

        i = 0
        dy, dx = directions[i]
        ny = y+dy
        nx = x+dx

        if nx >= width:
            i = (i + 1) % 4
            dy, dx = directions[i]
            ny = y+dy
            nx = x+dx

        while ny >= 0 and ny < height and nx >= 0 and nx < width and (ny,nx) not in seen:
            y = ny
            x = nx
            # print(f"({y},{x})")
            result.append(matrix[y][x])
            seen.add((y,x))
            ny = y+dy
            nx = x+dx

            if ny < 0 or ny >= height or nx < 0 or nx >= width or (ny,nx) in seen:
                i = (i + 1) % 4
                dy, dx = directions[i]
                ny = y+dy
                nx = x+dx
                # print(f"direction: ({dy},{dx})")

        return result

    def chatGPT(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # left -> right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # top -> bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # right -> left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # bottom -> top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result