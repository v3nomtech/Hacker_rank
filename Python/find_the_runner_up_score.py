def runner(array_students):
    array_students = list(array_students)
    array_students.sort(reverse=True)
    for score in range(len(array_students) - 1):
        if array_students[score] != array_students[score + 1]:
            runner_up = array_students[score + 1]
            break
    return runner_up


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = runner(arr)
    print(result)
