class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        #when a start happens we modify the total time for last value in stack
        #when it ends we update the exclusive time and pop last value from stack
        call_stack = []
        exclusive_time_dict = collections.defaultdict(int)
        prev_time = 0
        for log in logs:
            fid, state, time = log.split(":")
            fid = int(fid)
            time = int(time)
            if state == "start":
                if call_stack:
                    last_fid = call_stack[-1]
                    exclusive_time_dict[last_fid] += time-prev_time
                prev_time = time
                call_stack.append(fid) 
            else:
                exclusive_time_dict[call_stack.pop()] += (time+1)-prev_time
                prev_time = time+1
        return list(exclusive_time_dict.values())