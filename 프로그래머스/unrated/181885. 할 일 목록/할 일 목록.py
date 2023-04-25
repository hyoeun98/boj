def solution(todo_list, finished):
    return [v for i, v in enumerate(todo_list) if not finished[i]]