from datetime import datetime

str_timestamp = datetime.now().strftime(f"%Y-%m-%d %H:%M")
print(str_timestamp)


# str_timestamp = f"2025-01-18 12:38"
try:
    timestamp = datetime.strptime(str_timestamp, f"%Y-%m-%d %H:%M")
    print(timestamp)
except ValueError:
    print("aaaaaaaaaaaaaaaa!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



print(f"------------------------")

sdws = "111,ss3".replace(f",", f".")
try:
    print(float(sdws))
except ValueError:
    print(f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2")