#!/bin/bash

sync_clipboard() {
  echo "$1" | clip.exe
}

sync_clipboard "Text to copy"