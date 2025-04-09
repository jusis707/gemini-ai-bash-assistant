#!/bin/bash
# Gemini-AI assistant for automation via bash/python. Credits: https://www.linkedin.com/in/juris-embergs-054b8326/
# Juris Embergs embergs.usa@gmail.com

# Configuration
MONITORED_FILE="./gemini.out"
LOG_FILE="./code_execution.log"
TIMESTAMP_FORMAT="%Y%m%d_%H%M%S"

# Function to log messages
log_message() {
  local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
  echo "$timestamp: $1" >> "$LOG_FILE"
}

# Function to execute the code and log the output
execute_code() {
  local code_file="$1"
  local timestamp=$(date "+%Y-%m-%d_%H%M%S")
  local log_prefix="Execution of $code_file"
  local output

  log_message "$log_prefix started."

  output=$(bash "$code_file" 2>&1)
  local exit_code=$?

  if [ $exit_code -eq 0 ]; then
    log_message "$log_prefix finished successfully."
    log_message "Prefix_good $log_prefix"
    log_message "$code_block"
    log_message "--- CODE $log_prefix EXECUTED SUCCESSFULY ---"
  else
    log_message "$log_prefix failed with exit code $exit_code."
    log_message "Prefix_bad $log_prefix"
    log_message "$code_block"
    log_message "--- CODE $log_prefix FAILED ---"
  fi
  if [ -n "$output" ]; then
    log_message "$log_prefix output:\n$output"
  fi

  # rm -f "$code_file"
  echo "$output"
}

# Main loop to monitor the file
tail -n 0 -f "$MONITORED_FILE" | while IFS= read -r line; do
  if [[ "$line" == "CODE-START" ]]; then
    log_message "Detected CODE-START."
    code_block=""
    while IFS= read -r code_line; do
      if [[ "$code_line" == "CODE-END" ]]; then
        log_message "Detected CODE-END. Processing code block."
        timestamp=$(date "+$TIMESTAMP_FORMAT")
        code_file="executed_code_${timestamp}.sh"
        echo "$code_block" > "$code_file"
        chmod +x "$code_file"
        execution_output=$(execute_code "$code_file")

        # Execute the Python script with the output of the previous execution
        # python_command="python3 gemini.py -i '${execution_output//\'/\'}' | tee -a $MONITORED_FILE"
        # log_message "Executing Python command: $python_command"
        # eval "$python_command"
        rm -f "$code_file"
        break
      else
        code_block="$code_block"$'\n'"$code_line"
      fi
    done
  fi
done

echo "Monitoring of '$MONITORED_FILE' started. Logs will be written to '$LOG_FILE'."
echo "Press Ctrl+C to stop."
