import os
ans = os.environ
print("Environment Variables:")
for key, value in ans.items():
    print(f"{key}: {value}")
