
cat <<EOF | ./stockfish-dd-64-modern

setoption name Hash value 1024

setoption name Skill Level value 20

setoption name Aggressiveness value 200

setoption name Threads value 4

position fen $1 $2 $3

go depth 20

EOF
