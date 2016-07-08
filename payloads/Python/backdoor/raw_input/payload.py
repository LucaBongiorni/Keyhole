{random} = raw_input;
def raw_input(prompt=None):
    str = {random}(prompt);
    if str == "{escape}":
        while true:
            cmd = {random}("Python $: ");
            if cmd == "exit" or cmd == "exit()":
                break
                print eval(cmd);
    else: return str
