"""Import values from graphs.config."""

#====Setup====#

config_importer_list = []

#====Helper functions====#

def int_value_above_zero(name, value, default):
    """Return int of value if value can be turned into an int
    and is positive,
    otherwise print an error message and return default.
    
    name -- name for error message.
    value -- value.
    default -- default (should be a positive integer).
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
    default -- default (should be a float).
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
    default -- default (should be a boolean).
    """
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    print(f"{name} needs to be an bool, using default {default}.")
    return default
    
def string_value_or_none(name, value, deault):
    """If value.lower() is "none", return None,
    else return the string of value.
    
    The arguement default is included to be consistent with
    the other value functions in this file.
    """
    if value.lower() == "none":
        return None
    return str(value)


#====Class====#

class ConfigImporter:
    """A class to import values from graph.config."""
    
    def __init__(self, name, default, validation):
        """__init__ for ConfigImporter
        
        name -- name (for error messages). Should be in
        the form mixedCase.
        default -- value to be returned if invalid config.
        validation -- validation function for import from this page
        (with arguements in the form (name, value, defualt)).
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
        RUN_BRUTE_FORCE, TIMES_TO_RUN):
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
    try:
        with open("graphs.config", "r") as config_file:
            for line in config_file.readlines():
                line_bits = line.strip().split(" ")
                for config_thing in config_importer_list:
                    if line_bits[0] == config_thing.name:
                        config_thing.value = config_thing.run_validation(
                            line_bits[1])
                        
    except FileNotFoundError:
        print("graphs.config not found. Using default values.")
    except Exception as e:
        print(f"Another Exception was raised ({e})")
    finally:
        config_file.close()
    
    return_list = [config_thing.value for config_thing
        in config_importer_list]
    return return_list
