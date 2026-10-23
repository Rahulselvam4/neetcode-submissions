class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp not in map:
                map[temp] = []
            map[temp].append(s)
            
                
        return list(map.values())