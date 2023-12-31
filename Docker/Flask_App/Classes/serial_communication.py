"""
_summary_
"""
import json
import random
import threading
import time
from typing import Union

import serial


class SerialObject():
    """ Serial Object Class """

    def __init__(
        self,
        *args,
        port: Union[str, None] = None,
        baudrate: int = 9600,
        bytesize: int = 8,
        parity: str = "N",
        stopbits: float = 1,
        timeout: Union[float, None] = None,
        **kwargs,
    ):
        super(SerialObject, self).__init__(*args, **kwargs)
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout

        self.serial: serial.Serial

    def __enter__(self):
        self.serial = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            bytesize=self.bytesize,
            parity=self.parity,
            stopbits=self.stopbits,
            timeout=self.timeout,
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.serial.close()

    def read(self):
        """ Read Serial and Return """
        return self.serial.read()

    def read_yield(self):
        """ Read Serial and Yield """
        while True:
            time.sleep(0.05)
            yield self.serial.read()

    @staticmethod
    def read_yield_simulate():
        """ Simulation of Read Serial and Yield """

        analog_value = 256
        current_time = 123456
        temperature = 25.5
        humidity = 77.7
        water_temperature = 24.8
        air_quality = 35

        # Re-assign values
        population = 26
        oxygen = 88
        co2 = 12
        humidity = 77.7
        temperature_environment = 21.5
        temperature_water = 21.8
        # producing_o2 = 55.74
        # carbon_footprint_recycle = 79.83
        producing_o2 = 3.3
        carbon_footprint_recycle = 4.71

        sleep_time = 5
        while True:
            time.sleep(sleep_time)
            producing_o2 += 7/3600/sleep_time
            carbon_footprint_recycle += 10/3600/sleep_time

            if temperature_environment > 21.5:
                temperature_environment -= 0.001
            else:
                temperature_environment += 0.002

            if temperature_water < 21.8:
                temperature_water += 0.001
            else:
                temperature_water -= 0.002

            light_level = analog_value

            if light_level < 105:
                light_status = "Işık yeterli, fotosentez yapılıyor"
            else:
                light_status = "Işık yetersiz, dinlenme sürecinde"

            # output = f"Analog Value: {analog_value} | Time: {current_time} | Temperature: {temperature}C | Humidity: {humidity}% | DS18B20 Temp: {water_temperature}ºC / {water_temperature * 1.8 + 32}ºF | Air Quality: {air_quality}PPM | Light Level: {light_level} - {light_status}"

            # print(output)
            _output = json.dumps(
                {
                    "analog_value": analog_value,
                    "current_time": current_time,
                    "temperature": temperature,
                    # "humidity": humidity,
                    "water_temperature": water_temperature,
                    "air_quality": air_quality,
                    "light_level": light_level,
                    "light_status": light_status,

                    # Re-assign values
                    "population": population,
                    "oxygen": oxygen,
                    "co2": co2,
                    "humidity": humidity,
                    "temperature_environment": round(temperature_environment, 1),
                    "temperature_water": round(temperature_water, 1),
                    "producing_o2": round(producing_o2, 2),
                    "carbon_footprint_recycle": round(carbon_footprint_recycle, 2),
                }
            )
            yield "data: " + _output + "\n\n"
            # time.sleep(2)

    def task(self):
        """ Thread Task """
        thread = threading.Thread(
            target=self.read_yield_simulate, name='read_yield_simulate')

        time.sleep(0.05)
        print("Thread is starting...")
        thread.start()
        print("Thread is running...")
        time.sleep(0.03)

        thread.join()


if __name__ == "__main__":
    # with SerialObject(port="COM3") as serial_object:
    #     for data in serial_object.read_yield_simulate():
    #         print(data)
    SerialObject().task()
    while True:
        time.sleep(1)
        print(".")
