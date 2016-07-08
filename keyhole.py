#!/usr/bin/python
from pygments.lexers import guess_lexer, get_lexer_for_filename #Language Detection
from sys import argv, exit #System functions
import os.path, json, random, string

def detect(file, buffer):
    try:
        lex = guess_lexer(buffer)
    except:
        lex = get_lexer_for_filename(file)

    #isolate x from <pygments.lexers.xLexer>
    lex = str(lex) # convert to string
    lex = lex.replace("<", "").replace(">", "") # remove angle brackets
    lex = lex.replace("pygments.lexers.", "").replace("Lexer", "") # isolating x

    return lex

def load(file):
    buf = ""
    with open(file, "r") as f:
        buf = f.read()
    lex = detect(file, buf)
    return buf, lex

def prepare(file, payload):
    with open(payload + "readme.json", "r") as f:
        config = f.read()
    config = json.loads(config)
    print(config['info'])
    print("")
    payload = payload + config['payload']
    with open(payload, 'r') as f:
        payload = f.read()
    if "options" in config:
        print("Set options: ")
        formatString = ""
        UsageFormat = ""
        for k, v in config['options'].iteritems():
            print("")
            print("Info: " + str(v['info']))
            resp = raw_input("{} [{}]".format(v['name'], v['default']))
            config['usage'] = eval("str(config['usage']).format(" + k + "='" + resp + "')")
            UsageFormat = UsageFormat + k + "='" + resp + "',"
            formatString = formatString + k + "='" + resp + "',"

        UsageFormat = "str(config)['usage']).format('" + UsageFormat + "')"
        formatString = "str(payload).format('" + formatString + "')"
        eval(UsageFormat)
        eval(formatString)

    print(config['usage'])
    payload = payload.format(random=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6)))
    print("")
    with open(file, 'r') as f:
        before = f.read()

    location = config['location']
    with open(file, 'w') as f:
        if location == "top":
            f.write(payload + "\r")
            f.write(before)
        else:
            f.write(before + "\r")
            f.write(payload)


    print "Code Injected"

def cmd():
    def help():
        print("keyhole.py (file) (catergory/payload) [type]")
        print("file:        path to file")
        print("cat/payload: payload to use, look in the payloads/[language] directory")
        print("type:        type of file, 'binary' or 'source' defaults to 'source'")
        print("")
        print("Example: keyhole.py test.py backdoor/raw_input source")
        print("Example: keyhole.py jar.jar fun/reverse_text binary")

    def binary(file, payload):
        #TODO: add binary support
        print("binary files are not supported at this time")

    def source(file, payload):
        file, type = load(file)
        print "Language = " + str(type)
        if not os.path.exists("payloads/" + str(type) + "/" + payload):
            print("No such payload " + str(type) + "/" + payload)
            exit()
        payload = "payloads/" + str(type) + "/" + payload + "/"
        print "Payload =  " + payload
        print
        prepare(file, payload)


    def main():
        file = argv[1]
        if not os.path.isfile(file):
            print("No such file " + str(file))
            exit()
        payload = argv[2]
        type = "source"
        if len(argv) > 3:
            type = argv[3]
        if type == "binary":
            binary(file, payload)
        else:
            source(file, payload)
    if len(argv) < 3:
        help()
    else:
        main()


if __name__ == '__main__':
    cmd()
