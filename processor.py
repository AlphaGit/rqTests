from time import sleep


def processor_function():
    print("Started worker.")
    sleep(1)
    print("1 second passed.")

    sleep(1)
    print("2 seconds passed.")

    sleep(1)
    print("3 seconds passed.")

    print("Finished.")
