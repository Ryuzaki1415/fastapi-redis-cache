import time


def fetch_user_from_slow_source(user_id: int):
    time.sleep(5) 
    return {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john@example.com",
        "source": "slow_api"
    }