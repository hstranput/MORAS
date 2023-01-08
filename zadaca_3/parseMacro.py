def _parse_macros(self):
    self._iter_lines(self._parse_macro)


def _parse_macro(self, line, o, p):
    if line[0] == "$":
        macrostr = line[1:]
        macro = macrostr.split("(")

        comm = macro[0]
        print(macro)

        argsstr = []
        args = []

        if len(macro) > 1:
            argsstr = macro[1]
            argsstr = argsstr.replace(")", "")
            args = argsstr.split(",")

        if comm == "MV":
            lst = self._create_mv(args[0], args[1])
            return lst

        elif comm == "SWP":
            lst = self._create_swp(args[0], args[1])
            return lst

        elif comm == "SUM":
            lst = self._create_sum(args[0], args[1], args[2])
            return lst

        elif comm == "WHILE":
            lst = self._create_while(args[0])
            return lst

        elif comm == "END":
            lst = ["@WHILE" + str(self._nested), "0;JMP", "(END" + str(self._nested) + ")"]
            self._nested -= 1
            return lst

        else:
            self._flag = False
            self._line = p
            self._errm = "Invalid command: " + comm
            return ""

    else:
        return line


def _create_mv(self, a, b):
    lst = ["@" + a, "D=M", "@" + b, "M=D"]
    return lst


def _create_swp(self, a, b):
    lst = ["@temp", "M=0", "@" + a, "D=M", "@temp", "M=D", "@" + b, "D=M", "@" + a, "M=D", "@temp", "D=M", "@" + b,
             "M=D"]
    return lst


def _create_sum(self, a, b, d):
    lst = ["@" + a, "D=M", "@" + b, "D=D+M", "@" + d, "M=D"]
    return lst


def _create_while(self, arg):
    self._nested += 1
    lst = ["(WHILE" + str(self._nested) + ")", "@" + arg, "D=M", "@END" + str(self._nested), "D;JEQ"]
    return lst