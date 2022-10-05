global PROGRAM_NAME, PROGRAM_VERSION, PROGRAM_DEVSTATUS
PROGRAM_NAME = "坤语 for Python"
PROGRAM_VERSION = "1.0beta"
PROGRAM_DEVSTATUS = True
class bfe:
    class applet:
        def applet_title(sw_applet, title):
            sw_applet.title(title)
        class window:
            def refreshTheme(sw_applet, color):
                sw_applet["background"] = color

class bf_ext:
    global out
    out = []

    def kk(code):
        code.replace(" ", "")
        code.replace("\n", "")
        if True == False:
            out.append("\nERROR: Styanx mistakes: " + code)
            return "\nERROR: Styanx mistakes: " + code
        else:

            data = [0 for i in range(1000)]
            pc = 0
            ptr = 0
            skip_loop = False
            bracket_count = 0
            stack = []
            try:
                while pc < len(code):
                    c = code[pc]
                    if skip_loop:
                        if c == '你':
                            bracket_count += 1
                        elif c == '嘛':
                            bracket_count -= 1
                            if bracket_count == 0:
                                skip_loop = False
                        pc += 1
                        continue
                    if c == '哟':
                        ptr += 1
                        pc += 1
                    elif c == '哎':
                        ptr -= 1
                        pc += 1
                    elif c == '鸡':
                        data[ptr] += 1
                        pc += 1
                    elif c == '美':
                        data[ptr] -= 1
                        pc += 1
                    elif c == '干':
                        out.append(chr(data[ptr]))
                        pc += 1
                    elif c == '太':
                        pc += 1
                    elif c == '你':
                        if data[ptr] == 0:
                            # nonlocal bracket_count,skip_loop
                            bracket_count = 1
                            skip_loop = True
                            pc += 1
                        else:
                            pc += 1
                            stack.append(pc)
                    elif c == '嘛':
                        if data[ptr] == 0:
                            pc += 1
                            stack.pop()
                        else:
                            pc = stack[len(stack) - 1]
            except KeyboardInterrupt as e:
                out.append("\nERROR: Styanx mistakes: " + code)
                return "\nERROR: Styanx mistakes: " + code

    def bf_formatter(bf_callback):
        a = ""
        for i in range(0, len(out)):
            a += out[i]
        return a
