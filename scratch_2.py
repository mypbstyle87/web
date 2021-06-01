def solution(array):
    # 제한사항 체크 (위반시 -2 리턴)
    if len(arr) > 100:
        print("배열의 길이는 100 이하의 자연수 입니다.")
        return -2
    for num in arr:
        if num > 100 or num <= 0 or type(num) != int:
        print("배열의 원소는 1이상 100 이하 자연수 입니다.")
        return -2

    # 리스트 정렬
    array.sort()
    # print(array)

    # 중복 제거
    temp = list()
    for i in array:
        if i not in temp:
        temp.append(i)
    # print(temp)

    # 중복 제거된 원소로 array에서 갯수 카운트
    sol = dict()
    for j in temp:
        if array.count(j) > 1:
        sol[j] = array.count(j)
    # print(sol)

    # 중복해서 나타나는 숫자가 없으면 -1 반환
    if len(sol) == 0:
        return -1

    # 중복되는 갯수만 최종 리스트에 추가하여 리턴
    solve = list()
    for k in sol:
        solve.append(sol[k])
    return solve

arr = [1, 2, 3, 3, 3, 3, 4, 4]
print(solution(arr))

arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
print(solution(arr))

arr = [3, 5, 7, 9, 1]
print(solution(arr))

arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(arr))

arr = [1, 2, 3, 3, 4, 101]
print(solution(arr))
