class EinstamosEquationBalancer:
    def isValid(self, equations: str) -> bool:
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_bracket = set(["(", "[", "{"])
        stack = []
        for equation_char in equations:
            if equation_char in open_bracket:
                stack.append(equation_char)
            elif stack and equation_char == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
