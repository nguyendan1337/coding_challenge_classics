def maxDistinctSubstringLengthInSessions(sessionString):
    # Write your code here
    if not sessionString:
        return 0

    sessions = sessionString.split('*')
    # print(sessions)
    longest = 0
    for session in sessions:
        if len(session) < 1:
            break
        i = 0
        sliding_window = [session[0]]
        for j in range(1, len(session)):
            if session[j] in sliding_window:
                sliding_window.remove(session[i])
                i += 1
            sliding_window.append(session[j])
            longest = max(longest, len(sliding_window))

    return longest

sessionString = "abc*abac*defg"
print(maxDistinctSubstringLengthInSessions(sessionString))