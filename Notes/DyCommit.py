import subprocess

def run_command(command):
    """运行一个 shell 命令并返回结果"""
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: Command failed with error:\n{stderr.decode(errors='ignore')}")
    else:
        print(f"Success: Command output:\n{stdout.decode(errors='ignore')}")
    return process.returncode, stdout.decode(errors='ignore'), stderr.decode(errors='ignore')

def check_changes():
    """检查是否有未提交的更改"""
    _, stdout, _ = run_command("git status --porcelain")
    return bool(stdout.strip())  # 如果有输出，说明有未提交的更改

def add_and_push():
    # 检查是否有需要提交的更改
    if not check_changes():
        print("Nothing to commit. Working tree clean.")
        return  # 如果没有更改，退出函数

    # 添加所有更改
    if run_command("git add .")[0] != 0:
        return  # 如果命令失败，则退出

    # 提交更改
    if run_command("git commit -m '自动提交'")[0] != 0:
        return  # 如果命令失败，则退出

    # 推送更改到远程 main 分支
    if run_command("git push origin main")[0] != 0:
        return  # 如果命令失败，则退出

# 立即执行 add 和 push
add_and_push()