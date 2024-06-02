# For using torch on ubuntu
export LD_LIBRARY_PATH="$VIRTUAL_ENV/lib64/python3.11/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH"

# For using matlab on ubuntu
alias matlab='/usr/local/MATLAB/R2024a/bin/matlab'

# Start matlab
nohup matlab >/dev/null & disown

cd ./notes-interactive 

find . -type f -size +50M -exec printf "Warning, file larger than GitHub recommended max size: %s\n" {} \;

