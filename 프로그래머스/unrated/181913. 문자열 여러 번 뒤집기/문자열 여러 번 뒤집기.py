def solution(my_string, queries):

    for q in queries:
        st,ed = q[0],q[1]+1
        new_str = my_string[st:ed]
        my_string = my_string[:st]+new_str[::-1]+my_string[ed:]

    return my_string