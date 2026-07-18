class TrafficSignal:

    def __init__(self):
        self.green_time = 30
        self.yellow_time = 5
        self.red_time = 35


    def calculate_signal_time(self, vehicle_count):

        if vehicle_count > 50:
            return 60

        elif vehicle_count > 20:
            return 45

        else:
            return 30


    def signal_status(self, vehicle_count):

        time = self.calculate_signal_time(vehicle_count)

        return {
            "signal": "GREEN",
            "time": time,
            "vehicles": vehicle_count
        }