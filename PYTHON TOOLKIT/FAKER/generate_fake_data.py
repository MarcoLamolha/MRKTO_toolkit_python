from faker import Faker
import json
from datetime import datetime

fake = Faker()

def generate_records(num_records=600):
    data = []
    
    for _ in range(num_records):
        record = {
            "id": fake.unique.random_number(digits=6),
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": {
                "street": fake.street_address(),
                "city": fake.city(),
                "state": fake.state(),
                "zip": fake.zipcode(),
                "country": fake.country()
            },
            "company": fake.company(),
            "job_title": fake.job(),
            "credit_card": {
                "number": fake.credit_card_number(),
                "expiry": fake.credit_card_expire(),
                "type": fake.credit_card_provider()
            },
            "account_balance": round(fake.random.uniform(100, 999999), 2),
            "created_at": fake.date_time_this_year().isoformat(),
            "is_active": fake.boolean()
        }
        data.append(record)
    
    return data

if __name__ == "__main__":
    records = generate_records()
    
    with open('fake_data.json', 'w') as f:
        json.dump(records, f, indent=2)
    
    print(f"Generated {len(records)} records in fake_data.json")