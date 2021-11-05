from datetime import datetime

class Logger:
    def log_transaction(self, account, amount, balance):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open(f"data/account_history/{account}", "a")
        f.write(f"{timestamp} {amount} {balance}\n")
        f.close()