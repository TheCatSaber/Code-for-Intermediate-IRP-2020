"""Import values from graphs.config."""
# Copyright (C) 2020-21 TheCatSaber

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


#====Imports====#

from typing import Any, Callable, Union

#====Validation functions====#

def int_value_above_zero(name: str, value: Any, default: int) -> int:
    """Return int of value if value can be turned into an int
    and is positive,
    otherwise print an error message and return default.
    
    name -- name for error message.
    value -- value.
    default -- default (positive integer).
    """
    try:
        new_value = int(value)
        if new_value > 0:
            return new_value
        else:
            print(f"{name} needs to be greater than 0, using default {default}.")
            return default
    except:
        print(f"{name} needs to be an integer, using default {default}.")
        return default

def float_value(name: str, value: Any, default: float) -> float:
    """Return float of value if value can be turned into a float,
    otherwise print an error message and return default.
    
    name -- name for error message.
    value -- value.
    default -- default (float).
    """
    try:
        new_value = float(value)
        return new_value
    except:
        print(f"{name} needs to be a number, using default {default}.")
        return default

def bool_value(name: str, value: str, default: bool) -> bool:
    """Return bool of value if value is the string of a bool,
    otherwise print an error message and return default.
    
    name -- name for error message.
    value -- value.
    default -- default (boolean).
    """
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    print(f"{name} needs to be an bool, using default {default}.")
    return default
    
def string_value_or_none(name: str, value: str, default: Union[str, None]) \
        -> Union[str, None]:
    """If value.lower() is "none", return None,
    else return the string of value.
    
    The arguements name and default are included to be consistent with
    the other validation functions in this file.
    name -- name for error message.
    value -- value.
    default -- default (string or None).
    """
    if value.lower() == "none":
        return None
    return str(value)

def string_value(name: str, value: str, default: str) -> str:
    """Return string of value.
    
    The arguements name and default are included to be consistent with
    the other value functions in this file.
    name -- name for error message.
    value -- value.
    default -- default (string).
    """
    return str(value)

def ratios_int_zero_or_above(
        name: str, value: str, default: dict[str, int]
    ) -> dict[str, int]:
    """Return dict of keys of default matched with values from value,
    only when the value is an int with value zero or above.
    
    If not same length, go through value as far as possible,
    and rest of default stays the same, or extra values are discarded
    
    name -- name for error message.
    value -- value in form a,b,c,d,e,f,g....
    default -- default (dict with same length as value).
    """
    return_dict: dict[str, int] = {}
    
    keys = list(default.keys())
    default_values = list(default.values())
    values = value.split(",")
    
    for counter in range(len(default)):
        try:
            value_to_store = int(values[counter])
            if value_to_store < 0:
                value_to_store = default_values[counter]
                print(f"The {counter+1} value in {name.lower()} " \
                      f"needs to be positive or 0, " \
                      f"using default {value_to_store}.")
            
        except ValueError:
            value_to_store = default_values[counter]
            print(f"The {counter+1} value in {name.lower()} " \
                  f"needs to be an integer, " \
                  f"using default {value_to_store}.")
        except IndexError:
            value_to_store = default_values[counter]
            print(f"The {counter+1} value in {name.lower()} " \
                  f"was not defined, " \
                  f"using default {value_to_store}.")
        except:
            value_to_store = default_values[counter]
            print(f"The {counter+1} value in {name.lower()} " \
                  f"experienced an unexpected error, " \
                  f"using default {value_to_store}.")
        
        return_dict[keys[counter]] = value_to_store
    
    if len(values) > len(keys):
        print(f"Too many values provided for {name.lower()}, " \
               "discarding unused ones.")
    
    return return_dict

#====Class====#
        
class Config(object):
    # Do with Github actions future Alex
    """A class to store the config for the program
    
    graphSize (default: 6) -- defines how many vertices in the graph.
    Valid: any integer greater than 0.

    randomGraphEdgeNumber (default: 2) -- number of edges per vertex for
    random_graphs().
    Valid: any integer greater than 0.

    erdosRenyiP (default: 0.5) -- defines p for Erdős-Rényi model.
    (The second one with G(n, p)).
    Valid: any float. If value <= 0, there will be no edges,
    and if >= 1, the graph will be complete.

    colouringToShow (default: None) -- defines which colouring to show.
    None is no colouring, others are the colouring of the same name.
    Valid: None, randomGreedy, degreeGreedy, DSatur, productBruteForce,
    customBruteForce, iteratedGreedy. (Invalid will default to None).

    showLabels (default: True) -- whether to show the labels on the
    output graph.
    Valid: True or False.

    useErdosRenyi (default: True) -- whether to use Erdős-Rényi for
    random graph generation.
    If False, uses random_graphs() (designed by TheCatSaber).
    Valid: True or False.

    runBruteForce (default: True) -- whether to run the brute force algorithms
    (useful to make False if you want to run with large graphs).
    Valid: True or False.

    timesToRun (default: 1) -- If 1, run the run_once() function
    (runs once and output includes a picture), if > 1,
    run each colouring that number of times, but no picture output.
    Valid: any integer greater than 0.

    IGInital (default: "degree_greedy") -- the initial colouring to
    use for iterated greedy.
    Invalid will default to degree_greedy
    Valid: degree_greedy, random_greedy, dsatur

    IGLimit (default: 100) -- how many iterations of iterated greedy to
    perform without in number of colours.
    Valid: any integer greater than 0.

    IGGoalK (default: 1) -- goal for how many colours to achieve
    in iterated greedy.
    Iterated greedy will automatically stop once achieved.
    Valid: any integer greater than 0.

    ig_ratios (default: 50,30,50,0,0,0) -- Ratios for functions
    for iterated greedy.
    In order: reverse group, random group, largest first group
    smallest first group,
    increasing total degree, decreasing total degree.
    Valid: comma separated values of 6 positive integers (no spaces).
    """

    config_values: dict[str, Any] = {
        "graphSize": 6,
        "randomGraphEdgeNumber": 2,
        "erdosRenyiP": 0.5,
        "colouringToShow": None,
        "showLabels": True,
        "useErdosRenyi": True,
        "runBruteForce": True,
        "timesToRun": 1,
        "IGInitial": "degree_greedy",
        "IGLimit": 100,
        "IGGoalK": 1,
        "IGRatios": {
            "reverse": 50,
            "random": 30,
            "largest": 50,
            "smallest": 0,
            "increasing": 0,
            "decreasing": 0
        }
    }
    

    @classmethod
    def set_value(cls, key: str, value: str,
            validation: Callable[[str, str, Any], Any]) -> None:
        default = cls.config_values[key]
        try:
            cls.config_values[key] = validation(key, value, default)
        except:
            print(f"{key} not defined in graphs.config, "\
                  f"using default {default}.")


def config_imports():

    # Make dictionary of values in file
    with open("graphs.config", "r") as config_file:
        lines = config_file.readlines()
        file_values: dict[str, str] = {}
        try:
            for line in lines:
                line = line.strip().split(" ")
                file_values[line[0]] = line[1]
        except IndexError:
            print("Invalid graphs.config layout, using defaults.")
            return Config
        except:
            pass

    validation_functions: dict[str, Callable[[str, str, Any], Any]] = {
        "graphSize": int_value_above_zero,
        "randomGraphEdgeNumber": int_value_above_zero,
        "erdosRenyiP": float_value,
        "colouringToShow": string_value_or_none,
        "showLabels": bool_value,
        "useErdosRenyi": bool_value,
        "runBruteForce": bool_value,
        "timesToRun": int_value_above_zero,
        "IGInitial": string_value,
        "IGLimit": int_value_above_zero,
        "IGGoalK": int_value_above_zero,
        "IGRatios": ratios_int_zero_or_above
    }
    for key in Config.config_values.keys():
        try:
            Config.set_value(key, file_values[key], validation_functions[key])
        except:
            print(f"{key} not defined in graphs.config, " \
                  f"using default {Config.config_values[key]}")
    return Config