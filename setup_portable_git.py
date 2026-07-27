import os
import urllib.request
import zipfile
import subprocess

git_dir = os.path.abspath('mingit')
git_exe = os.path.join(git_dir, 'cmd', 'git.exe')

if not os.path.exists(git_exe):
    print("Downloading Portable MinGit...")
    url = "https://github.com/git-for-windows/git/releases/download/v2.45.2.windows.1/MinGit-2.45.2-64-bit.zip"
    zip_path = "mingit.zip"
    urllib.request.urlretrieve(url, zip_path)
    print("Extracting MinGit...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(git_dir)
    os.remove(zip_path)
    print("MinGit installed successfully!")

print("Using Git executable:", git_exe)

def run_git(args):
    res = subprocess.run([git_exe] + args, capture_output=True, text=True, cwd=os.getcwd())
    print(f"git {' '.join(args)}")
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
run_git(['commit', '-m', 'Initial commit with 143 QCMs and auto-sync server'])
run_git(['push', '-u', 'origin', 'main', '--force'])
