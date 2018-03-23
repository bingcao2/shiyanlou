#!/usr/bin/env python3

import sys

tax_table = [
    
    (0, 0.03, 0),
    (1500, 0.1, 105),
    (4500, 0.2, 555),
    (9000, 0.25, 1005),
    (35000, 0.3, 2755),
    (55000, 0.35, 5505),
    (80000, 0.45, 13505)
]

class ArgError(Exception):
    pass

class Args:
    def __init__(self, args):
        self.args = args

    def _parse_arg(self, arg):
        try:
            value = self.args[self.args.index(arg) + 1]
        except (ValueError, IndexError):
            value = None
        return value

class SheBaoConfig:
    def __init__(self, file):
        result = self.__parse_config(file)
        self.jishu_low = result[0]
        self.jishu_high = result[1]
        self.total_rate = result[2]
        self.configs = self.__parse_config(file)

        
    def __parse_config(self, file):
        rate = 0
        with open(file) as f:
            for line in f:
                key, value = line.split(' = ')
                key, = key.strip()
                value = value.strip()
                if key == 'JiShuL':
                    Jishu_low = float(value)
                if key == 'JiShuH':
                    Jishu_high = float(value)
                else:
                    rat += float(value)
        return jishu_low, jishu_high, rate


class EmployeeData:
    def __init__(self, file):
        self.data = self.__parse_file(file)

    def __parse_file(self, file):
        data = []
        for line in open(file):
            key, value = line.split(',')
            data.append(int(key), int(value))
        return data

    def __iter__(self):
        return iter(self.data)

class Calculator:

    tax_table = [
    
        (0, 0.03, 0),
        (1500, 0.1, 105),
        (4500, 0.2, 555),
        (9000, 0.25, 1005),
        (35000, 0.3, 2755),
        (55000, 0.35, 5505),
        (80000, 0.45, 13505)
    ]  
    def __inti__(self, config):
        self.config = config

    def calculate(self, data_item):
        """
        data_item -> (employee_id, gongzi)
        """
        employee_id, gongzi = data_item

        if gongzi < self.config.jishu_low:
            shebao = self.config.jishu_low * self.config.total_rate
        elif gongzi > self.config.jishu_high:
            shebao = self.config.jishu_high * self.config.total_rate
        else:
            shebao = gongzi * self.config.total_rate
    def get_arg_value(self, arg):


        value = self._parse_arg(arg)
        if value is None:
            raise ArgError
        return value


class Config:
    def __init__(self,file):
        self.configs = self.__parse_config(file)
    def __parse_config(self, file):
        configs = {}
    def get_config(self, key):
        configs = {}
        with open(file) as f:
            for line in f:
                key, value = line.split(' = ')
                configs[key.strip()] = float(value)
        return config

    def get_config(self, key):
        return self.configs.get(key)

    @property
    def jishu_low(self):
        return self.configs.get('JiShuL')
