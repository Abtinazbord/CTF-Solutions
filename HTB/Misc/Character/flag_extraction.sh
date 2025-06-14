#!/bin/bash

# Replace with actual server address and port
HOST="94.237.57.57"
PORT=58323
echo "The server is: $HOST"
echo "The port is: $PORT"

# Temp file to collect responses
TMPFILE=$(mktemp)

# Initialize the response variable to hold the full string
FULL_RESPONSE=""

# Start the index at 0
START_INDEX=0

# Loop indefinitely until the flag is complete
while true; do
    # Send the current index to the server and capture the response
    RESPONSE=$(echo "$START_INDEX" | nc -q 1 "$HOST" "$PORT")

    # Output the raw response for debugging
    echo "Sent index $START_INDEX to server, received response: $RESPONSE"

    # Extract only the relevant part of the response (Character part)
    CHARACTER=$(echo "$RESPONSE" | sed -n 's/.*Character at Index [0-9]*: \(.\)/\1/p')

    # If we successfully extracted the character, append it
    if [ -n "$CHARACTER" ]; then
        FULL_RESPONSE="$FULL_RESPONSE$CHARACTER"
        echo "Extracted character: $CHARACTER"
    else
        echo "Failed to extract character for index $START_INDEX"
    fi

    # Check if the flag is complete (e.g., contains '}')
    if [[ "$FULL_RESPONSE" == *"}"* ]]; then
        echo "Flag complete: $FULL_RESPONSE"
        break
    fi

    # Increment the index for the next request
    ((START_INDEX++))
done

# Clean up
rm "$TMPFILE"
