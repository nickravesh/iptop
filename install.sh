#!/bin/bash

# Define ANSI color codes
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
RESET="\033[0m"  # Reset color

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Define the target directory path
TARGET_DIR="$HOME/.local/bin/iptop"

# Check if the directory already exists
if [ -d "$TARGET_DIR" ]; then
  echo -e "${YELLOW}Directory already exists: $TARGET_DIR${RESET}"
else
  # Create the directory and its parent directories
  if mkdir -p "$TARGET_DIR"; then
    echo -e "${GREEN}Directory created: $TARGET_DIR${RESET}"
  else
    echo -e "${RED}Failed to create directory: $TARGET_DIR${RESET}"
    exit 1
  fi
fi

# Move files to the target directory
echo -e "${YELLOW}MOVING THE FILES...${RESET}"
if cp -r "$SCRIPT_DIR"/* "$TARGET_DIR"; then
  cd "$TARGET_DIR"
  echo -e "${GREEN}MOVING... DONE!${RESET}"
else
  echo -e "${RED}Failed to move files. Aborting installation.${RESET}"
  exit 1
fi

# Configure aliases
echo -e "${YELLOW}ONE MOMENT... SETTING THINGS UP...${RESET}"
{
  echo "alias iptop='python3 $HOME/.local/bin/iptop/iptop.py'"
} >> ~/.bashrc

echo -e "${GREEN}ALL DONE!${RESET}"
echo "iptop has been sucesfully installed."
echo "Now just type 'iptop' to get started."

# Return to the original directory
cd "$SCRIPT_DIR"
bash