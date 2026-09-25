class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            res = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    cur, i = parse(i + 1)
                    i += 1
                else:
                    cur = {expression[i]}
                    i += 1

                # Concatenation
                res = {a + b for a in res for b in cur}

                # Union
                if i < len(expression) and expression[i] == ',':
                    i += 1
                    other, i = parse(i)
                    res |= other
                    break

            return res, i

        result, _ = parse(0)
        return sorted(result)