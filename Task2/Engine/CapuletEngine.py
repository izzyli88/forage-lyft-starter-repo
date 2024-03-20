from Engine import Engine


class CapuletEngine(Engine.Engine):

    MAX_MILES = 30_000

    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= CapuletEngine.MAX_MILES
    '''
    Task3/
    |
    ----Engine/
        |
        |____init__.py
        |_ Engine.py
        |_ CapuletEngine.py
    
    |
    |___EngineTest/
        |__ __init-_.py
        |_ capulet_test.py
    '''
