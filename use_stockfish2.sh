
cat <<EOF | ./stockfish-dd-64-modern

setoption name Hash value 1024

setoption name Skill Level value 20

setoption name Threads value 4

position startpos moves $@

go movetime 5000

EOF
