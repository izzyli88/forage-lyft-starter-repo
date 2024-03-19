from Battery import Battery

class SpindlerBattery(Battery):
    SERVICE_DURATION = 2

    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        years_passed = (self.current_date - self.last_service_date) / 365.25
        return years_passed >= SpindlerBattery.SERVICE_DURATION
