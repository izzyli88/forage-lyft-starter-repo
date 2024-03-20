from Battery.Battery import Battery

class NubbinBattery(Battery):
    SERVICE_DURATION = 4

    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        exp_year = self.last_service_date.year + NubbinBattery.SERVICE_DURATION
        exp_date = self.last_service_date.replace(year=exp_year)
        if exp_date <= self.current_date:
            return True
        else:
            return False
