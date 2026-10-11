
import requests
import csv
import logging
import time

# Save errors in a file
logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Accept multiple usernames
usernames = input(
    "Enter GitHub usernames separated by commas: "
).split(",")

# Create the CSV file
with open("summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["login", "name", "public repos", "followers"])

    # Process each username
    for username in usernames:
        username = username.strip()

        if not username:
            continue

        url = f"https://api.github.com/users/{username}"
        success = False

        # Try each request up to 3 times
        for attempt in range(1, 4):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                user = response.json()

                writer.writerow([
                    user["login"],
                    user["name"],
                    user["public_repos"],
                    user["followers"]
                ])

                print(f"Success: {username}")
                success = True
                break

            except requests.RequestException as e:
                logging.error(
                    "User: %s | Attempt: %s/3 | Error: %s",
                    username, attempt, e
                )

                print(
                    f"Attempt {attempt}/3 failed for {username}"
                )

                if attempt < 3:
                    time.sleep(1)

        if not success:
            print(f"Giving up on {username} after 3 attempts.")

print("Finished! Check summary.csv and errors.log")
