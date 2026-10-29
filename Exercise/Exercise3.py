max_retries_text = input("Maximum retries (0-10): ").strip()
response_text = input("Response codes (comma-separated): ").strip()

retryable_codes = {408, 429, 500, 502, 503, 504}

# Step 1: Validate maximum retries
if not max_retries_text.isascii() or not max_retries_text.isdigit():
    valid_input = False
    error_message = "Maximum retries must be an integer."
else:
    max_retries = int(max_retries_text)

    if not 0 <= max_retries <= 10:
        valid_input = False
        error_message = "Maximum retries must be between 0 and 10."
    else:
        valid_input = True

# Step 2: Validate the entire response sequence
if valid_input:
    parts = [part.strip() for part in response_text.split(",")]
    print(parts)
    if any(
        not part or not part.isascii() or not part.isdigit()
        for part in parts
    ):
        valid_input = False
        error_message = "Every response code must be an integer."
    else:
        codes = [int(part) for part in parts]

        if any(not 100 <= code <= 599 for code in codes):
            valid_input = False
            error_message = "HTTP status codes must be between 100 and 599."

# Step 3: Reject invalid input before simulation
if not valid_input:
    print("\nError:", error_message)
    print("Outcome: INVALID_INPUT")
    print("Attempts made: 0")
    print("Last HTTP status: N/A")

else:
    attempt_limit = max_retries + 1
    attempts_made = 0
    last_status = None
    outcome = None

    # Process only the responses within the permitted attempt limit
    for attempt, status in enumerate(codes[:attempt_limit], start=1):
        attempts_made = attempt
        last_status = status

        if 200 <= status <= 299:
            print(f"Attempt {attempt}: HTTP {status} — success")
            outcome = "SUCCESS"
            break

        elif status in retryable_codes:
            if attempt == attempt_limit:
                print(
                    f"Attempt {attempt}: HTTP {status} "
                    "— retry limit exhausted"
                )
                outcome = "RETRY_LIMIT_EXHAUSTED"
                break
            else:
                print(
                    f"Attempt {attempt}: HTTP {status} "
                    "— retryable error"
                )

        else:
            print(
                f"Attempt {attempt}: HTTP {status} "
                "— non-retryable failure"
            )
            outcome = "FAILURE"
            break

    else:
        # The supplied trace ended before a final outcome was reached
        outcome = "INCOMPLETE_TRACE"
        print("The response sequence ended before the outcome was known.")

    # Step 4: Print the final report
    print("\n========== API RETRY REPORT ==========")
    print(f"Outcome: {outcome}")
    print(f"Attempts made: {attempts_made}")

    if last_status is not None:
        print(f"Last HTTP status: {last_status}")
    else:
        print("Last HTTP status: N/A")