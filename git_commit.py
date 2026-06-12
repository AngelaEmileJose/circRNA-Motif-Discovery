import subprocess
import os

# Files and folders to add
files_to_commit = [
    "submission",
    "motif_comparison_report.md",
    "prepare_submission.py",
    "git_commit.py"
]

src_dir = os.path.dirname(os.path.abspath(__file__))

print("Staging files for git...")
for path in files_to_commit:
    full_path = os.path.join(src_dir, path)
    if os.path.exists(full_path):
        subprocess.run(["git", "add", path], cwd=src_dir)
        print(f"Staged: {path}")

# Run git commit
commit_msg = "Add final project submission files and Word report"
print(f"\nCommitting files with message: '{commit_msg}'...")
res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=src_dir, capture_output=True, text=True)

if res.returncode == 0:
    print("Success! Git commit completed.")
    print(res.stdout)
    
    # Run git push
    print("\nPushing to remote repository...")
    push_res = subprocess.run(["git", "push"], cwd=src_dir, capture_output=True, text=True)
    if push_res.returncode == 0:
        print("Success! Pushed to git remote repository.")
        print(push_res.stdout)
    else:
        print("Git push encountered an issue:")
        print(push_res.stderr)
else:
    print("Git commit encountered an issue (perhaps no changes to commit, or git config missing):")
    print(res.stderr)
