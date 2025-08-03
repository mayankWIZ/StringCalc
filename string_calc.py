


import re
MUL_DELIM_REGEX = r"(\[.*?\])"
DELIM_REGEX = r"(\/\/(.*?)\n)?(.*)"


def add(input: str):
    delims = [","]
    if input.startswith("//"):
        matched = re.match(DELIM_REGEX, input, flags=re.DOTALL)
        if matched and matched.group(2):
            delim = matched.group(2)
            input = input.replace(matched.group(1), "")
            delims = [
                delim.removeprefix("[").removesuffix("]")
                for delim in re.findall(MUL_DELIM_REGEX, delim)
                if delim
            ]
            if not delims:
                delims = [delim]
    delims.append("\n")
    nums = []
    invalid_nums = []
    print("delims", delims)
    for num in re.split('|'.join(map(re.escape, delims)), input):
        if num:
            num = int(num.strip())
            if num >= 0 and num <= 1000:
                nums.append(num)
            elif num < 0:
                invalid_nums.append(str(num))
    if invalid_nums:
        raise ValueError(
            "Negatives not allowed - got {}".format(
                ",".join(invalid_nums)
            )
        )
    if not len(nums):
        return 0
    return sum(nums)


print(add("//[***][abc]xyz\n2***3***6\n1abc1000"))
