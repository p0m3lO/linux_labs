import sys

def check_task():
    # ... Your check logic here ...
    success = True  # Set this to True or False based on the check logic

    if success:
        print("Task 1 check: Success")
        sys.exit(0)  # Success
    else:
        print("Task 1 check: Failure")
        sys.exit(1)  # Failure

if __name__ == "__main__":
    check_task()
