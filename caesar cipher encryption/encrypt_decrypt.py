def encrypt(msg, shift, list1, list2):
    new_msg = ""
    for i in msg:
        found = False
        index = 0
        for j in list1:
            if i == j:
                found = True
                break
            else:
                index += 1
        if found:
            total_index = (index + shift) % len(list2)
            new_msg += list2[total_index]
        else:
            new_msg += i

    print(f"Here's the encoded result: {new_msg.lower()}")


def decrypt(msg, shift, list1, list2):
    new_msg = ""
    for i in msg:
        found = False
        index = 0
        for j in list1:
            if i == j:
                found = True
                break
            else:
                index += 1
        if found:
            total_index = (index - shift) % len(list2)
            new_msg += list2[total_index]
        else:
            new_msg += i

    print(f"Here's the decoded result: {new_msg.lower()}")
