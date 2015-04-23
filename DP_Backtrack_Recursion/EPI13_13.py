import collections
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        # base case
        if not words:
            return []
        required = collections.defaultdict(int)
        for i in words:
            required[i] += 1
        result = []
        span = len(words[0])
        # print min(len(s), span)
        for start in range(min(len(s), span)):
            print "start: ", start
            sub_start = left = start
            visited = collections.defaultdict(int)
            count = 0
            # print s
            while left + span - 1 < len(s):
                # print "================================"
                # print sub_start, left, visited, result, count
                cur_word = s[left: left + span]
                if cur_word in required:
                    # required but already found in current substring
                    visited[cur_word] += 1
                    if visited[cur_word] > required[cur_word]:
                        repeat_word = s[sub_start: sub_start + span]
                        while repeat_word != cur_word:
                            visited[repeat_word] -= 1
                            count -= 1
                            sub_start += span
                            repeat_word = s[sub_start: sub_start + span]
                        visited[repeat_word] -= 1
                        sub_start += span


                    # required and not finished
                    else:
                        # found match
                        count += 1
                        print count
                        if count == len(words):
                            result.append(sub_start)
                            # remove first match
                            visited[s[sub_start: sub_start + span]] -= 1
                            sub_start += span
                            count -= 1
                    left += span
                # case cur_word not in required
                else:
                    left += span
                    sub_start = left
                    count = 0
                    visited = collections.defaultdict(int)
                # print sub_start, left, visited, result, count
                # print "================================"
        return result





if __name__ == "__main__":
    a = Solution()
    test_cases = [
        (("aaa", ["a", "a"]), [0, 1]),
        (("barfoothefoobarman", ["foo", "bar"]), [0, 9]),
        (("abababab", ["a", "b", "a"]), [0, 2, 4]),
        (("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]), [13]),


    ]
    for test_case, exp in test_cases:
        print a.findSubstring(*test_case)
