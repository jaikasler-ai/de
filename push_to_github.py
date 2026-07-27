import os
import subprocess

git_exe = os.path.abspath(r'mingit\cmd\git.exe')

with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write("mingit/\nnode_modules/\n.DS_Store\n")

def run_git(args):
    print(f"Running: git {' '.join(args)}")
    res = subprocess.run([git_exe] + args, capture_output=True, text=True, cwd=os.getcwd())
    if res.stdout:
        print("STDOUT:", res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    return res

run_git(['init'])
run_git(['config', 'user.name', 'jaikasler-ai'])
run_git(['config', 'user.email', 'jaikasler@gmail.com'])
run_git(['remote', 'remove', 'origin'])
run_git(['remote', 'add', 'origin', 'https://github.com/jaikasler-ai/de.git'])
run_git(['branch', '-M', 'main'])
run_git(['add', '.'])
run_git(['commit', '-m', 'Deploy code and 143 QCMs to GitHub'])
print("Pushing to remote origin main...")
res = run_git(['push', '-u', 'origin', 'main', '--force'])
print("Done!")
