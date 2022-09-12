class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0


    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        
        log_string = f'{order.name} was purchased at location {store_number} for ${order.price} | Total: ${self.daily_sales} \n'
        
        log_file = open('log.txt', 'a')
        log_file.write(log_string)
        log_file.close()


file_logger = Logger()