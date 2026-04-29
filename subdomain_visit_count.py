class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        token_counts = {}
        for cpdomain in cpdomains:
            split = cpdomain.split()
            count = int(split[0])
            tokens = split[1].split(".")
            d = []
            for i in range(len(tokens)):
                d = ".".join(tokens[i:])
                token_counts[d] = token_counts.get(d, 0) + count

        print(token_counts)
        result = []
        for d, count in token_counts.items():
            result.append(f"{count} {d}")
        return result
