"""Import values from graphs.config."""
# Copyright (C) 2020 TheCatSaber

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

#====Setup====#

config_importer_list = []

#====Helper functions====#

def int_value_above_zero(name, value, default):
    """Return int of value if value can be turned into an int
    and is positive,
    otherwise print an error message and return default.
    
    name -- name for error message.
    value -- value.
    default -- default (positive integer).
    """
    if value.isdigit():
        if int(value) > 0:
            return int(value)
        print(f"{name} needs to be positive, using default {default}.")
        return default
    print(f"{name} needs to be an integer, using default {default}.")
    return default

def float_value(name, value, default):
    """Return float of value if value can be turned into a float,
    otherwise print an error message and return default.
    
    name -- name for error message.
    value -- value.
    default -- default (float).
    """
    if value.replace(".","").isdigit():
        return float(value)
    print(f"{name} needs to be a number, using default {default}.")
    return default

def bool_value(name, value, default):
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
    
def string_value_or_none(name, value, default):
    """If value.lower() is "none", return None,
    else return the string of value.
    
    The arguement default is included to be consistent with
    the other value functions in this file.
    name -- name for error message.
    value -- value.
    default -- default (string or None).
    """
    if value.lower() == "none":
        return None
    return str(value)

def string_value(name, value, default):
    """Return string of value.
    
    The arguement default is included to be consistent with
    the other value functions in this file.
    name -- name for error message.
    value -- value.
    default -- default (string).
    """
    return str(value)

def ratios_int_zero_or_above(name, value, default):
    """Return dict of keys of default matched with values from value,
    only when the value is an int with value zero or above.
    
    If not same length, go through value as far as possible,
    and rest of default stays the same, or extra values are discarded
    
    name -- name for error message.
    value -- value in form a,b,c,d,e,f,g....
    default -- default (dict with same length as value).
    """
    return_dict = {}
    
    keys = list(default.keys())
    default_values = list(default.values())
    values = value.split(",")
    
    wrong = False
    
    for counter in range(len(default)):
        try:
            value = int(values[counter])
            if value < 0:
                value = default_values[counter]
                print(f"The {counter+1} value in {name.lower()} " \
                      f"needs to be positive or 0, using default {value}.")
        except ValueError:
            value = default_values[counter]
            print(f"The {counter+1} value in {name.lower()} " \
                  f"needs to be an integer, using default {value}.")
        except IndexError:
            value = default_values[counter]
            print(f"The {counter+1} value in {name.lower()} " \
                  f"was not defined, using default {value}.")
        except:
            value = default_values[counter]
            print(f"The {counter+1} value in {name.lower()} " \
                  f"experienced an unexpected error, using default {value}.")
        
        return_dict[keys[counter]] = value
    
    if len(values) > len(keys):
        print(f"Too many values provided for {name.lower()}, " \
               "discarding unused ones.")
    
    return return_dict

#====Class====#

class ConfigImporter:
    """A class to import values from graph.config."""
    
    def __init__(self, name, default, validation):
        """__init__ for ConfigImporter
        
        name -- name (for error messages). Should be in
        the form mixedCase.
        default -- value to be returned if invalid config.
        validation -- validation function for import from this page
        (with arguements in the form (name, value, default)).
        """
        self.name = name
        self.default = default
        self.validation = validation
        config_importer_list.append(self)
        # self.value starts off at self.default but is changed later.
        self.value = self.default
    
    def run_validation(self, value):
        return self.validation(self.name, value, self.default)
        
    

#====Running function====#
    
def config_imports(
        GRAPH_SIZE, RANDOM_GRAPH_EDGE_NUMBER, ERDOS_RENYI_P,
        COLOURING_TO_SHOW, SHOW_LABELS, USE_ERDOS_RENYI,
        RUN_BRUTE_FORCE, TIMES_TO_RUN, IG_INITIAL,
        IG_LIMIT, IG_GOAL_K, IG_RATIOS):
    """Run config imports.
    
    Arguements are the default values to be returned if not set
    in the config file.
    """
    graph_size =  ConfigImporter("graphSize", GRAPH_SIZE, int_value_above_zero)
    random_graph_edge_number = ConfigImporter(
        "randomGraphEdgeNumber", RANDOM_GRAPH_EDGE_NUMBER,
        int_value_above_zero)
    erdos_renyi_p = ConfigImporter(
        "erdosRenyiP", ERDOS_RENYI_P, float_value)
    colouring_to_show = ConfigImporter(
        "colouringToShow", COLOURING_TO_SHOW, string_value_or_none)
    show_labels = ConfigImporter("showLabels", SHOW_LABELS, bool_value)
    use_erdos_renyi = ConfigImporter(
        "useErdosRenyi", USE_ERDOS_RENYI, bool_value)
    run_brute_force = ConfigImporter(
        "runBruteForce", RUN_BRUTE_FORCE, bool_value)
    times_to_run = ConfigImporter(
        "timesToRun", TIMES_TO_RUN, int_value_above_zero)
    ig_inital = ConfigImporter(
        "IGInitial", IG_INITIAL, string_value)
    ig_limit = ConfigImporter(
        "IGLimit", IG_LIMIT, int_value_above_zero)
    ig_goal_k = ConfigImporter(
        "IGGoalK", IG_GOAL_K, int_value_above_zero)
    ig_ratios = ConfigImporter(
        "IGRatios", IG_RATIOS, ratios_int_zero_or_above)
    try:
        with open("graphs.config", "r") as config_file:
            for line in config_file.readlines():
                line_contents = line.strip().split(" ")
                for config_importer in config_importer_list:
                    if line_contents[0] == config_importer.name:
                        config_importer.value = config_importer.run_validation(
                            line_contents[1])
                        
    except FileNotFoundError:
        print("graphs.config not found. Using default values.")
    except Exception as e:
        print(f"Another Exception was raised: ({e})")
    finally:
        try:
            config_file.close()
        except:
            pass
    
    return_list = [config_importer.value for config_importer
        in config_importer_list]
    return return_list
