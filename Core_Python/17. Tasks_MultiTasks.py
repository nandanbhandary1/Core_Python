"""
1. Can only use 'await' inside 'async def' functions
2. Use 'await' when calling functions that have 'async def'"
3. Use 'await' with asyncio.sleep(), asyncio.gather(), etc.
"""

# These are imports - they bring in tools we need
import asyncio  # Tool for doing multiple things at once
import time  # Tool to measure how long things take


# This is a function - think of it like a recipe
# The word "async" means this function can wait without blocking other things
# The word "def" means we're creating a function
async def download_file(name, seconds):
    # This function pretends to download a file
    # It takes two inputs:
    # - name: what file we're downloading (like "File1")
    # - seconds: how long the download takes

    # Print means "show this text on screen"
    print(f"Started downloading {name}")

    # await asyncio.sleep(seconds) means "wait for this many seconds"
    # It's like a timer - the function pauses here
    await asyncio.sleep(seconds)

    # After waiting, print this message
    print(f"Finished downloading {name}")

    # Return means "give back this result"
    return f"{name} downloaded"


# Another function for single task approach
async def single_task():
    print("=== SINGLE TASK ===")  # Just a title

    # time.time() gets the current time (like looking at a stopwatch)
    start = time.time()

    # The word "await" means "wait for this to finish before continuing"
    # So we wait for File1 to finish, THEN start File2, THEN start File3
    result1 = await download_file("File1", 2)  # This takes 2 seconds
    result2 = await download_file("File2", 3)  # This takes 3 seconds
    result3 = await download_file("File3", 1)  # This takes 1 second

    # Get the current time again and calculate how long everything took
    end = time.time()
    print(f"Total time: {end - start:.0f} seconds\n")


# Function for multi task approach
async def multi_task():
    print("=== MULTI TASK ===")  # Just a title

    start = time.time()  # Start our timer

    # asyncio.gather() is like saying "start all of these at the same time"
    # Instead of waiting for each one to finish, they all run together
    results = await asyncio.gather(
        download_file("File1", 2),  # These three lines all start
        download_file("File2", 3),  # at the same time, not one
        download_file("File3", 1),  # after another
    )

    end = time.time()  # Stop our timer
    print(f"Total time: {end - start:.0f} seconds")


# The main function that runs everything
async def main():
    # First run the single task example
    await single_task()
    # Then run the multi task example
    await multi_task()


# This line actually starts the program
# asyncio.run() is like pressing the "start" button
asyncio.run(main())
