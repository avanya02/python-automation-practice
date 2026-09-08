import json
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

try:
    with open("customers.json", "r") as file:
        customers = json.load(file)

except FileNotFoundError:
    logging.error("customers.json was not found")
    exit()

except json.JSONDecodeError:
    logging.error("customers.json contains invalid JSON")
    exit()


results = []

for customer in customers:

    if not customer["active"]:
        continue

    customer_id = customer["id"]

    logging.info(f"Processing customer {customer_id}")

    payload = {
        "customer_id": customer["id"],
        "name": customer["name"]
    }

    try:

        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=payload
        )

        if response.status_code == 201:

            logging.info(
                f"Customer {customer_id} processed successfully"
            )

            results.append({
                "customer_id": customer_id,
                "status": "success"
            })

        else:

            logging.error(
                f"API failed for customer {customer_id}: "
                f"{response.status_code}"
            )

            results.append({
                "customer_id": customer_id,
                "status": "failed",
                "error": f"HTTP {response.status_code}"
            })

    except requests.exceptions.RequestException as e:

        logging.error(
            f"Request failed for customer {customer_id}: {e}"
        )

        results.append({
            "customer_id": customer_id,
            "status": "failed",
            "error": str(e)
        })


with open("results.json", "w") as file:
    json.dump(results, file, indent=4)

logging.info("Processing completed")