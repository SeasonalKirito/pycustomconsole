from .ansi import Fore

class DefaultValues():
    autoReset           = True
    textColor           = Fore.WHITE

class PrintTypes():
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    INFO = Fore.YELLOW
    

def autoResetCheck():
    if DefaultValues.autoReset:
        return Fore.RESET
    else:
        # return
        pass

def init(autoReset: bool = None):
    if not isinstance(autoReset, bool):
        print(f"{Fore.RED}autoReset given does not match a boolean (e.g., [True, False]), autoReset has been set to false automatically{Fore.RESET}")
    else:
        try:
            DefaultValues.autoReset = autoReset
        except Exception as e:
            print(f"{Fore.RED}{e}{Fore.RESET}")

def log(color=DefaultValues.textColor, text="returned None"):
    try:
        return(f"{str(color)}{str(text)}{autoResetCheck()}")
    except Exception as e:
        print(f"\033[31m{e}\033[0m")