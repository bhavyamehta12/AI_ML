# Step 1: Create the original file
with open('run_state.txt', 'w', encoding='utf-8') as file:
    file.write('STATE=RUNNING\nLAST=2026-10-28\n')


# Step 2: Update both lines using r+
with open('run_state.txt', 'r+', encoding='utf-8') as file:
    file.seek(0)

    file.write('STATE=COMPLETE\nLAST=2026-10-29\n')

    file.truncate()

    # Return to the beginning and read the updated file
    file.seek(0)
    print(file.read())