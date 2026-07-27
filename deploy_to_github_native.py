import os
import shutil
import subprocess

git_exe = r"C:\Program Files\Git\cmd\git.exe"

git_dir = os.path.abspath('.git')
if os.path.exists(git_dir):
    try:
        shutil.rmtree(git_dir)
        print("Cleared previous .git directory")
    except Exception as e:
        print("Note on .git removal:", e)

with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write("mingit/\nnode_modules/\n.DS_Store\n")

def run_git(args):
    print(f"Executing: git {' '.join(args)}")
    res = subprocess.run([git_exe] + args, capture_output=True, text=True, cwd=os.getcwd())
    if res.stdout:
        print("STDOUT:", res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    return res

run_git(['init'])
run_git(['config', 'user.name', 'jaikasler-ai'])
run_git(['config', 'user.email', 'jaikasler@gmail.com'])
run_git(['remote', 'add', 'origin', 'https://github.com/jaikasler-ai/de.git'])
run_git(['branch', '-M', 'main'])
run_git(['add', '.'])
run_git(['commit', '-m', 'Deploy application and 143 QCMs'])
print("Pushing to GitHub remote origin main...")
res = run_git(['push', '-u', 'origin', 'main', '--force'])
print("Completed deployment!")
