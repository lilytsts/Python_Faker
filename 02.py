from faker import Faker

Faker.seed()

fake = Faker()

print(fake.simple_profile(),
    "\n================\n",
    fake.job(),
    "\n================\n",
    fake.address(),
    "\n================\n",
    fake.credit_card_full(card_type='visa'),
    "\n================\n",
    fake.phone_number(),
    "\n================\n",
    fake.ipv4())

