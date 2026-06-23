#!/usr/bin/env sh

set -u

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR" || exit 1

pass() {
  printf "PASS: %s\n" "$1"
}

fail() {
  printf "FAIL: %s\n" "$1"
  exit 1
}

case "${1:-}" in
  01)
    [ -f answers/01-navigation.txt ] || fail "missing answers/01-navigation.txt"
    grep -q "/Users/zhangjie/Desktop/code-practise/terminal" answers/01-navigation.txt \
      || fail "answers/01-navigation.txt should contain the project absolute path"
    pass "01 navigation"
    ;;
  02)
    [ -d workspace/notes ] || fail "missing workspace/notes"
    [ -f workspace/notes/day-1.txt ] || fail "missing workspace/notes/day-1.txt"
    grep -q "learn terminal commands" workspace/notes/day-1.txt \
      || fail "day-1.txt should contain the practice sentence"
    [ -f workspace/notes/checklist.txt ] || fail "missing copied checklist"
    [ ! -e workspace/notes/delete-me.txt ] || fail "delete-me.txt should be removed"
    grep -q "done" answers/02-files.txt 2>/dev/null || fail "answers/02-files.txt should contain done"
    pass "02 files"
    ;;
  03)
    grep -q "ERROR failed to read config file" answers/03-error-line.txt 2>/dev/null \
      || fail "answers/03-error-line.txt should contain the ERROR log line"
    grep -q "noodles.txt" answers/03-salt-file.txt 2>/dev/null \
      || fail "answers/03-salt-file.txt should mention noodles.txt"
    pass "03 search"
    ;;
  04)
    [ -f workspace/fruits-unique.txt ] || fail "missing workspace/fruits-unique.txt"
    [ "$(wc -l < workspace/fruits-unique.txt | tr -d ' ')" = "5" ] \
      || fail "workspace/fruits-unique.txt should have 5 unique fruits"
    grep -q "Ada,Shanghai,Engineer" workspace/shanghai-people.csv 2>/dev/null \
      || fail "workspace/shanghai-people.csv should include Ada"
    grep -q "Grace,Shanghai,Manager" workspace/shanghai-people.csv 2>/dev/null \
      || fail "workspace/shanghai-people.csv should include Grace"
    grep -q "5" answers/04-unique-count.txt 2>/dev/null \
      || fail "answers/04-unique-count.txt should include 5"
    pass "04 pipes and redirection"
    ;;
  05)
    grep -q "hello terminal" answers/05-hello.txt 2>/dev/null \
      || fail "answers/05-hello.txt should contain hello terminal"
    grep -q "killed" answers/05-process.txt 2>/dev/null \
      || fail "answers/05-process.txt should contain killed"
    pass "05 permissions and processes"
    ;;
  06)
    git rev-parse --is-inside-work-tree >/dev/null 2>&1 \
      || fail "this directory should be initialized as a Git repository"
    grep -q "git practice started" answers/06-git.txt 2>/dev/null \
      || fail "answers/06-git.txt should contain git practice started"
    git log --oneline -1 >/dev/null 2>&1 \
      || fail "there should be at least one Git commit"
    pass "06 git basics"
    ;;
  *)
    printf "Usage: ./scripts/check.sh 01|02|03|04|05|06\n"
    exit 1
    ;;
esac
