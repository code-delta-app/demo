#!/bin/sh
export OLLAMA_HOST=127.0.0.1:11434
CMD=$(ollama run llama3 "give one shell command that lists the home directory")
eval "$CMD"
