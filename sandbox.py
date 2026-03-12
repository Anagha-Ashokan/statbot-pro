BLOCKED_WORDS = [
    "os.remove",
    "os.system",
    "subprocess",
    "shutil",
    "rm -rf",
    "delete"
]

def check_security(question):

    for word in BLOCKED_WORDS:
        if word in question.lower():
            return False

    return True