string1 = "hellworldsdfka"
string2 = "world"

def substr(str1, str2, count):
    if (str1 == 0 or str2==0):
        return count
    if(string1[str1-1] == string2[str2-1]):
        count = substr(str1-1, str2-1, count+1)
    count = max(count, max(substr(str1, str2 -1, 0), substr(str1 - 1, str2, 0)))

    return count

output = substr(len(string1), len(string2), 2)
