from Tests.TestAll import runAllTests
from UI.new_console import menu
from UI.console import RunMain


def main():
    runAllTests()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        RunMain([])
    elif optiune == "2":
        menu([])


main()